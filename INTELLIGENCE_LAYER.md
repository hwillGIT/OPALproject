# The OPAL Intelligence Layer

A plain-English guide to what we've built, why it exists, and what
it lets people do — using Epic (the EHR that runs the hospitals
we're selling into) as the reference system throughout.

If you're new to this repo, read this before any module README. If
you're an engineer looking for code, every section ends with
pointers to where the implementation lives.

---

## 1. What the Intelligence Layer is

The OPAL Intelligence Layer is the software that makes our voice
assistant (LYNA) **useful at the bedside** and our team
(advisors + founders + bots) **coherent across days and weeks**.

In one sentence: **it's the layer that turns Epic's data and Epic's
documentation into answers a nurse can act on in under two seconds,
and turns every conversation our team has into structured memory we
can navigate later.**

It sits between two worlds:

- **Below it:** Epic's EHR (FHIR, CDS Hooks, SMART on FHIR, the
  hospital network), the LYNA voice device, the bot platform, and
  whatever LLM is most appropriate at the moment.
- **Above it:** the clinician asking "what's the latest creatinine
  on bed 14?", the operator deciding whether to pursue a pilot at
  Mt Sinai, the advisory board deciding whether to ship a feature.

The middle is where all the work is.

---

## 2. Why it exists

Three problems we have to solve at the same time:

### 2.1 Epic is enormous, and clinicians can't find what's already there

Epic exposes patient data, write-backs, and decision-support hooks
through several specs, all of them documented somewhere:

- **HL7 FHIR R4** — the data model. Patients, observations,
  medications, encounters.
- **Epic on FHIR** — Epic's flavor of the FHIR API, including the
  resources Epic actually exposes and the quirks of how.
- **CDS Hooks** — the protocol for inserting decision support into
  Epic's workflow (e.g., "patient just opened a chart →
  recommend a bundle").
- **SMART on FHIR** — the OAuth-based auth + app-launch standard
  third-party apps use to live inside Epic.
- **Open Epic** — the public sandbox where developers test all of
  the above without a real hospital.

A nurse who needs an answer doesn't have time to search this
documentation, and the LLM that would answer for her can't be
trusted unless its answer cites a specific Epic doc.

**What the Intelligence Layer does about this:** we crawl every one
of those documentation sites, chunk it, index it, and serve answers
to LYNA — with citations to the exact section of the exact Epic doc.
A clinician's voice query lands a cited, plain-English answer in
under two seconds, no hallucinations and no "let me get back to you."

### 2.2 The team makes a hundred small decisions a week, and forgets them

OPAL is a small startup with a large advisory board. Athena (our
strategist persona) recommends an ICP shift on Tuesday; Diego (our
hardware-lead persona) commits to an ESP32-S3 dev kit order on
Wednesday; Regina (regulatory affairs) flags an FDA concern on
Friday. By next Monday, nobody remembers what was decided.

**What the Intelligence Layer does about this:** every persona
conversation, every workflow run, and every operator note can emit
a typed memory event (DECISION, ACTION, INSIGHT, PREDICTION,
OUTCOME, DEBATE, CONTEXT_CHANGE, ARTIFACT). Those events are the
single source of truth for "what does the team know?" — readable
by humans, queryable by LLMs, projected into a graph for
relationship questions, and surfaced in tomorrow's briefing.

### 2.3 Pilot sales are slow, and we can't afford to chase the wrong sites

Every healthcare pilot has a six-dimensional readiness profile:
clinical fit, integration feasibility, compliance burden,
executive resonance, deal economics, and operator ground-truth.
Founders triage candidate hospitals by gut, which is fast but
inconsistent.

**What the Intelligence Layer does about this:** a deterministic
scoring rubric the operator can fill out per candidate site, plus
structured workflows for the two compliance items that historically
kill timelines (BAA and IRB). Same vocabulary humans and bots use.

---

## 3. The four layers, plainly

Picture four concentric layers, each calling the one below it:

```
┌──────────────────────────────────────────────────────────────┐
│  4.  The team workspace                                       │
│      Mattermost channels, the persona bots, daily briefings,  │
│      operator CLIs, pilot scoring tools                       │
├──────────────────────────────────────────────────────────────┤
│  3.  Orchestrators                                            │
│      Workflow runner (turns YAML into multi-phase             │
│      conversations), briefing engine, BAA / IRB processes     │
├──────────────────────────────────────────────────────────────┤
│  2.  Memory + reasoning                                       │
│      Typed events, scopes, predicates, ontology,              │
│      adversarial review for high-stakes transitions           │
├──────────────────────────────────────────────────────────────┤
│  1.  Knowledge sources                                        │
│      Epic documentation (FHIR, CDS Hooks, SMART, etc.),       │
│      LLM providers, the hospital's live FHIR server           │
└──────────────────────────────────────────────────────────────┘
```

