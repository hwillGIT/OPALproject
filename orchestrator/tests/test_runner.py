"""Unit tests for the workflow runner.

The runner no longer fabricates one event per declared emit type —
it parses persona-authored ``memory-emit`` blocks out of the LLM
response, validates them against the phase's emit vocabulary, and
appends typed events with the persona's stated fields. These tests
inject a stub provider that returns canned responses (including
emit blocks), a fake persona loader, and an in-memory event sink.
"""
from __future__ import annotations

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
# Fixtures
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
    emits: tuple[str, ...] = ("DECISION", "ACTION", "INSIGHT", "PREDICTION"),
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
    name = "stub-runner"
    model = "stub-model"

    def __init__(self, responses: list[str] | None = None) -> None:
        self._responses = list(responses or [])
        self.calls: list[dict] = []

    def complete(self, system_prompt, user_prompt, max_tokens=1024, temperature=0.3):
        self.calls.append({
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
        })
        if self._responses:
            return self._responses.pop(0)
        # Default: prose + one minimal DECISION emit so downstream
        # assertions can run without us spelling out a response per test.
        return (
            "stub prose.\n\n"
            "```memory-emit\n"
            "- type: DECISION\n"
            "  title: stub decision\n"
            "```\n"
        )


# --------------------------------------------------------------------------
# Pure helpers (unchanged from A-1)
# --------------------------------------------------------------------------


class TestBuildPhasePrompt:
    def test_prompt_includes_workflow_phase_persona_questions(self) -> None:
        wf = _make_workflow()
        text = build_phase_prompt(
            workflow=wf, phase=wf.phases[0], persona=_make_persona("strategist"),
            prior_phase_summaries=(), config=RunnerConfig(),
        )
        assert "WORKFLOW: test-wf (testing)" in text
        assert "PHASE: frame" in text
        assert "Strategist Role" in text
        assert "what is the strategic frame?" in text
        assert "speed vs rigor" in text
        assert "ORCHESTRATION PATTERN: single-lead" in text

    def test_prompt_includes_prior_summaries_and_context(self) -> None:
        wf = _make_workflow()
        text = build_phase_prompt(
            workflow=wf, phase=wf.phases[1], persona=_make_persona("critic"),
            prior_phase_summaries=["[frame] punchy frame -- body"],
            config=RunnerConfig(initial_context="operator says: be skeptical"),
        )
        assert "OPERATOR CONTEXT:" in text
        assert "be skeptical" in text
        assert "[frame] punchy frame" in text


class TestSummarizePhase:
    def test_summary_is_bounded(self) -> None:
        phase = WorkflowPhase(id="long", lead="x", questions=("q",), output="o")
        body = "first line\n" + ("body " * 1000)
        s = summarize_phase(phase, body, max_chars=200)
        assert s.startswith("[long] first line")
        assert s.endswith("...")
        assert len(s) < 500


# --------------------------------------------------------------------------
# Runner end-to-end with persona-authored emits
# --------------------------------------------------------------------------


