"""Workflow orchestrator runtime — A-1.

Turns the declarative YAML workflows in
``bots/shared/workflows/business/*.yaml`` into executable
conversation flows. For each workflow phase the runtime:

  1. Loads the lead persona's system prompt from
     ``bots/shared/personas/gtm/<key>.md``
  2. Builds the per-phase user prompt from the YAML
     (questions + accumulated context + tension framing)
  3. Calls the LLM provider from
     ``epic_intelligence.synthesis.provider`` (pluggable;
     stub by default so tests run without API keys)
  4. Appends typed memory events for every emit declared
     by the workflow

Pluggable everywhere it matters: persona-file loader, LLM provider,
event sink. The CLI wires real defaults; tests inject fakes.

End-to-end:

    workflow YAML  ─►  load_workflow  ─►  Workflow
                                            │
                                            ▼
    persona registry  ─►  load_persona  ─►  Persona
                                            │
                                            ▼
                                       WorkflowRunner.run
                                            │
                                            ▼
                                       WorkflowResult
                                       (phase results +
                                        emitted event ids +
                                        backpressure status)
"""
from .loader import Workflow, WorkflowPhase, load_workflow, list_workflows
from .persona import Persona, load_persona
from .runner import (
    PhaseResult,
    RunnerConfig,
    WorkflowResult,
    WorkflowRunner,
)

__all__ = [
    "Persona",
    "PhaseResult",
    "RunnerConfig",
    "Workflow",
    "WorkflowPhase",
    "WorkflowResult",
    "WorkflowRunner",
    "list_workflows",
    "load_persona",
    "load_workflow",
]
