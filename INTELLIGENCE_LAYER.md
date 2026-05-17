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
assistant (LYNA) **useful at the bedside**. It is what turns Epic's
patient data and Epic's published documentation into spoken answers
a nurse can act on in under two seconds — cited, accurate, and
delivered without leaving the room.

It sits between two worlds:

- **Below it:** Epic's EHR (FHIR, CDS Hooks, SMART on FHIR, the
  hospital network), the per-site Operational Knowledge Base (door
  codes, supply locations, on-call rosters, prep checklists), the
  LYNA voice device, and whichever AI model is most appropriate for
  the question.
- **Above it:** a clinician asking "what's the last pain med for
  bed 14?", a float nurse asking "where are the sterile dressings
  on this unit?", a charge nurse asking "give me a unit status for
  handoff."

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

The intended users of LYNA are **clinical and medical staff at the
hospitals that have bought it** — nurses on the floor, charge nurses
running a unit, the wider clinical team during a shift. They never
see the orchestrator, the memory log, or any of the engineering
machinery; they talk to LYNA and LYNA answers. The Intelligence Layer
is invisible plumbing that makes those answers fast, accurate, and
cited — sub-two-second voice replies grounded in the hospital's own
Epic instance and in published Epic documentation.

Three stories from the floor. All three are nurses, because LYNA is
positioned for nurses specifically — "Information OUT for nurses,"
distinct from physician-documentation tools like Suki or Abridge.

### 4.1 — Sarah, a med-surg nurse, at the bedside

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

### 4.2 — Linh, a float nurse, on her first shift on 4-South

Linh is a float-pool RN who was assigned to 4-South tonight because
the regular staff is short. She has never worked this unit before.
In the first 30 minutes of her shift she needs to know: where the
sterile dressings are, what the door code is for the medication
room, who the charge nurse is tonight, and which of the unit's
attendings is on call.

**Without LYNA:** Linh hunts for the charge nurse three separate
times in 30 minutes, interrupts two other RNs to ask where supplies
are, and asks Sarah for the med-room door code (which Sarah has to
look up because she only knows her own units). Roughly 15 minutes
of every float nurse's first shift evaporate this way.

**With LYNA:**

> "Where are the sterile dressing supplies on this unit?"
>
> "On 4-South, sterile dressings are in the clean utility room
> across from bed 12 — second cabinet from the left, second shelf.
> Sizes 4x4 and 2x2 are stocked; if you need larger, the supply
> room on 4-North has them."

A minute later:

> "What's the med-room door code?"
>
> "4-South medication room: 2-4-1-3-#. Code rotates monthly; this
> one is good through 2026-05-31."

A minute after that:

> "Who's the charge nurse tonight?"
>
> "Tonight's charge on 4-South is Devon Park. Devon is on the unit
> until 7 AM. To page Devon: hospital pager 4471, or say 'page
> Devon Park' and I'll send."

By the time Linh's first patient call light goes off, she knows the
unit well enough to work without flagging anyone down.

**Under the hood:**

1. None of these queries touch Epic or any PHI. They hit the
   **Operational Knowledge Base** — the institutional layer of door
   codes, supply locations, pager numbers, prep checklists, and
   unit-specific procedures that every hospital has but almost
   none of them have searchable.
2. The Operational KB is the single most defensible piece of LYNA's
   data position. Every pilot site contributes its own KB; that
   KB compounds with every nurse-shift of usage and is the reason
   a float nurse onboards in minutes instead of hours.
3. The "page Devon Park" command would route through the **execution
   layer** — LYNA can not only retrieve but act (send pages, place
   calls, broadcast to teams) once the operator has confirmed the
   action.

**Where in the code:**

- Operational KB lookup is upstream of the LYNA Intelligence Layer
  (per-site data store). The Intelligence Layer's role here is the
  query router that recognizes "where is X?" and "who is on call?"
  as Operational KB queries (vs. Epic FHIR queries vs. Epic doc
  queries) and dispatches accordingly.
