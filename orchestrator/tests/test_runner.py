"""Unit tests for the workflow runner.

Everything injectable is injected here: a stub LLM provider that
echoes its inputs, a fake persona loader that hands back a pre-baked
Persona for each lead key, and an in-memory event sink that collects
emitted events so we can assert on them. No filesystem, no network.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from orchestrator.loader import Workflow, WorkflowPhase
from orchestrator.persona import Persona
from orchestrator.runner import (
    PhaseResult,
    RunnerConfig,
    WorkflowResult,
    WorkflowRunner,
    build_phase_prompt,
    summarize_phase,
)


# --------------------------------------------------------------------------
# Fixtures: tiny in-memory workflow + persona registry + LLM provider
# --------------------------------------------------------------------------


def _make_persona(key: str) -> Persona:
    return Persona(
        key=key,
        name=key.title(),
        label=f"{key.title()} Role",
        system_prompt=f"system prompt for {key}",
        source_path=None,
    )


def _make_workflow(
    *,
    phases: tuple[WorkflowPhase, ...] | None = None,
    emits: tuple[str, ...] = ("DECISION",),
) -> Workflow:
    if phases is None:
        phases = (
            WorkflowPhase(
                id="frame",
                lead="strategist",
                questions=("what is the strategic frame?",),
                output="a one-sentence strategic frame",
                supporting=("product-owner",),
                tensions=("speed vs rigor",),
                pattern="single-lead",
            ),
            WorkflowPhase(
                id="critique",
                lead="critic",
                questions=("what could go wrong?",),
                output="3 failure modes",
            ),
        )
    return Workflow(
        name="test-wf",
        category="business",
        domain="testing",
        version="1.0",
        description="for the test suite",
        backpressure=("ship before tuesday",),
        phases=phases,
        emits=emits,
    )


class StubProvider:
    """Records the calls it received and returns canned responses."""

    name = "stub-runner"
    model = "stub-model"

    def __init__(self, responses: list[str] | None = None) -> None:
        self._responses = list(responses or [])
        self.calls: list[dict] = []

    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int = 1024,
        temperature: float = 0.3,
    ) -> str:
        self.calls.append({
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
        })
        if self._responses:
            return self._responses.pop(0)
        return f"stub-response[len={len(user_prompt)}]"


# --------------------------------------------------------------------------
# Pure helpers
# --------------------------------------------------------------------------


class TestBuildPhasePrompt:
    def test_prompt_includes_workflow_phase_persona_questions(self) -> None:
        wf = _make_workflow()
        phase = wf.phases[0]
        persona = _make_persona("strategist")
        text = build_phase_prompt(
            workflow=wf, phase=phase, persona=persona,
            prior_phase_summaries=(),
            config=RunnerConfig(),
        )
        assert "WORKFLOW: test-wf (testing)" in text
        assert "PHASE: frame" in text
        assert "Strategist Role" in text
        assert "what is the strategic frame?" in text
        assert "EXPECTED OUTPUT: a one-sentence strategic frame" in text
        assert "speed vs rigor" in text
        assert "ORCHESTRATION PATTERN: single-lead" in text
        assert "PRIOR PHASES" not in text  # nothing prior on phase 1

    def test_prompt_includes_prior_summaries_and_context(self) -> None:
        wf = _make_workflow()
        phase = wf.phases[1]
        persona = _make_persona("critic")
        text = build_phase_prompt(
            workflow=wf, phase=phase, persona=persona,
            prior_phase_summaries=["[frame] punchy frame -- body"],
            config=RunnerConfig(initial_context="operator says: be skeptical"),
        )
        assert "OPERATOR CONTEXT:" in text
        assert "be skeptical" in text
        assert "PRIOR PHASES" in text
        assert "[frame] punchy frame" in text


class TestSummarizePhase:
    def test_summary_is_bounded(self) -> None:
        phase = WorkflowPhase(
            id="long", lead="x", questions=("q",), output="o",
        )
        body = "first line\n" + ("body " * 1000)
        s = summarize_phase(phase, body, max_chars=200)
        assert s.startswith("[long] first line")
        assert s.endswith("...")
        assert len(s) < 500


# --------------------------------------------------------------------------
# Runner end-to-end (in-memory)
# --------------------------------------------------------------------------


class TestWorkflowRunner:
    def test_runs_every_phase_and_emits_one_event_per_emit(self) -> None:
        wf = _make_workflow(emits=("DECISION", "INSIGHT"))
        provider = StubProvider(responses=["strat-out", "critic-out"])
        sink: list = []
        runner = WorkflowRunner(
            provider=provider,
            persona_loader=_make_persona,
            event_sink=sink.append,
        )
        result = runner.run(wf)

        assert isinstance(result, WorkflowResult)
        assert len(result.phase_results) == 2
        # Each phase emits one event per emit type
        assert len(sink) == 4
        types = [ev.type for ev in sink]
        assert types == ["DECISION", "INSIGHT", "DECISION", "INSIGHT"]
        # IDs surfaced on the phase result
        first = result.phase_results[0]
        assert len(first.emitted_event_ids) == 2
        assert first.persona.key == "strategist"
        assert first.response_text == "strat-out"
        # Backpressure is informational for now
        assert result.backpressure_status == "unevaluated"

    def test_provider_called_with_persona_system_prompt(self) -> None:
        wf = _make_workflow()
        provider = StubProvider()
        runner = WorkflowRunner(
            provider=provider,
            persona_loader=_make_persona,
            event_sink=lambda ev: None,
        )
        runner.run(wf)
        assert provider.calls[0]["system_prompt"] == "system prompt for strategist"
        assert provider.calls[1]["system_prompt"] == "system prompt for critic"

    def test_prior_phase_summary_flows_into_next_phase_prompt(self) -> None:
        wf = _make_workflow()
        provider = StubProvider(responses=["FRAMING ANSWER\nmore detail", "CRITIQUE"])
        runner = WorkflowRunner(
            provider=provider,
            persona_loader=_make_persona,
            event_sink=lambda ev: None,
        )
        runner.run(wf)
        # phase #2 prompt should include the phase #1 summary
        second_user = provider.calls[1]["user_prompt"]
        assert "PRIOR PHASES" in second_user
        assert "[frame]" in second_user
        assert "FRAMING ANSWER" in second_user

    def test_action_event_metadata_marks_owner_open(self) -> None:
        wf = _make_workflow(emits=("ACTION",))
        sink: list = []
        runner = WorkflowRunner(
            provider=StubProvider(),
            persona_loader=_make_persona,
            event_sink=sink.append,
        )
        runner.run(wf)
        # Every ACTION event carries owner + status=open
        for ev in sink:
            assert ev.type == "ACTION"
            assert ev.metadata.get("status") == "open"
            assert ev.metadata.get("owner") in {"strategist", "critic"}

    def test_prediction_event_metadata_has_confidence(self) -> None:
        wf = _make_workflow(emits=("PREDICTION",))
        sink: list = []
        runner = WorkflowRunner(
            provider=StubProvider(),
            persona_loader=_make_persona,
            event_sink=sink.append,
        )
        runner.run(wf)
        for ev in sink:
            assert ev.type == "PREDICTION"
            assert ev.metadata.get("confidence") == 0.5

    def test_event_tagged_with_workflow_domain_phase_and_tensions(self) -> None:
        wf = _make_workflow()
        sink: list = []
        runner = WorkflowRunner(
            provider=StubProvider(),
            persona_loader=_make_persona,
            event_sink=sink.append,
        )
        runner.run(wf)
        first = sink[0]
        assert "test-wf" in first.tags
        assert "testing" in first.tags
        assert "frame" in first.tags
        assert "speed vs rigor" in first.tags  # phase 1 had a tension

    def test_response_text_truncated_into_event_content(self) -> None:
        wf = _make_workflow(emits=("INSIGHT",))
        big = "x" * 20_000
        provider = StubProvider(responses=[big, big])
        sink: list = []
        runner = WorkflowRunner(
            provider=provider,
            persona_loader=_make_persona,
            event_sink=sink.append,
        )
        runner.run(wf)
        for ev in sink:
            assert len(ev.content) <= 8000

    def test_runner_propagates_persona_loader_error(self) -> None:
        wf = _make_workflow()

        def angry_loader(key: str) -> Persona:
            raise RuntimeError(f"can't load {key}")

        runner = WorkflowRunner(
            provider=StubProvider(),
            persona_loader=angry_loader,
            event_sink=lambda ev: None,
        )
        with pytest.raises(RuntimeError, match="can't load strategist"):
            runner.run(wf)

    def test_phase_with_no_emits_still_records_phase_result(self) -> None:
        # Workflow that emits a single type — verify the phase result
        # records the prompt_user for audit purposes
        wf = _make_workflow()
        runner = WorkflowRunner(
            provider=StubProvider(),
            persona_loader=_make_persona,
            event_sink=lambda ev: None,
        )
        result = runner.run(wf)
        for pr in result.phase_results:
            assert pr.prompt_user
            assert "WORKFLOW: test-wf" in pr.prompt_user

    def test_provider_and_model_name_propagated(self) -> None:
        wf = _make_workflow()
        runner = WorkflowRunner(
            provider=StubProvider(),
            persona_loader=_make_persona,
            event_sink=lambda ev: None,
        )
        result = runner.run(wf)
        assert result.provider_name == "stub-runner"
        assert result.model_name == "stub-model"
