# orchestrator — workflow runtime (A-1)

Turns the declarative YAML workflows in
`bots/shared/workflows/business/*.yaml` into executable conversation
flows. For each workflow phase the runtime:

1. Loads the lead persona's system prompt from
   `bots/shared/personas/gtm/<key>.md` and wraps it with a preamble
   that teaches the persona the **memory-emit protocol** (see below)
2. Builds the per-phase user prompt from the YAML (questions +
   accumulated context + tension framing)
3. Calls the LLM provider (built-in stub by default — no API keys
   needed; pass `--provider auto|anthropic|openai|gemini` for real
   models via the synthesis layer)
4. Parses any `memory-emit` blocks the persona authored, validates
   each against the phase's emit vocabulary, and appends typed
   memory events — **with no events when the persona judged nothing
   memory-worthy** (no glorified logging)
5. Runs `post_write` predicates over the just-emitted events and
   surfaces matched patterns on the phase result

After all phases it returns a `WorkflowResult` with per-phase
responses, emitted event ids, tripped predicates, and a backpressure
status (informational for now — backpressure evaluation is future).

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

## Memory-emit protocol (A-2)

The persona — not an external classifier — decides when something it
just said is worth recording in shared memory. When the answer is
"yes," it appends a fenced YAML block at the end of its reply:

````
Here's my call. We'll go with the ESP32-S3; the BLE coexistence story
on the nRF beats the raw MIPS we get from the S3, but the developer
ecosystem and our team's existing fluency tilt it.

```memory-emit
- type: DECISION
  title: ESP32-S3 over nRF5340 for the prototype rig
  confidence: 0.8
  related: [evt-9f3a4b...]
  tags: [esp32, hardware]
- type: ACTION
  title: Order 10 ESP32-S3 dev boards by Friday
```
````

The runner strips the fenced block out of the user-visible reply,
parses each entry, and:

- **Vocabulary check** — if the persona emits a type not in the
  workflow's `emits:` allowlist, the event is demoted to
  `CONTEXT_CHANGE` with `metadata.original_type` recording what the
  persona intended.
- **Schema check** — `PREDICTION` must carry `confidence` in `[0,1]`;
  every entry needs `type` + `title`. Malformed entries are recorded
  as `CONTEXT_CHANGE` events with the raw block + the failure reason
  so the persona's intent isn't lost.
- **Field forwarding** — `confidence`, `related`, persona-supplied
  `tags`, and any free-form `content` flow into the resulting event.
  The runner only adds defaults for fields the persona omitted
  (`ACTION` gets `status=open` + `owner=<persona-key>`).

If the persona's reply has **no** emit block, **zero events are
written**. That is the correct answer for routine prose. Auto-classifying
every reply would just be glorified logging — the consumers
(briefing, predicates, retrieval) are the ones who infer meaning.

## Predicates

`memory_system/ontology/predicates.json` declares filter predicates
the runner evaluates with the `post_write` trigger after each phase's
emits land. Matched predicates surface on
`PhaseResult.triggered_predicates` so downstream consumers know what
patterns the new events tripped (e.g. `matches-open-action`,
`matches-prediction`). Inject `predicates=[]` to disable.

## Layout

```
orchestrator/
├── __init__.py       # public exports
├── loader.py         # YAML -> Workflow + WorkflowPhase + validation
├── persona.py        # .md -> Persona; preamble teaches memory-emit protocol
├── emit_parser.py    # extract + validate persona-authored memory-emit blocks
├── provider.py       # built-in StubProvider + get_provider() shim to synthesis
├── runner.py         # WorkflowRunner.run() — phase-by-phase execution
├── cli.py            # list / show / run subcommands
└── tests/
    ├── test_loader.py
    ├── test_persona.py
    ├── test_emit_parser.py
    └── test_runner.py
```

## Wiring

- **Personas** live under `bots/shared/personas/gtm/<key>.md`. The
  file's body becomes the LLM system prompt verbatim, wrapped with a
  short preamble that includes the memory-emit protocol.
- **Workflows** live under `bots/shared/workflows/business/<name>.yaml`.
  The Python validator in `loader.py` mirrors the Node validator at
  `bots/shared/workflows/validate.js` — keep them in sync.
- **Memory events** are written via `memory_system.events.write.append_event`
  using `memory_system.events.new_event`. The workflow's `emits:` list
  is a **vocabulary whitelist**, not a "always emit one of each"
  mechanical rule.
- **Predicates** are loaded from `memory_system/ontology/predicates.json`
  via `memory_system.ontology.predicates.load_predicates`; the runner
  evaluates `post_write` triggers after each phase's emits land.
- **Default provider** is the in-package `StubProvider` — deterministic,
  no API key, no network. The stub authors no emit blocks; use
  `--provider auto|anthropic|openai|gemini` to delegate to the real
  synthesis layer where the persona's judgment about significance
  actually matters.

## Backpressure (future)

Workflows declare backpressure criteria — conditions that must hold
before the workflow's recommendation is considered ready to act on.
The current runner returns `backpressure_status="unevaluated"` and
leaves enforcement to the operator. A future PR will run the
criteria as LLM-judged predicates over the accumulated phase outputs
and either gate the final event emission or annotate it.
