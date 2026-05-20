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

## Architecture additions ported from RTRevenue collab-memory

The base Memory-First Protocol (typed events + JSONL + briefing) was
the first piece. The richer architecture from RTRevenue's
collab-memory has now been ported into OPAL's `memory_system/`:

### Scope / namespace primitive (`memory_system/scopes/`)

Two-tier vocabulary: any tag a writer attaches at write-time is
provisional; the canonical taxonomy lives in
`memory_system/ontology/taxonomy.json`. **Scopes** bridge the two —
inferred clusters of related provisional tags with their own
lifecycle (`provisional → active → canonical → deprecated`). Solves
the new-initiative problem: a pilot kickoff that introduces a
project codename + 5-10 internal terms is absorbed in one event
without blocking the writer.

```
memory_system/scopes/
├── models.py        Scope / ScopeMember / ScopeTransition (frozen)
├── identifiers.py   Deterministic scope/transition/rollback id minting
├── transitions.py   State-machine + tier classification table
├── detect.py        Pure burst detector (single-event + windowed)
├── lifecycle.py     Pure promotion / canonicalization / deprecation
├── store.py         SQLite store (3 tables, idempotent schema)
├── auto_detect.py   Hook called from events/cli.py on every accepted write
└── cli.py           python -m memory_system.scopes.cli {list|lifecycle|revert|rebuild}
```

Tiered authority for transitions:

| Tier | Move | Authority |
|---|---|---|
| 0 | Tag application + scope creation | Autonomous, no review |
| 1 | provisional → active | Autonomous, 7-day rollback window |
| 2 | active → canonical, * → deprecated | Autonomous + adversarial review (gated externally) |
| 3 | canonical → active, active → provisional | Operator only |

All Tier-1/Tier-2 transitions carry a deterministic `rollback_id`. One
`memory-scopes revert <rollback_id>` undoes a Tier-1 move by appending
a compensating transition (audit-preserving — nothing is deleted).

### Hybrid retrieval pipeline (`memory_system/retrieval/`)

Composable, pure-functional stages:

```
filter_only      structured filter by type/actor/workflow/tags/dates
hybrid_search    RRF-merge of FTS5 hits + ChromaDB vector hits
scope_expand     pull events sharing a scope membership with hits
window_truncate  enforce token budget; oldest-or-lowest-score dropped first
```

Pipeline is `compose(*stages)`. Each stage is `(StageContext) -> StageContext`.
Backends (FTS5, vectors, scope membership lookup) are injected as
callbacks so the same pipeline runs in tests with in-memory fakes
and in production with the real ChromaDB / SQLite backends.

### Ontology + predicate engine (`memory_system/ontology/`)

`taxonomy.json` is a SKOS-flavoured JSON tree (no rdflib dependency).
`predicates.json` declares proactive pub/sub rules consulted by the
briefing engine on triggers (`session_start`, `pre_query`,
`post_write`). The bundled OPAL ontology covers clinical / hardware /
regulatory / EHR-integration / pilot / fundraising / manufacturing /
IP / strategy concepts; the bundled predicates surface open ACTIONs,
recent DECISIONs, CONTEXT_CHANGEs, clinical-safety touches,
regulatory touches, investor-pitch tracking, and pilot status at every
session start.

### Auto-detection on write

Every accepted event flows through `scopes/auto_detect.py` (called
from `events/cli.py`) which:
  1. Loads canonical tags from the ontology
  2. Loads tags-already-attached-to-existing-scopes from the SQLite store
  3. Runs `detect()` over the new event + recent context
  4. Materializes any candidate scopes into Scope + ScopeMember[] +
     ScopeTransition rows in SQLite
  5. Returns the materializations to the caller for surfacing

Failures are non-fatal — the JSONL log is always the source of truth.

## Adversarial review of Tier-2 transitions (E-1)

Tier-2 transitions (`active -> canonical`, `* -> deprecated`) are
autonomous **but gated by adversarial review**. The reviewer is a
loyal-opposition LLM call: its job is to argue AGAINST the proposal
with specifics from the scope state + recent events. It returns a
structured verdict the gating layer reads to decide what to apply.

### Modules

| File | Role |
|---|---|
| `memory_system/scopes/adversarial.py` | `AdversarialReviewer`, `StubReviewer`, `ReviewRequest`, `ReviewVerdict`, prompt builder, response parser |
| `memory_system/scopes/lifecycle_gating.py` | `gate_tier_2()` runs the reviewer over every Tier-2 proposal; returns `GatingResult(approved, rejected, verdicts)` |

### Output contract

The adversary MUST emit:

```
VERDICT: APPROVED | REJECTED
REASONING: <one to three sentences>
ALTERNATIVE: <one line, or 'none'>
```

A malformed response fails safe to `REJECTED` with a "parse failure"
reasoning. A provider exception fails safe to `REJECTED`. The design
treats silent approval as the worst outcome.

### Two bars (the reviewer's system prompt enforces this)

**Promotion to canonical** — high bar. The canonical vocabulary is
the predicate engine's source of truth; a wrong promotion contaminates
retrieval. Reject when: member tags are drifting, activity is a
single short burst, the scope's name looks like a transient codename,
or adjacent canonical concepts already cover this ground.

**Deprecation** — moderate bar. Deprecation is reversible
(`deprecated -> active` is allowed), but every false deprecation
costs an operator revert. Reject when: silence could be a measurement
gap, a recent CONTEXT_CHANGE suggests dormant-not-dead, or the scope
was just promoted.

### CLI

