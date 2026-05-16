# Memory-First Protocol

> "Don't reconstruct what you can retrieve. Save your reasoning for
> what's actually hard."

The Memory-First Protocol is OPAL's discipline for capturing typed,
retrievable events as personas + the operator work — so future sessions
start from "here's what we already know" instead of re-deriving it.

Adapted from the RTRevenue Memory-First Protocol pattern, kept
compatible with the existing OPAL memory infrastructure
(`save_session.py` / `recall_context.py` and the ChromaDB + Neo4j
backends already wired in).

---

## The 25/75 Rule

| Phase | Allocation | What |
|---|---|---|
| **Memory lookup** | ~25% of session time | Retrieve briefings + prior decisions before reasoning |
| **Novel reasoning** | ~75% of session time | Solve what's genuinely new |

If a session spends more than half its time re-deriving things the team
already knew, that's a protocol failure, not "thorough work."

## Event vocabulary

Eight types. Every write picks exactly one. Keep this list in sync with
`bots/shared/workflows/validate.js` (`MEMORY_EVENT_TYPES`).

| Type | When to emit | Required metadata |
|---|---|---|
| `DECISION` | A choice was made among options; record the chooser, the options weighed, and the rationale | none beyond title/content |
| `ACTION` | A task was taken or assigned | `status` ∈ {open, in-progress, completed, cancelled}; optionally `owner`, `due` |
| `INSIGHT` | A non-obvious pattern, finding, or fact worth retaining | none |
| `PREDICTION` | A falsifiable forecast | `confidence` ∈ [0.0, 1.0]; optionally `horizon` (ISO-8601 deadline) |
| `OUTCOME` | Observed reality against a prior PREDICTION or ACTION | `verifies` (a prior event id) OR a non-empty `related` list |
| `DEBATE` | Multi-position discussion captured for future reference | none |
| `CONTEXT_CHANGE` | Environment shift (market, regulatory, org, scope) that may invalidate prior decisions | none |
| `ARTIFACT` | A concrete deliverable produced (spec, deck, model, diagram) | optionally `uri` pointing to the artifact |

Schema enforced by `memory_system/events/schema.py`.

## Where it lives

### Source of truth
```
memory_system/events/log/YYYY-MM-DD.jsonl
```
Append-only daily JSONL files. Each line is one validated event.
Idempotent on event id. Survives ChromaDB/Neo4j outages.

### Derived indexes
- **ChromaDB collection** `opal_memory_events` — semantic queries.
  Rebuildable from the log via `cli.py rebuild`.
- (Future) **Neo4j projection** — relationship traversal, persona
  centrality, workflow throughput. Not in this PR.

### Existing memory_system files
`save_session.py` and `recall_context.py` are **not modified by this
PR.** They continue to serve free-form session-summary use. The
typed-events layer adds on top.

## Write surface

### Command line
```bash
python -m memory_system.events.cli write \
  --type DECISION --actor strategist \
  --workflow investor-pitch-review --phase strategic-logic \
  --title "Lead with the platform thesis" \
  --content "We chose the platform thesis over the device thesis because..." \
  --tags pitch,strategy
```

### Python (from bots, orchestrators, scripts)
```python
from memory_system.events import new_event
from memory_system.events.write import append_event, project_to_chroma

ev = new_event(
    type="ACTION",
    actor="product-owner",
    workflow="hardware-build-review",
    phase="synthesis",
    title="Spec a fallback wake-word for noisy wards",
    content="Per Reliability Engineer's failure-mode scan...",
    tags=["hardware", "audio"],
    metadata={"owner": "hardware-lead", "status": "open",
              "due": "2026-06-01"},
)
append_event(ev)
project_to_chroma(ev)  # best-effort; safe if ChromaDB unreachable
```

## Read surface

### Session-start briefing
```bash
python -m memory_system.events.cli briefing --lookback-days 14
```

The briefing always answers four questions, in order:

1. **Open actions** — every ACTION event with status ∈ {open, in-progress}, regardless of age.
2. **Overdue predictions** — every PREDICTION whose `metadata.horizon` is past AND not marked `resolved`. Reminds you to write the OUTCOME.
3. **Recent CONTEXT_CHANGEs** — environmental shifts that may have moved the goalposts since you last looked.
4. **Recent OUTCOMEs** — what actually happened relative to PREDICTIONs / ACTIONs.

Then per-type counts and per-actor activity for the window.

## Workflow integration

Each business workflow in `bots/shared/workflows/business/` declares
its `emits:` list. The orchestrator that runs a workflow is expected
to append at least one event of each declared type by the end of the
workflow. The workflow validator enforces that `emits:` references are
in the protocol vocabulary; runtime enforcement (did the workflow
actually emit?) lives in the orchestrator (next PR).

Example mapping (from `clinical-decision-loop.yaml`):

```yaml
emits:
  - DECISION   # final ship/defer/reject call
  - INSIGHT    # bedside observations worth retaining
  - ARTIFACT   # the versioned spec produced
  - ACTION     # follow-ups assigned to named owners
```

## When to emit (and when NOT to)

**Emit when:**
- A choice has been made that future sessions should not relitigate (DECISION)
- A non-obvious observation has been reached (INSIGHT)
- A measurable bet has been placed (PREDICTION)
- A deliverable has been produced (ARTIFACT)
- Something measurable has happened against a prior bet (OUTCOME)
- The environment has shifted in a way that affects current plans (CONTEXT_CHANGE)
- An owner has accepted a task (ACTION)
- A multi-position discussion was had and the dissent is worth preserving (DEBATE)

**Do NOT emit when:**
- You're "thinking out loud" mid-phase (wait for synthesis)
- The decision is reversible and not yet committed
- The fact is already retrievable from another source (ChromaDB doc, git history, an artifact)
- You'd be writing a duplicate of an existing event id

## Open follow-ups (out of scope for this PR)

- **Neo4j projection** — emit memory events as graph nodes/edges for
  cross-persona traversal queries.
- **Workflow orchestrator integration** — make the bot platform
  automatically append events as workflows execute, instead of
  relying on the operator to do it by hand.
- **Briefing personalization** — filter briefings to the actor or
  department the operator is currently context-switched into.
- **DSPy assertions** — validate that AI-generated events comply with
  the schema (e.g., PREDICTION must include a confidence value).

## Test coverage

`memory_system/tests/test_events.py` covers:
- Event construction + validation (happy path + every failure mode)
- Type-specific metadata rules (PREDICTION confidence, ACTION status,
  OUTCOME verifies/related)
- Append-only JSONL idempotency
- Briefing summarization (in-window vs out-of-window, open actions,
  overdue predictions)

Run: `python -m pytest memory_system/tests/ -v`
