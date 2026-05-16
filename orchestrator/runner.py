"""Workflow runner — executes a loaded Workflow phase-by-phase.

For each phase:
  1. Load the lead persona's system prompt
  2. Build the user prompt: phase questions + accumulated context +
     tension framing + a short instruction on the expected output
  3. Call the LLM provider (default = stub, no network)
  4. Capture the response into a PhaseResult
  5. Emit one typed memory event per emit-type the workflow declares,
     attributing the event to the lead persona for this phase

After all phases:
  6. Return a WorkflowResult with the per-phase results, the emitted
     event ids, and a backpressure status (currently informational —
     real backpressure evaluation is a future PR)

Pure orchestration. LLM, persona loading, and event sink are all
injected. The CLI wires the real defaults; tests inject fakes.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Sequence

from memory_system.events import Event, new_event
from memory_system.events.write import append_event

from .loader import Workflow, WorkflowPhase
from .persona import Persona, load_persona


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------


# Same shape as `epic_intelligence.synthesis.LlmProvider` — duck-typed.
LlmProvider = object  # any object with .complete(system, user, max_tokens, temperature)
PersonaLoader = Callable[[str], Persona]
EventSink = Callable[[Event], None]


@dataclass(frozen=True)
class RunnerConfig:
    """Tunables for the runner. Sensible defaults; CLI/tests can override."""

    max_tokens_per_phase: int = 1024
    temperature: float = 0.3
    initial_context: str = ""
    operator_actor: str = "orchestrator"


@dataclass(frozen=True)
class PhaseResult:
    """The output of one phase's execution."""

    phase: WorkflowPhase
    persona: Persona
    response_text: str
    emitted_event_ids: tuple[str, ...]
    prompt_user: str  # for audit


@dataclass(frozen=True)
class WorkflowResult:
    """The output of a full workflow run."""

    workflow: Workflow
    phase_results: tuple[PhaseResult, ...]
    backpressure_status: str  # 'unevaluated' for now
    provider_name: str
    model_name: str


# ---------------------------------------------------------------------------
# Default LLM provider — reuse the synthesis stub
# ---------------------------------------------------------------------------


def default_provider():
    """Return the orchestrator's default provider — a deterministic stub.

    Tests + the CLI's default both use this. Pass a real provider into
    ``WorkflowRunner(provider=...)`` (or use ``--provider auto`` on the
    CLI) to swap in Anthropic / OpenAI / Gemini.
    """
    from .provider import StubProvider
    return StubProvider()


# ---------------------------------------------------------------------------
# Prompt construction (pure)
# ---------------------------------------------------------------------------


def build_phase_prompt(
    workflow: Workflow,
    phase: WorkflowPhase,
    persona: Persona,
    prior_phase_summaries: Sequence[str],
    config: RunnerConfig,
) -> str:
    """User prompt for one phase. Pure."""
    lines: list[str] = []
    lines.append(f"WORKFLOW: {workflow.name} ({workflow.domain})")
    lines.append(f"PHASE: {phase.id}  (lead: {persona.label} / {persona.name})")
    if phase.supporting:
        lines.append(f"SUPPORTING PERSONAS (for awareness, you lead):"
                     f" {', '.join(phase.supporting)}")
    if phase.tensions:
        lines.append("PRODUCTIVE TENSIONS THIS PHASE SHOULD SURFACE:")
        for t in phase.tensions:
            lines.append(f"  - {t}")
        lines.append(
            "(Name your side of the tension explicitly. Don't synthesize "
            "with the opposing view — that's the operator's job.)"
        )
    if phase.pattern:
        lines.append(f"ORCHESTRATION PATTERN: {phase.pattern}")
    lines.append("")
    lines.append("QUESTIONS TO ANSWER:")
    for q in phase.questions:
        lines.append(f"  - {q}")
    lines.append("")
    lines.append(f"EXPECTED OUTPUT: {phase.output}")
    if config.initial_context:
        lines.append("")
        lines.append("OPERATOR CONTEXT:")
        lines.append(config.initial_context)
    if prior_phase_summaries:
        lines.append("")
        lines.append("PRIOR PHASES (most recent first):")
        for summary in reversed(prior_phase_summaries):
            lines.append(f"  - {summary}")
    lines.append("")
    lines.append(
        "Respond in character. Lead with the answer; cite specifics; "
        "name the tension explicitly if your phase has one."
    )
    return "\n".join(lines)


