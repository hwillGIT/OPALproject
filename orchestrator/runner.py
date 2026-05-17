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
from typing import Callable, Mapping, Sequence

from memory_system.events import Event, new_event
from memory_system.events.write import append_event
from memory_system.ontology.predicates import (
    Predicate,
    evaluate_trigger,
    load_predicates,
)

from .emit_parser import ParsedEmit, ParseResult, parse_emits
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
    """The output of one phase's execution.

    ``response_text`` is the persona's reply with any ``memory-emit``
    fenced blocks already stripped — safe to surface to the operator.
    ``raw_response_text`` keeps the original for audit.
    ``triggered_predicates`` maps predicate id -> events that matched,
    surfacing meaning the consumer (briefing, reviewer) should know.
    """

    phase: WorkflowPhase
    persona: Persona
    response_text: str
    emitted_event_ids: tuple[str, ...]
    prompt_user: str  # for audit
    raw_response_text: str = ""
    triggered_predicates: Mapping[str, tuple[str, ...]] = field(default_factory=dict)


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
    parse_result: ParseResult,
    event_sink: EventSink,
) -> tuple[Event, ...]:
    """Append one Event per persona-authored emit + one CONTEXT_CHANGE
    per malformed attempt the persona made.

    Vocabulary enforcement: events whose type isn't in
    ``workflow.emits`` are demoted to CONTEXT_CHANGE so the persona's
    intent is preserved but the workflow's contract is honored. Zero
    valid emits produces zero events (the persona judged nothing
    worth recording) — that's the right answer, not a bug.
    """
    base_tags = tuple({
        workflow.name,
        workflow.domain,
        phase.id,
        *phase.tensions,
    })
    allowed = set(workflow.emits)
    appended: list[Event] = []

    for parsed in parse_result.emits:
        if parsed.type in allowed:
            event_type = parsed.type
            demoted_reason = None
        else:
            event_type = "CONTEXT_CHANGE"
            demoted_reason = (
                f"persona emitted {parsed.type!r} but this phase only "
                f"permits {sorted(allowed)}"
            )

        metadata: dict = {
            "lead_persona": persona.key,
            "phase_output_target": phase.output,
        }
        if parsed.confidence is not None:
            metadata["confidence"] = parsed.confidence
        if event_type == "ACTION":
            metadata.setdefault("status", "open")
            metadata.setdefault("owner", persona.key)
        if demoted_reason:
            metadata["original_type"] = parsed.type
            metadata["demotion_reason"] = demoted_reason

        ev = new_event(
            type=event_type,
            actor=persona.key,
            workflow=workflow.name,
            phase=phase.id,
            title=parsed.title[:200],
            content=(parsed.content or parse_result.clean_text or "(no body)")[:8000],
            tags=tuple({*base_tags, *parsed.tags}),
            related=parsed.related,
            metadata=metadata,
        )
        event_sink(ev)
        appended.append(ev)

    for malformed in parse_result.malformed:
        ev = new_event(
            type="CONTEXT_CHANGE",
            actor=persona.key,
            workflow=workflow.name,
            phase=phase.id,
            title=f"malformed memory-emit from {persona.key} in {phase.id}",
            content=(
                f"reason: {malformed.reason}\n\n"
                f"raw block:\n{malformed.raw}"
            )[:8000],
            tags=tuple({*base_tags, "malformed-emit"}),
            metadata={
                "lead_persona": persona.key,
                "malformed_emit": True,
                "reason": malformed.reason,
            },
        )
        event_sink(ev)
        appended.append(ev)

    return tuple(appended)


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


class WorkflowRunner:
    """Executes a Workflow phase-by-phase against an LLM provider.

    The persona authors a fenced ``memory-emit`` block alongside its
    prose reply when something is worth recording; the runner parses
    it out, validates against the phase's emit vocabulary, appends
    typed events, and runs ``post_write`` predicates over the new
    events so consumers see which patterns the emit matched.
    """

    def __init__(
        self,
        provider=None,
        *,
        persona_loader: PersonaLoader | None = None,
        event_sink: EventSink | None = None,
        config: RunnerConfig | None = None,
        predicates: Sequence[Predicate] | None = None,
    ) -> None:
        self._provider = provider if provider is not None else default_provider()
        self._persona_loader = persona_loader or (lambda k: load_persona(k))
        self._event_sink = event_sink or (lambda ev: append_event(ev))
        self._config = config or RunnerConfig()
        self._predicates = list(predicates) if predicates is not None else _default_predicates()

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
            raw_response = self._provider.complete(
                system_prompt=persona.system_prompt,
                user_prompt=user_prompt,
                max_tokens=self._config.max_tokens_per_phase,
                temperature=self._config.temperature,
            )
            parse_result = parse_emits(raw_response)
            appended = _emit_events_for_phase(
                workflow=workflow,
                phase=phase,
                persona=persona,
                parse_result=parse_result,
                event_sink=self._event_sink,
            )
            triggered = _run_post_write_predicates(self._predicates, appended)

            results.append(PhaseResult(
                phase=phase,
                persona=persona,
                response_text=parse_result.clean_text,
                emitted_event_ids=tuple(ev.id for ev in appended),
                prompt_user=user_prompt,
                raw_response_text=raw_response,
                triggered_predicates=triggered,
            ))
            prior_summaries.append(summarize_phase(phase, parse_result.clean_text))

        return WorkflowResult(
            workflow=workflow,
            phase_results=tuple(results),
            backpressure_status="unevaluated",
            provider_name=self.provider_name,
            model_name=self.model_name,
        )


# ---------------------------------------------------------------------------
# Predicates wiring
# ---------------------------------------------------------------------------


_PREDICATES_PATH = Path(__file__).resolve().parent.parent / "memory_system" / "ontology" / "predicates.json"


def _default_predicates() -> list[Predicate]:
    """Load the project's standard predicate set; empty list on failure."""
    try:
        return load_predicates(_PREDICATES_PATH)
    except (FileNotFoundError, ValueError):
        return []


def _run_post_write_predicates(
    predicates: Sequence[Predicate],
    appended: Sequence[Event],
) -> Mapping[str, tuple[str, ...]]:
    """Run post_write predicates over the just-emitted events.

    Returns ``{predicate_id -> tuple of matching event ids}`` only for
    predicates that matched something — empty matches are dropped so
    the result is a punch list of "patterns this phase tripped."
    """
    if not predicates or not appended:
        return {}
    event_dicts = [ev.to_dict() for ev in appended]
    matched = evaluate_trigger(predicates, "post_write", event_dicts)
    return {pid: tuple(e["id"] for e in events)
            for pid, events in matched.items() if events}