### Layer 1 — Knowledge sources

The "raw material" the rest of the layer reasons over.

- **Scraped Epic docs** — over 8,500 chunks across CDS Hooks,
  Epic on FHIR, HL7 FHIR R4, Open Epic, and SMART app launch.
  Stored in `epic_intelligence/scraper/output/markdown/`. Each
  chunk preserves its source URL so we can cite it.
- **A vector index** — ChromaDB stores embeddings of every chunk
  so a question gets the right paragraphs back. Lives in
  `epic_intelligence/`.
- **LLM provider abstraction** — Anthropic / OpenAI / Gemini /
  built-in stub. The stub is deterministic and has no network
  dependency, so tests and CI never need an API key. Lives in
  `epic_intelligence/synthesis/provider.py`.
- **Live hospital data** — Epic's FHIR endpoints at each pilot
  site. We never store Epic patient data permanently; we read at
  query time using SMART on FHIR auth, then forget.

### Layer 2 — Memory + reasoning

The team's nervous system. Once something is known, it's typed and
findable.

- **Typed events** — every recorded fact is one of eight types
  (DECISION, ACTION, INSIGHT, PREDICTION, OUTCOME, DEBATE,
  CONTEXT_CHANGE, ARTIFACT). Vocabulary intentionally narrow so
  predicates can reason over the log. JSONL is the source of truth;
  ChromaDB and Neo4j are projections (best-effort, can be rebuilt
  from the log). Lives in `memory_system/events/`.
- **Scopes** — auto-detected namespaces. When a burst of events
  shares tags and timing, the system creates a scope (e.g.
  `scope-mt-sinai-pilot-2026-05`) and groups them. Operator can
  promote a scope through a lifecycle (PROPOSED → ACTIVE →
  GOVERNING → ARCHIVED). High-stakes transitions trigger
  adversarial review. Lives in `memory_system/scopes/`.
- **Predicates** — small declarative rules that match events
  (e.g. "find every ACTION still open in the last 14 days"). Used
  by the briefing layer and surfaced on workflow runs so the
  operator sees what patterns the team's emits tripped. Lives in
  `memory_system/ontology/predicates.py`.
- **Adversarial review** — when a scope is promoted to GOVERNING
  (the highest authority tier), a separate "loyal-opposition" LLM
  reviews the transition and can reject it. Fails safe to rejected.
  Lives in `memory_system/scopes/adversarial.py`.

### Layer 3 — Orchestrators

Multi-step processes that turn a question into a coordinated team
conversation.

- **Workflow runner** — given a YAML workflow definition (8 of
  them currently, covering clinical decisions, hardware reviews,
  pilot assessments, investor pitches, regulatory risk, partnership
  qualification, BAA negotiation, IRB submission), runs each phase
  as a separate persona, threads context, and captures the result.
  Personas decide what's memory-worthy and emit typed events
  directly — no glorified logging. Lives in `orchestrator/`.
- **Briefing engine** — summarizes the memory log for any window
  (default: the last day) into a human-readable digest. Open
  actions, overdue predictions, recent context changes, who did
  what. Lives in `memory_system/events/briefing.py`.