def summarize_phase(phase: WorkflowPhase, response_text: str, max_chars: int = 400) -> str:
    """A one-liner for downstream phases to consume as context."""
    head = response_text.strip().splitlines()[0] if response_text.strip() else ""
    body = response_text.strip()[:max_chars]
    suffix = "..." if len(response_text) > max_chars else ""
    return f"[{phase.id}] {head[:120]} -- {body}{suffix}"


# ---------------------------------------------------------------------------
# Event emission
# ---------------------------------------------------------------------------


def _emit_events_for_phase(
    workflow: Workflow,
    phase: WorkflowPhase,
    persona: Persona,
    response_text: str,
    event_sink: EventSink,
) -> tuple[str, ...]:
    """Append one Event per declared emit type for this phase.

    All events from the same phase are tagged with the workflow id +
    phase id so a later query can group them. Each event's actor is
    the lead persona for the phase.
    """
    emitted_ids: list[str] = []
    for event_type in workflow.emits:
        title = f"[{workflow.name}/{phase.id}] {event_type}: {phase.output[:120]}"
        content = response_text or "(no response produced)"
        tags = tuple({
            workflow.name,
            workflow.domain,
            phase.id,
            *phase.tensions,
        })
        metadata: dict = {
            "phase_output_target": phase.output,
            "lead_persona": persona.key,
        }
        if event_type == "ACTION":
            metadata["status"] = "open"
            metadata["owner"] = persona.key
        if event_type == "PREDICTION":
            # Default confidence midpoint. A future PR may parse the
            # response for explicit confidence.
            metadata["confidence"] = 0.5

        ev = new_event(
            type=event_type,
            actor=persona.key,
            workflow=workflow.name,
            phase=phase.id,
            title=title[:200],
            content=content[:8000],
            tags=tags,
            metadata=metadata,
        )
        event_sink(ev)
        emitted_ids.append(ev.id)
    return tuple(emitted_ids)


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


class WorkflowRunner:
    """Executes a Workflow phase-by-phase against an LLM provider."""

    def __init__(
        self,
        provider=None,
        *,
        persona_loader: PersonaLoader | None = None,
        event_sink: EventSink | None = None,
        config: RunnerConfig | None = None,
    ) -> None:
        self._provider = provider if provider is not None else default_provider()
        self._persona_loader = persona_loader or (lambda k: load_persona(k))
        self._event_sink = event_sink or (lambda ev: append_event(ev))
        self._config = config or RunnerConfig()

    @property
    def provider_name(self) -> str:
        return getattr(self._provider, "name", "unknown")

    @property
    def model_name(self) -> str:
        return getattr(self._provider, "model", "unknown")

    def run(self, workflow: Workflow) -> WorkflowResult:
        """Run every phase of the workflow in order, returning a result."""
        prior_summaries: list[str] = []
        results: list[PhaseResult] = []

        for phase in workflow.phases:
            persona = self._persona_loader(phase.lead)
            user_prompt = build_phase_prompt(
                workflow=workflow,
                phase=phase,
                persona=persona,
                prior_phase_summaries=prior_summaries,
                config=self._config,
            )
            response = self._provider.complete(
                system_prompt=persona.system_prompt,
                user_prompt=user_prompt,
                max_tokens=self._config.max_tokens_per_phase,
                temperature=self._config.temperature,
            )
            emitted = _emit_events_for_phase(
                workflow=workflow,
                phase=phase,
                persona=persona,
                response_text=response,
                event_sink=self._event_sink,
            )
            results.append(PhaseResult(
                phase=phase,
                persona=persona,
                response_text=response,
                emitted_event_ids=emitted,
                prompt_user=user_prompt,
            ))
            prior_summaries.append(summarize_phase(phase, response))

        return WorkflowResult(
            workflow=workflow,
            phase_results=tuple(results),
            backpressure_status="unevaluated",
            provider_name=self.provider_name,
            model_name=self.model_name,
        )