- Query router: `epic_intelligence/assistant/voice_router_stub.py`
  (the production router lives downstream and consumes the same
  contract).
- Execution layer (page / call / broadcast): not yet implemented —
  documented as a v2 capability in the LYNA product brief.

### 4.3 — Marcus, charge nurse on 4-South, end of shift handoff

It's 6:45 AM. Marcus has been charge on 4-South for the 7p-7a
shift. In 15 minutes he hands off to the day-shift charge, Anita.
He needs to compile a unit-status summary: which patients have open
issues, who's NPO for AM procedures, who's pending discharge, and
whether any beds are free for the ED to admit into.

**Without LYNA:** Marcus opens Epic, scans every chart on the unit
(28 patients tonight), writes notes on a paper sheet, doublechecks
the surgical schedule for who's NPO, and asks two of his RNs about
incidents he might have missed. 20-25 minutes.

**With LYNA:**

> "Give me a unit status for 4-South for handoff."

In about 8 seconds:

> "4-South, 28/32 beds occupied, 4 free for ED admits.
>
> **Open clinical issues:**
> - Bed 4 (Cruz, J.) — pain not controlled on current regimen; PRN
>   used 4 times overnight, last at 04:20. Pain service consulted,
>   note pending.
> - Bed 18 (Patel, A.) — temp spike to 38.9°C at 02:15; blood
>   cultures drawn; on q4h vitals; covered with broad-spectrum.
> - Bed 22 (Williams, R.) — fall earlier this shift; per protocol,
>   incident report filed, family notified, neuro checks q1h.
>
> **AM procedures (NPO since midnight):**
> - Bed 7 (Garcia, M.) — colonoscopy at 08:00, GI prep complete.
> - Bed 19 (Chen, K.) — cardiac cath at 09:30, consent obtained.
>
> **Pending discharge today:**
> - Bed 11 (Roberts, T.) — awaiting transport; ride confirmed for
>   11:00.
> - Bed 25 (Liu, S.) — pending PT clearance, expected mid-afternoon.
>
> **Pending admits:** ED holding 1 patient (chest pain rule-out)
> for bed 4 once Cruz is repositioned to a quieter room.
>
> Citations: all data pulled from Epic at 06:42 AM; supply / bed-
> availability cross-checked against unit board."

Marcus reads it once, edits one line (Garcia's prep is actually
incomplete — the bowel-prep nurse called out), and hands it to
Anita as the foundation for the handoff. The handoff itself goes
from 20 minutes to 6.

**Under the hood:**

1. LYNA fires parallel FHIR queries against Epic for every patient
   on the unit: `Encounter` (active), `Observation` (vitals + labs
   in the last 12h), `MedicationAdministration` (PRN usage),
   `Procedure` (scheduled), `DiagnosticReport` (incidents).
2. Results are deduplicated, grouped by patient, and templated into
   a charge-nurse handoff shape. The Intelligence Layer applies the
   institution's handoff conventions (some sites use I-PASS, others
   SBAR, others a local template) from the Operational KB.
3. Free-bed count cross-references the unit's census board (also
   in the Operational KB) so the number reflects reality, not just
   Epic's discharge timestamps.
4. Every section carries a source so Anita knows what came from
   Epic vs. the unit board vs. Marcus's own notes.

**Where in the code:**

- Parallel FHIR fan-out + templating: downstream of the
  Intelligence Layer's query router; the Layer's contract with the
  EHR adapter is a single "unit-status for {unit}" request that
  returns the structured shape above.
- Handoff template selection (per-site I-PASS / SBAR / local):
  driven by Operational KB metadata, the same per-site data that
  Linh's queries hit in §4.2.
- Citation strategy: same as Sarah's bedside query in §4.1 — every
  fact carries its source, never narrate a claim without a
  citation.

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