- **BAA / IRB workflows** — the two compliance items that
  historically kill pilot timelines, turned into structured
  multi-phase reviews with backpressure gates ("you can't sign
  the BAA until the PHI flow is mapped"). Live in
  `bots/shared/workflows/business/`.

### Layer 4 — The team workspace

Where humans and bots actually meet.

- **Mattermost** — every persona is summonable by `!command` or
  `@mention`. Persona replies that contain memory-worthy moments
  emit structured events the same way the orchestrator does, via
  a fenced YAML block the bot parses and strips before posting.
  Lives in `bots/` (JS); the parser is `bots/shared/memory-emit/`.
- **CLIs** — every layer has an operator CLI. `python -m
  orchestrator.cli run <workflow>`, `python -m pilot.cli score
  <site>`, `python -m memory_system.events.cli briefing-post`,
  etc.
- **Daily briefing → Mattermost** — a cron job (Linux/Mac/Windows
  or inside the bot itself) posts the briefing every morning so
  the team starts the day with "here's what we knew yesterday."

---

## 4. User journeys

The point of the layer is concrete. Five stories.

### Journey 1 — Sarah, a med-surg nurse, at the bedside

It's 2:15 AM. Sarah is on a night shift, four hours into a 12-hour
stretch. Bed 14 just buzzed: the patient is asking for pain meds
and she has no idea when she last had any.

**Without LYNA:** Sarah walks to the nurses' station, logs into
Epic, navigates three tabs, scans the MAR (medication
administration record), and tries to remember whether it's the
post-op order set or the standing PRN. 2-4 minutes. Repeat 12
times a shift.

**With LYNA:** Sarah taps the LYNA badge clipped to her scrubs.

> "What's the last pain med for bed 14?"

In under two seconds:

> "Mrs. Reynolds in bed 14 last had hydromorphone 0.5 mg IV at
> 11:43 PM — about 2.5 hours ago. Her PRN order allows q3h. She's
> due in 30 minutes per the order; sooner is a call to the resident.
> Source: Epic MAR pulled via FHIR Observation."

She walks back to the room knowing exactly what to do.

**Under the hood:**

1. LYNA captures audio, transcribes locally (Phi-3 SLM on the
   hospital premises, no PHI in the cloud).
2. The transcript hits the Intelligence Layer's query router.
3. The router recognizes "last pain med for bed 14" as a live-data
   query, calls Epic's FHIR `MedicationAdministration` endpoint via
   SMART on FHIR with Sarah's scoped auth.
4. The Intelligence Layer also consults the indexed Epic docs to
   format the answer with the right citation (so Sarah knows where
   it came from).
5. The reply is rendered back through LYNA's voice channel.

**Where in the code:**

- Live FHIR pull: `epic_intelligence/assistant/voice_router_stub.py`
  (real Epic adapter is downstream of the synthesis layer).
- Doc citations: `epic_intelligence/query.py` against the indexed
  corpus in `epic_intelligence/scraper/output/markdown/`.
- Synthesis: `epic_intelligence/synthesis/synthesizer.py`.

### Journey 2 — Dr. Mendez, CMIO, evaluating LYNA on a Tuesday afternoon

Dr. Mendez is the Chief Medical Information Officer at a 600-bed
academic medical center. He's meeting with Ruth and Hubert at 2 PM.
He has 45 minutes and three competing vendors on his calendar this
week.

He asks: *"How does LYNA integrate with our Epic build? We're on
the May 2023 release; we run CDS Hooks; we're allergic to vendors
who can't tell us exactly which FHIR endpoints they hit."*

Hubert opens his laptop and types:

```
python -m pilot.cli score pilot/sites/mendez-amc.yaml
```

In under a second, the Intelligence Layer prints:

```
# Mendez AMC: HOLD (62.4/100)
Worth pursuing — fix the named gaps before signing.
Top gaps: CMO alignment confirmed; specific C-suite metric not yet
mapped; champion candidate scores 71/100 (good but evidence trail
is thin).

## Dimension breakdown
  [integration_feasibility]  raw=100/100  weighted=20.0
    + Epic May 2023 is supported by our integration.
    + FHIR resources we need are live + reachable.
    + Device provisioning path (wifi/MDM/segmentation) is mapped.
...
```

Hubert turns the laptop toward Dr. Mendez. *"Here's what we know
about your build. Here are the FHIR endpoints we hit. Here's the
device path. Here's the named gap — your nursing-vacancy metric
isn't mapped to anything LYNA moves, and that's the thing your CFO
will ask about."*

Dr. Mendez doesn't need to wait six weeks for a written assessment.
He spends the rest of the meeting on the actual problem (the
unmapped CFO metric), and they're 30 minutes ahead of where they
would have been.

**Under the hood:**

1. The rubric (`pilot/`) is pure Python — no LLM call, no network.
   It scores six dimensions against the operator's site YAML and
   reports the verdict.
2. Each dimension's rationale and gaps are surfaced so Dr. Mendez
   can argue with the score rather than accept it as a black box.
3. After the meeting, Hubert emits a memory event:

```bash
python -m memory_system.events.cli write \
  --type INSIGHT --actor founder \
  --title "Mendez AMC nursing-vacancy metric gap" \
  --content "..." --tags pilot,mendez-amc,c-suite-metric
```

That event lands in tomorrow's briefing.

**Where in the code:**

- Scoring: `pilot/scoring.py`, `pilot/champion.py`.
- Site templates: `pilot/examples/`.
- Memory write: `memory_system/events/write.py`.

### Journey 3 — Ruth runs the BAA workflow with St. Vincent's legal team

St. Vincent's said yes to a pilot. Their general counsel sent over
a 14-page BAA template Tuesday. Ruth has done this twice before;
both times it took six weeks she didn't have.

She types:

```
python -m orchestrator.cli run baa-negotiation \
  --provider anthropic \
  --context "Site: St. Vincent's; PHI surface: read Patient, MedicationRequest, Observation; write Communication; no at-rest storage on our side"
```

The orchestrator walks the personas through six phases:

1. **scope-the-phi** — Helena (enterprise architect) and Cyrus
   (security architect) map the exact PHI surface together. The
   tension Helena↔Cyrus produces the right answer: Helena wants
   the broadest possible integration; Cyrus wants the narrowest
   possible PHI exposure. The agreed scope lands as an INSIGHT.
2. **read-their-template** — Suki (compliance) classifies every
   clause in the BAA Ruth got: standard HHS-sample / customized /
   cross-referenced.
3. **identify-friction** — Suki, Cyrus, and Helena (tension
   Suki↔Cyrus surfaces "contract language vs threat model")
   produce a red-line table with proposed text + rationale.
4. **counterparty-position** — Suki and Wei (partnership lead)
   name the signer, the negotiator, and the institution's
   documented BAA SLA.
5. **timeline-and-blockers** — dated critical path with named
   blockers and escalation triggers.
6. **sign-or-walk** — dialectic debate between Suki and Wei
   (Suki↔Wei: "close timeline vs relationship"). Output is a
   DECISION recorded as a memory event.

Each phase produces a section in
[`pilot/templates/baa-checklist.md`](pilot/templates/baa-checklist.md)
that Ruth hands to St. Vincent's counsel. Each persona emits a
typed event the briefing surfaces.

Two days later, when Ruth meets with St. Vincent's counsel, she
walks in with the red-line, the rationale for every change, the
expected timeline, and a memory of every decision the team made
about it. The meeting is 30 minutes, not three hours.

**Under the hood:**

1. `orchestrator.cli run baa-negotiation` loads
   [`bots/shared/workflows/business/baa-negotiation.yaml`](bots/shared/workflows/business/baa-negotiation.yaml).
2. For each phase, the orchestrator loads the lead persona's
   system prompt, prepends the **memory-emit protocol** preamble
   (the persona is taught that it — not a classifier — decides
   what's memory-worthy), builds a prompt that includes the
   tensions explicitly, and calls the LLM.
3. The persona's reply may contain a fenced `memory-emit` YAML
   block. The orchestrator parses it, validates it, and appends
   typed events. Out-of-vocab types are demoted to CONTEXT_CHANGE
   with the original type preserved.
4. Post-write predicates fire on each emit ("this ACTION is open
   — surfaces in next briefing"; "this CONTEXT_CHANGE — broader
   scope likely needs re-evaluation").

**Where in the code:**

- Workflow YAML: `bots/shared/workflows/business/baa-negotiation.yaml`.
- Workflow runner: `orchestrator/runner.py`.
- Emit parser: `orchestrator/emit_parser.py`.
- Persona preamble: `orchestrator/persona.py:_PREAMBLE`.
- Operator checklist: `pilot/templates/baa-checklist.md`.

### Journey 4 — The OPAL team's daily briefing

It's 9 AM Eastern, Monday. Hubert opens Mattermost. The first post
in `#town-square` is from Briefing Bot:

```
# Briefing — window 2026-05-15T00:00 → 2026-05-16T09:00
  47 events in window; 9 distinct actors

## Open actions (6)
  - [open] Order 10 ESP32-S3 dev boards by Friday
    (owner: hardware-lead; id: evt-9f3a4b...)
  - [in-progress] Schedule call with Mt Sinai Innovation Program lead
    (owner: founder; id: evt-c7d1e9...)
  - [open] Draft IRB protocol skeleton for St. Vincent's pilot
    (owner: regulatory-affairs; id: evt-aa2b88...)
  ...

## Overdue predictions (1)
  - [conf=0.7] Device case will fit in standard scrubs pocket
    (horizon: 2026-05-10; id: evt-44dd...)

## Recent CONTEXT_CHANGE (2)
  - Mt Sinai Innovation Program announced new spring cohort
    (actor: founder; id: evt-1e2f3a...)
  - Epic announced FHIR R5 GA for 2027 — likely no impact pre-pilot
    (actor: enterprise-architect; id: evt-7c8d9e...)

## Counts by type (in window)
  ACTION: 12
  DECISION: 8
  INSIGHT: 14
  PREDICTION: 5
  CONTEXT_CHANGE: 2
  ARTIFACT: 6

## Activity by actor
  strategist: 9
  product-owner: 8
  regulatory-affairs: 7
  hardware-lead: 6
  ...
```

Hubert reads it in two minutes. He now knows what's open, what's
late, what shifted. The team starts the week aligned without a
meeting.

**Under the hood:**

1. A cron job runs `python -m memory_system.events.cli
   briefing-post --lookback-days 1`.
2. That command reads yesterday's JSONL log, runs the briefing
   engine to summarize, then POSTs the markdown to a Mattermost
   incoming webhook configured in env.
3. Chunks longer than ~15k chars are split on blank-line
   boundaries so a busy week's briefing arrives in order across
   multiple posts with `_(continued N/M)_` prefixes.

**Where in the code:**

- Briefing render: `memory_system/events/briefing.py`.
- Mattermost POST: `memory_system/events/mattermost_post.py`.
- CLI + cron docs: `memory_system/events/BRIEFING_POST.md`.

### Journey 5 — Athena and Diego disagree on Tuesday afternoon

Hubert, prepping for a board meeting, asks Athena (the strategist
persona, summoned via `!strategist` in Mattermost):

> *"Should we lead the seed pitch with the hardware moat or the
> data moat?"*

Athena replies in character, with reasoning. At the end of her
reply, she appends:

````
```memory-emit
- type: DECISION
  title: Lead seed pitch with data moat (operational KB), hardware as proof
  content: |
    The operational knowledge base is uniquely defensible — door
    codes, pager numbers, prep checklists — and compounds with
    every pilot. Hardware is necessary but not sufficient as a
    moat; Vocera proved it commoditizes.
  confidence: 0.75
  tags: [seed-pitch, positioning, moat]
- type: ACTION
  title: Re-order pitch deck pages 4-7 to put operational KB first
  related: [evt-prior-pitch-draft-id]
```
````

The Mattermost bot **strips the fenced block** before posting
Athena's reply to the channel (Hubert sees a clean answer, no YAML
noise). The block itself becomes two memory events: a DECISION
with confidence 0.75, and an ACTION with the pitch-deck reorder
auto-assigned to Athena.

Diego (hardware lead) sees the post in `#strategy` and disagrees.
Hubert summons him: `!hardware`. Diego argues, in character, for
hardware-first positioning. At the end of *his* reply:

````
```memory-emit
- type: DEBATE
  title: Hardware vs data moat — opposing case
  content: |
    Operational KB is replicable; the badge form factor isn't.
    Vocera commoditized because they stopped iterating on the
    badge. Our differentiator is the device, period.
  related: [evt-athena-decision-id]
  tags: [seed-pitch, positioning, hardware]
```
````

Now the memory log has a DECISION, an ACTION, and a DEBATE
explicitly linked. Tomorrow's briefing surfaces all three. The
predicate `matches-context-change` fires because a DEBATE on the
same topic as an existing DECISION is a signal that scope likely
needs re-evaluation.

Three weeks later, when Hubert is reviewing the pitch deck before
the board meeting, he searches the memory log for `seed-pitch`
events. The DECISION, the ACTION, the DEBATE, and any subsequent
OUTCOME are all there, linked, with timestamps and reasoning. He
doesn't have to remember; the system did.

**Under the hood:**

1. The bot's system prompt teaches every persona the
   memory-emit protocol (the same one the orchestrator uses).
2. The JS-side parser (`bots/shared/memory-emit/parser.js`)
   extracts the fenced block, validates each entry against the
   schema, strips the block from the human-visible message, and
   feeds each entry to `bots/shared/institutional-memory/`.
3. The Python side (workflow runs) and the JS side (live bot
   chat) both produce the same shape of event — contract-compatible
   parsers on both sides.

**Where in the code:**

- JS parser: `bots/shared/memory-emit/parser.js`.
- Protocol preamble (JS): `bots/shared/memory-emit/preamble.js`.
- Bot wiring: `bots/gtm/index.js` (look for `emitParsedToMemory`).
- Python equivalents: `orchestrator/emit_parser.py`,
  `orchestrator/persona.py:_PREAMBLE`.

---

## 5. The trust model — why anyone should believe a word the system says

Three discipline choices we've made deliberately:

### 5.1 Every clinical answer cites Epic's own documentation

LYNA never says "I think the FHIR endpoint is..." — it says
"per Epic on FHIR §3.2 Patient Resource, the endpoint is...",
with the URL. The chunker that indexes the docs preserves source
URL per chunk; the synthesizer is forbidden from generating a
claim without a backing citation.

If a question can't be answered from the indexed docs, the answer
is "I don't have that documented; check with Epic implementation
support." We chose to be silent over wrong.

### 5.2 Memory is what the persona deliberately emits — not what a classifier guesses

An earlier version of the bot ran a regex over every response
("if the reply contains 'recommend' or 'we should', emit it as an
INSIGHT"). That produces glorified logging — every long response
becomes an event, the briefing fills with noise, and the team
stops reading.

The current discipline: the persona itself decides what's
memory-worthy. If a reply contains nothing significant, **zero
events are emitted**. That's the right answer for routine prose.
Predicates over the (sparse, intentional) memory log surface
patterns at read time — they don't try to make every line
significant at write time.

### 5.3 High-stakes promotions require a separate "loyal opposition" review

A "scope" can be promoted through a lifecycle from PROPOSED →
ACTIVE → GOVERNING. GOVERNING means the scope's contents are
treated as authoritative for future decisions — a high bar.

Any Tier-2 promotion triggers an adversarial review: a separate
LLM is asked to argue *against* the promotion. If it produces a
substantive objection (not just "lgtm"), the promotion fails.
Provider exceptions, malformed responses, missing scopes — all
fail safe to rejected. The system would rather refuse than
mistakenly authorize.

---

## 6. Where this is going

In sequence, what the layer enables that we haven't built yet:

- **Backpressure evaluation.** Workflows declare backpressure
  criteria today (e.g. "Lead clinician persona has said 'I would
  not slow my workflow to use this'"). The orchestrator currently
  records them but doesn't evaluate. A future PR runs them as
  LLM-judged predicates over the accumulated phase outputs and
  gates the final emission.
- **Multi-persona conversation patterns.** The workflows reference
  patterns like `dialectic-debate` and `single-lead`; today the
  runner only invokes the lead persona. Real debate (two personas
  taking turns) is next.
- **Cross-language unified event store.** Today the JS bots write
  to `bots/shared/institutional-memory/` and the Python
  orchestrator writes to `memory_system/events/log/`. Unifying is
  a small piece but needs a shared id scheme and a decision about
  JSONL ownership.
- **Briefing → predicate enrichment.** The briefing reads JSONL
  directly today. Wiring the post-write predicate matches into
  the briefing ("phase X tripped predicate Y") is a follow-up.
- **Gap-surfacing predictive predicates** (ACTION still open
  after 30 days, PREDICTION with no OUTCOME after 90 days).
  Needs a small `older_than_days` enhancement to the predicate
  engine.

---

## 7. For developers — where to start reading

| If you want to understand... | Read these, in order |
|---|---|
| The Intelligence Layer end-to-end | This doc, then `AI-CONTEXT.md` |
| How a clinical query becomes a cited answer | `epic_intelligence/README.md` → `epic_intelligence/synthesis/synthesizer.py` → `epic_intelligence/query.py` |
| How a workflow becomes a multi-phase conversation | `orchestrator/README.md` → `orchestrator/runner.py` → `bots/shared/workflows/business/clinical-decision-loop.yaml` |
| How a persona reply becomes a memory event | `orchestrator/persona.py` (preamble) → `orchestrator/emit_parser.py` → `memory_system/events/schema.py` |
| How the daily briefing is built | `memory_system/PROTOCOL.md` → `memory_system/events/briefing.py` → `memory_system/events/mattermost_post.py` |
| How a pilot site gets scored | `pilot/README.md` → `pilot/scoring.py` → `pilot/examples/strong-fit.yaml` |
| How BAA and IRB are run as workflows | `bots/shared/workflows/business/baa-negotiation.yaml` + `pilot/templates/baa-checklist.md`; same shape for IRB |
| The persona roster + productive tensions | `bots/shared/personas/DEPARTMENTS.md` + `bots/shared/personas/TENSIONS.md` |

Every module under `memory_system/`, `epic_intelligence/`,
`orchestrator/`, `pilot/`, and `bots/` has its own README that
goes deeper. This doc is the index.
