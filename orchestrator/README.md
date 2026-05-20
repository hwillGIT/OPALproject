# orchestrator — workflow runtime (A-1)

Turns the declarative YAML workflows in
`bots/shared/workflows/business/*.yaml` into executable conversation
flows. For each workflow phase the runtime:

1. Loads the lead persona's system prompt from
   `bots/shared/personas/gtm/<key>.md`
2. Builds the per-phase user prompt from the YAML (questions +
   accumulated context + tension framing)
3. Calls the LLM provider (built-in stub by default — no API keys
   needed; pass `--provider auto|anthropic|openai|gemini` for real
   models via the synthesis layer)
4. Appends one typed memory event per emit-type the workflow declares,
   tagged with the workflow + domain + phase + tensions

After all phases it returns a `WorkflowResult` with per-phase
responses, emitted event ids, and a backpressure status (currently
informational — real backpressure evaluation is a future PR).

## CLI

```bash
# list every business workflow on disk
python -m orchestrator.cli list

# print one workflow's structure
python -m orchestrator.cli show clinical-decision-loop

# dry-run end-to-end with the deterministic stub provider
python -m orchestrator.cli run clinical-decision-loop --provider stub --dry-run --json

# real run (writes typed events to data/memory/events.jsonl)
python -m orchestrator.cli run clinical-decision-loop --provider auto --context "operator note"
```

Flags on `run`:

| flag | default | purpose |
|------|---------|---------|
| `--provider` | `stub` | `stub` (no deps) / `auto` / `anthropic` / `openai` / `gemini` |
| `--max-tokens` | 1024 | LLM token budget per phase |
| `--temperature` | 0.3 | LLM temperature per phase |
| `--context` | (none) | operator context prepended to every phase prompt |
| `--dry-run` | off | run phases + build prompts but skip event appends |
| `--json` | off | emit JSON instead of pretty text |

## Programmatic use

```python
from orchestrator import WorkflowRunner, load_workflow
from orchestrator.provider import StubProvider

wf = load_workflow("clinical-decision-loop")
runner = WorkflowRunner(provider=StubProvider())  # everything else defaults
result = runner.run(wf)

for pr in result.phase_results:
    print(pr.phase.id, pr.persona.key, len(pr.emitted_event_ids), "events")
```

Inject your own persona loader / event sink for tests:

```python
runner = WorkflowRunner(
    provider=my_stub_provider,
    persona_loader=lambda key: my_fake_persona(key),
    event_sink=collected_events.append,
)
```

## Layout

```
orchestrator/
├── __init__.py       # public exports
├── loader.py         # YAML -> Workflow + WorkflowPhase + validation
├── persona.py        # .md -> Persona (wraps body with "stay in character" preamble)
├── provider.py       # built-in StubProvider + get_provider() shim to synthesis
├── runner.py         # WorkflowRunner.run() — phase-by-phase execution
├── cli.py            # list / show / run subcommands
└── tests/
    ├── test_loader.py
    ├── test_persona.py
    └── test_runner.py
```

## Wiring

- **Personas** live under `bots/shared/personas/gtm/<key>.md`. Each
  file's body becomes the LLM system prompt verbatim, wrapped with a
  short preamble that tells the model to stay in character for one
  phase.
- **Workflows** live under `bots/shared/workflows/business/<name>.yaml`.
  The Python validator in `loader.py` mirrors the Node validator at
  `bots/shared/workflows/validate.js` — keep them in sync.
- **Memory events** are written via `memory_system.events.write.append_event`
  using `memory_system.events.new_event`. Each phase emits one event
  per type declared in the workflow's `emits:` list; `ACTION` events
  get `status=open` + `owner=<persona-key>` metadata; `PREDICTION`
  events get a default `confidence=0.5` (a future PR may parse the
  response for explicit confidence).
- **Default provider** is the in-package `StubProvider` — deterministic,
  no API key, no network. Pass `--provider auto|anthropic|openai|gemini`
  on the CLI to delegate to `epic_intelligence.synthesis.get_provider`.

## Backpressure (future)

Workflows declare backpressure criteria — conditions that must hold
before the workflow's recommendation is considered ready to act on.
The current runner returns `backpressure_status="unevaluated"` and
leaves enforcement to the operator. A future PR will run the
criteria as LLM-judged predicates over the accumulated phase outputs
and either gate the final event emission or annotate it.