class TestEmitDrivenRunner:
    def test_persona_with_no_emit_block_produces_zero_events(self) -> None:
        wf = _make_workflow()
        provider = StubProvider(responses=[
            "just prose, no emit\n",
            "more prose\n",
        ])
        sink: list = []
        runner = WorkflowRunner(
            provider=provider,
            persona_loader=_make_persona,
            event_sink=sink.append,
            predicates=[],
        )
        result = runner.run(wf)
        assert sink == []
        for pr in result.phase_results:
            assert pr.emitted_event_ids == ()

    def test_persona_emit_lands_as_typed_event(self) -> None:
        wf = _make_workflow()
        provider = StubProvider(responses=[
            (
                "Here's my call.\n\n"
                "```memory-emit\n"
                "- type: DECISION\n"
                "  title: We go with ESP32-S3\n"
                "- type: ACTION\n"
                "  title: Order 10 dev boards\n"
                "```\n"
            ),
            "no emit from phase 2\n",
        ])
        sink: list = []
        runner = WorkflowRunner(
            provider=provider,
            persona_loader=_make_persona,
            event_sink=sink.append,
            predicates=[],
        )
        result = runner.run(wf)
        assert [ev.type for ev in sink] == ["DECISION", "ACTION"]
        assert sink[0].title == "We go with ESP32-S3"
        assert sink[0].actor == "strategist"
        assert sink[1].metadata["status"] == "open"
        assert sink[1].metadata["owner"] == "strategist"
        # Phase 1 result must reflect both events; phase 2 zero
        assert len(result.phase_results[0].emitted_event_ids) == 2
        assert result.phase_results[1].emitted_event_ids == ()

    def test_clean_text_strips_emit_block(self) -> None:
        wf = _make_workflow()
        provider = StubProvider(responses=[
            (
                "User-visible prose.\n\n"
                "```memory-emit\n"
                "- type: DECISION\n"
                "  title: x\n"
                "```\n"
            ),
            "phase 2\n",
        ])
        runner = WorkflowRunner(
            provider=provider, persona_loader=_make_persona,
            event_sink=lambda ev: None, predicates=[],
        )
        result = runner.run(wf)
        assert "memory-emit" not in result.phase_results[0].response_text
        assert "User-visible prose." in result.phase_results[0].response_text
        # Raw is preserved for audit
        assert "memory-emit" in result.phase_results[0].raw_response_text

    def test_type_outside_vocabulary_demoted_to_context_change(self) -> None:
        # Workflow allows DECISION only; persona emits OUTCOME
        wf = _make_workflow(emits=("DECISION",))
        provider = StubProvider(responses=[
            (
                "prose\n\n"
                "```memory-emit\n"
                "- type: OUTCOME\n"
                "  title: shipped on time\n"
                "```\n"
            ),
            "phase 2\n",
        ])
        sink: list = []
        runner = WorkflowRunner(
            provider=provider, persona_loader=_make_persona,
            event_sink=sink.append, predicates=[],
        )
        runner.run(wf)
        assert len(sink) == 1
        assert sink[0].type == "CONTEXT_CHANGE"
        assert sink[0].metadata["original_type"] == "OUTCOME"
        assert "only permits" in sink[0].metadata["demotion_reason"]

    def test_malformed_emit_recorded_as_context_change(self) -> None:
        wf = _make_workflow()
        provider = StubProvider(responses=[
            (
                "prose\n\n"
                "```memory-emit\n"
                "- type: PREDICTION\n"
                "  title: missing confidence\n"
                "```\n"
            ),
            "phase 2\n",
        ])
        sink: list = []
        runner = WorkflowRunner(
            provider=provider, persona_loader=_make_persona,
            event_sink=sink.append, predicates=[],
        )
        runner.run(wf)
        assert len(sink) == 1
        assert sink[0].type == "CONTEXT_CHANGE"
        assert sink[0].metadata["malformed_emit"] is True
        assert "confidence" in sink[0].metadata["reason"]

    def test_persona_confidence_carried_through_to_metadata(self) -> None:
        wf = _make_workflow()
        provider = StubProvider(responses=[
            (
                "```memory-emit\n"
                "- type: PREDICTION\n"
                "  title: device ships in Q3\n"
                "  confidence: 0.85\n"
                "```\n"
            ),
            "phase 2\n",
        ])
        sink: list = []
        runner = WorkflowRunner(
            provider=provider, persona_loader=_make_persona,
            event_sink=sink.append, predicates=[],
        )
        runner.run(wf)
        assert sink[0].metadata["confidence"] == 0.85

    def test_persona_tags_merged_with_phase_tags(self) -> None:
        wf = _make_workflow()  # phase 1 tensions: "speed vs rigor"
        provider = StubProvider(responses=[
            (
                "```memory-emit\n"
                "- type: DECISION\n"
                "  title: x\n"
                "  tags: [esp32, hardware]\n"
                "```\n"
            ),
            "phase 2\n",
        ])
        sink: list = []
        runner = WorkflowRunner(
            provider=provider, persona_loader=_make_persona,
            event_sink=sink.append, predicates=[],
        )
        runner.run(wf)
        tags = set(sink[0].tags)
        assert {"esp32", "hardware", "test-wf", "testing", "frame", "speed vs rigor"} <= tags

    def test_provider_called_with_persona_system_prompt(self) -> None:
        wf = _make_workflow()
        provider = StubProvider()
        runner = WorkflowRunner(
            provider=provider, persona_loader=_make_persona,
            event_sink=lambda ev: None, predicates=[],
        )
        runner.run(wf)
        assert provider.calls[0]["system_prompt"] == "system prompt for strategist"
        assert provider.calls[1]["system_prompt"] == "system prompt for critic"

    def test_prior_clean_text_flows_into_next_phase_prompt(self) -> None:
        wf = _make_workflow()
        provider = StubProvider(responses=[
            (
                "FRAMING ANSWER\nmore detail\n\n"
                "```memory-emit\n- type: DECISION\n  title: x\n```\n"
            ),
            "CRITIQUE\n",
        ])
        runner = WorkflowRunner(
            provider=provider, persona_loader=_make_persona,
            event_sink=lambda ev: None, predicates=[],
        )
        runner.run(wf)
        second_user = provider.calls[1]["user_prompt"]
        assert "PRIOR PHASES" in second_user
        assert "[frame]" in second_user
        assert "FRAMING ANSWER" in second_user
        # Emit block must NOT leak into next phase's prompt
        assert "memory-emit" not in second_user

    def test_runner_propagates_persona_loader_error(self) -> None:
        wf = _make_workflow()

        def angry_loader(key: str) -> Persona:
            raise RuntimeError(f"can't load {key}")

        runner = WorkflowRunner(
            provider=StubProvider(), persona_loader=angry_loader,
            event_sink=lambda ev: None, predicates=[],
        )
        with pytest.raises(RuntimeError, match="can't load strategist"):
            runner.run(wf)

    def test_provider_and_model_name_propagated(self) -> None:
        wf = _make_workflow()
        runner = WorkflowRunner(
            provider=StubProvider(), persona_loader=_make_persona,
            event_sink=lambda ev: None, predicates=[],
        )
        result = runner.run(wf)
        assert result.provider_name == "stub-runner"
        assert result.model_name == "stub-model"


# --------------------------------------------------------------------------
# Post-write predicates
# --------------------------------------------------------------------------


class TestPostWritePredicates:
    def test_loaded_default_predicates_trip_on_action(self) -> None:
        wf = _make_workflow()
        provider = StubProvider(responses=[
            (
                "```memory-emit\n"
                "- type: ACTION\n"
                "  title: do the thing\n"
                "```\n"
            ),
            "no emit\n",
        ])
        sink: list = []
        runner = WorkflowRunner(
            provider=provider, persona_loader=_make_persona,
            event_sink=sink.append,
            # predicates=None -> loads from memory_system/ontology/predicates.json
        )
        result = runner.run(wf)
        triggered = result.phase_results[0].triggered_predicates
        # The ACTION should trip 'matches-open-action'
        assert "matches-open-action" in triggered
        assert len(triggered["matches-open-action"]) == 1

    def test_empty_predicates_means_empty_triggered_field(self) -> None:
        wf = _make_workflow()
        runner = WorkflowRunner(
            provider=StubProvider(), persona_loader=_make_persona,
            event_sink=lambda ev: None, predicates=[],
        )
        result = runner.run(wf)
        for pr in result.phase_results:
            assert pr.triggered_predicates == {}