```bash
# Dry-run with adversarial review (default: stub reviewer; pass
# --adversary-provider anthropic|openai|gemini for the real thing)
python -m memory_system.scopes.cli lifecycle --with-adversarial-review

# Commit only the approved Tier-1 + approved Tier-2 transitions
python -m memory_system.scopes.cli lifecycle \
    --apply --with-adversarial-review --adversary-provider anthropic
```

The legacy `--apply-tier-2` (no review) still exists for emergencies
but is documented as NOT RECOMMENDED. The approved-by-the-adversary
path is the operational default.

### Provider reuse

The adversarial reviewer reuses the pluggable LLM provider from
`epic_intelligence.synthesis.provider` (Anthropic / OpenAI / Gemini /
Stub). No duplicate plumbing. Env overrides:
`OPAL_SYNTHESIS_PROVIDER`, `OPAL_SYNTHESIS_MODEL`.

### Audit trail

`annotate_transition_with_verdict()` re-emits the approved transition
with the adversary's reasoning baked into its `reason` field, and
changes the `actor` to `adversary_rejected` on the rejected path. The
store records the full transition either way, so every Tier-2
decision is reconstructable from the JSONL audit log alone — no
separate verdict store needed.

## Neo4j projection of memory events (E-2)

Every typed event also lands as a graph node + relationships in Neo4j,
giving operators cross-persona / cross-workflow traversal queries that
SQLite + ChromaDB don't naturally support.

### Schema (kept deliberately small)

| Node label | Identity | Purpose |
|---|---|---|
| `:Event` | `.id` (event id) | Primary record per typed event |
| `:Actor` | `.key` | Distinct persona / platform identifier |
| `:Workflow` | `.id` | Distinct workflow id |
| `:Phase` | `.key = "<workflow>:<phase>"` | Distinct workflow phase |
| `:Tag` | `.name` | Distinct tag value |

| Relationship | Direction | Source |
|---|---|---|
| `:BY` | `Event -> Actor` | Every event |
| `:IN_WORKFLOW` | `Event -> Workflow` | Events with a workflow |
| `:IN_PHASE` | `Event -> Phase` | Events with workflow + phase |
| `:TAGGED` | `Event -> Tag` | One per tag |
| `:RELATED_TO` | `Event -> Event` | From event.related |
| `:VERIFIES` | `Event -> Event` | OUTCOME's metadata.verifies |
| `:SUPERSEDES` | `Event -> Event` | metadata.supersedes when set |

All upserts use `MERGE` so re-running against the same event is
idempotent. Constraints + indexes are created once at projector init
via `IF NOT EXISTS`.

### Modules

| File | Role |
|---|---|
| `memory_system/events/neo4j_projection.py` | Pure `build_event_upsert(event) -> [CypherStatement]` + live `Neo4jProjector` class that opens the driver lazily and runs the statements |

### CLI

```bash
# Project every accepted event into Neo4j as well as the JSONL log
python -m memory_system.events.cli write \
    --type DECISION --actor strategist \
    --title "..." --content "..." \
    --neo4j-project

# Replay the entire JSONL log into Neo4j (idempotent)
python -m memory_system.events.cli neo4j-rebuild
```

Env vars (mirror the pattern from `save_session.py`):
`NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`, `NEO4J_DATABASE`
(legacy `KNOWLEDGE_GRAPH_*` aliases also accepted).

### Best-effort + source-of-truth contract

The JSONL log is always the source of truth. A Neo4j outage:
- Logs to stderr but never blocks an event write
- Is recoverable via `neo4j-rebuild` once the DB comes back
- Doesn't affect the ChromaDB projection or the scope auto-detect hook

### Example queries it enables

```cypher
// All DECISIONs Athena made in the past 30 days
MATCH (e:Event {type: 'DECISION'})-[:BY]->(:Actor {key: 'strategist'})
WHERE e.timestamp > '2026-04-16'
RETURN e.title, e.timestamp ORDER BY e.timestamp DESC

// What workflows touched tag 'aurora'?
MATCH (:Tag {name: 'aurora'})<-[:TAGGED]-(:Event)-[:IN_WORKFLOW]->(w:Workflow)
RETURN DISTINCT w.id

// Chain of OUTCOMEs verifying earlier PREDICTIONs
MATCH (o:Event {type: 'OUTCOME'})-[:VERIFIES]->(p:Event {type: 'PREDICTION'})
RETURN p.title AS prediction, o.title AS outcome, p.timestamp, o.timestamp
```

## Open follow-ups (out of scope)

- **Workflow orchestrator integration** — make the bot platform
  automatically append events as workflows execute, instead of
  relying on the operator to do it by hand.
- **DSPy assertions** — validate AI-generated events against the
  schema (e.g., PREDICTION must include a confidence value).
- **Briefing personalization** — filter briefings to the actor or
  department the operator is currently context-switched into.
- **Multi-round adversarial debate** — currently the reviewer is a
  single LLM call. A proposer + critic + judge architecture could
  surface more nuanced disagreements at the cost of additional
  latency + tokens.
- **Graph-aware briefings** — use the Neo4j projection to surface
  "what depends on this scope" or "who was last to act on this
  workflow" in the session-start briefing.

## Test coverage

`memory_system/tests/test_events.py` covers:
- Event construction + validation (happy path + every failure mode)
- Type-specific metadata rules (PREDICTION confidence, ACTION status,
  OUTCOME verifies/related)
- Append-only JSONL idempotency
- Briefing summarization (in-window vs out-of-window, open actions,
  overdue predictions)

Run: `python -m pytest memory_system/tests/ -v`
