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

Ten stories from the floor, spanning the day-to-day shape of
nursing work: a routine bedside lookup, onboarding to an unfamiliar
unit, a charge-nurse handoff during the resource-nurse-offline
window, taking over a patient assignment at start of shift, a new
graduate looking up policy at the bedside, a nurse finding an AI
tool the hospital has been paying for that nobody on the floor
knew was there, a step-down rapid response, a hands-free broadcast
from an isolation room, a clean handoff to the phone for a
camera-dependent task, and an ad-hoc bedside interpreter session
at 03:00 when the certified-interpreter queue is full. All ten are
nurses, because LYNA is positioned for nurses specifically —
"Information OUT for nurses," distinct from physician-documentation
tools like Suki or Abridge.

Every story is anchored to the I-Corps customer-discovery research
(`i-corps/interviews/`, `i-corps/hypothesis-map.md`,
`i-corps/data-room/problem-validation-research.md`). Each story
ends with an **Interview anchor** block citing the specific
interview transcripts, hypotheses (H1–H18), and BMC V2 themes
that the scenario dramatizes — so we never write a journey we
can't trace back to something a real nurse said.

### Story index — what's covered, at a glance

Quick scan before you commit to reading each one in full. Each row
points at the section that has the full narrative, the dialogue,
and the "under the hood" walkthrough.

| §    | Nurse  | Setting                                | Trigger phrase                                | Layer capability                                                       | Interview anchor                                        |
|------|--------|----------------------------------------|-----------------------------------------------|------------------------------------------------------------------------|---------------------------------------------------------|
| 4.1  | Sarah  | Med-surg, 2:15 AM bedside              | "What's the last pain med for bed 14?"        | Live Epic FHIR (MedicationAdministration) + Epic-doc citation          | H5, H7, H9 — bypass-the-screen at point of care         |
| 4.2  | Linh   | Float pool, first shift on 4-South     | "Where are the sterile dressings?"            | Operational Knowledge Base (door codes, supplies, on-call)             | Interview #1 (David, float pool); BMC V2 three-layer baseline |
| 4.3  | Marcus | Charge, late in the no-resource window | "Give me a unit status for 4-South"           | Parallel FHIR fan-out + per-site handoff template (I-PASS / SBAR)      | H12 (12–17 charge-as-sole-routing), H9                  |
| 4.4  | Jamal  | Day-shift, taking over 4 patients      | "Sign-on summary for my four patients"        | Per-shift cutover + sign-on template + cross-shift continuity          | H5, H9; cross-shift continuity inferred from cluster 1  |
| 4.5  | Tanya  | 2 weeks off orientation, refused med   | "Policy for a patient refusing a cardiac med?"| Policy system + Drug Info (both cited explicitly)                      | Interview #2 (Policy Tech complaint); H4, H5            |
| 4.6  | Robert | Med-surg, new admit with 6 active meds | "Is the new cipro okay with what he's on?"    | Hospital AI registry + integrated nursing-reference AI + Drug Info     | H6 (AI-awareness gap), H13 (silent abandonment), H18    |
| 4.7  | Sofia  | Cardiac step-down (4-East), deteriorating | "Rapid response, bed 6, ST changes"        | Emergency-intent path: parallel paging + protocol surfacing + FHIR     | H1 (med-surg/cardiac beachhead), H7; not day-one ICU    |
| 4.8  | Priya  | Med-surg, mid-procedure in isolation   | "Broadcast 4-South: I need a saline flush in 305" | Execution layer in non-emergency mode: targeted broadcast + ack    | Interview #2 (group-chat-from-isolation feature request); H7, H14 |
| 4.9  | Aisha  | Med-surg, wound documentation          | "LYNA, document a pressure injury on bed 18"  | Phone coexistence: voice ↔ camera handoff + workflow resume            | H14 (phone owns camera; LYNA must coexist)              |
| 4.10 | Maya   | Med-surg night, Spanish-only patient   | "Interpreter mode, Spanish"                   | Session-mode change: bidirectional translation + compliance log        | H5 (formal-system bypass), H8 (chronic-normalized); Mt. Sinai catchment language mix |

**Cross-cutting themes the ten stories establish:**

- **Faster than asking a person — not just faster than the
  screen.** The benchmark from the I-Corps interviews is the
  ~5 minutes a float nurse spends finding a senior nurse to ask
  (Interview #1, David Hernandez), not the 2-4 minutes spent at
  a workstation. Every story shows LYNA beating the human-first
  bypass that nurses already adopted (H5) — sub-2-second voice
  round-trip, hands-free, no eyes off the patient (§4.1, §4.6,
  §4.7, §4.8).
- **Every answer carries a citation.** Sarah sees "via Epic MAR /
  FHIR Observation"; Tanya sees "hospital policy NU-MED-027 +
  Drug Info"; Robert sees the integrated AI tool named by name;
  Marcus sees "all data pulled from Epic at 06:42 AM." LYNA is
  never allowed to make a claim without naming where it came from —
  including naming the hospital's own AI tools when they are the
  source (§4.6).
- **Five knowledge surfaces** appear across the nine: the live EHR
  (Epic via FHIR), the per-site Operational Knowledge Base (Linh,
  Marcus, Jamal, Priya), the per-site Policy system (Tanya, Sofia),
  Drug Info, and a **per-site AI registry** that catalogs every
  clinical AI tool the hospital has bought (Robert).
- **LYNA as the router across the hospital's existing AI
  investments.** BMC V2 framing: hospitals are deploying clinical
  AI but nurses don't know it exists at the point of care (H6).
  LYNA's defensibility is not "we have a better model" — it's "we
  are the single voice surface the nurse already uses, and we
  surface every clinical AI tool the hospital already paid for"
  (§4.6 explicitly; §4.5 implicitly via Policy + Drug Info routing).
- **The execution layer** (page, call, broadcast, render to a
  bedside display) shows up in §4.2 (deferred — operator-confirmed),
  §4.6 (deferred — operator-confirmed), §4.7 (autonomous within
  declared emergency intents), and §4.8 (autonomous within the
  declared broadcast-with-acknowledgment intent — the *content* is
  the authorization). Discipline: routine actions need explicit
  confirmation; emergency-intent and help-broadcast actions don't.
- **Phone coexistence, not replacement.** Validated explicitly in
  the BMC V2 update: the phone owns camera-dependent workflows
  (med scanning, pressure-injury photos) and LYNA must hand off
  cleanly (§4.9). Positioning LYNA as a phone replacement is the
  fastest way to lose a CNIO conversation (H14).
- **Session modes for capabilities voice-Q&A alone can't carry.**
  Most journeys fit the query/response shape; one (§4.10
  interpreter) needs a different conversational pattern —
  bidirectional turn-taking, sub-2-second translation latency in
  either direction, and explicit compliance gating against the
  certified-interpreter mandate. Session modes are the
  architectural extension point for the capabilities (interpreter,
  documentation dictation, contextual whisper during a call) that
  break the single-turn query shape.

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

**Interview anchor:** Sarah's story dramatizes the bypass-the-screen
pattern that cluster-1 interviewees consistently described — nurses
choose the fastest information source available, and at 2 AM that
has historically been "walk to the workstation" because there is no
faster option. Maps to **H5** (nurses bypass hospital systems and
go human-first across experience levels and unit types — but at 2
AM there is no human to go to), **H7** (the Vocera-to-smartphone
transition removed hands-free capability nurses still want back —
6/7 cluster-1 nurses confirmed; CNIO confirmed nothing hands-free
exists in the market), and **H9** (screen interruptions during care
increase clinical error risk by ~13%; LYNA replaces a screen lookup
with a voice round-trip). The bedside med-administration timing
detail wasn't directly surfaced by Interview #1 or #2 as a
top-of-mind pain — both interviewees couldn't recall a specific
"critical lab / med info was inconvenient" instance — so the
specific scenario is plausible-but-not-quoted, supported by the
broader bypass-the-screen pattern rather than a literal transcript.

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

**Interview anchor:** Linh's story is the closest of the nine to a
direct transcript. **Interview #1** (David Hernandez, float pool
RN, 8 years experience) described almost every beat: gets his
assignment 5-10 minutes before shift, takes 15-20 minutes to feel
settled on a new unit, struggles with remembering access codes
across units, sometimes lacks system access entirely. Described
units as "territorial" ("this is my computer, this is my that").
Goes to a senior nurse or charge nurse *first* for protocols
because he already knows who's senior; intranet is a distant second
because "navigating the computer would probably take longer."
Estimated ~5 minutes to get an answer from a person. The
**Operational Knowledge Base** — door codes, supply locations,
pager numbers, prep checklists — is the BMC V2 "three-layer
baseline (navigation, reminders, unit-specific knowledge) — works
day one" promise. Maps to **H1** (problem-universality at the
mechanism level; the float onboarding gap exists across every unit
and experience level), **H5** (human-first bypass), and the BMC V2
addition of "screenless clinical workstation" framing.

### 4.3 — Marcus, charge nurse on 4-South, end of shift handoff

It's 6:45 AM. Marcus has been charge on 4-South for the 7p-7a
shift — the second half of which is the **resource-nurse-offline
window**: on this unit, like most med-surg floors at this site,
the resource nurse goes offline 00:00–05:00 to cover staff breaks
and meals, which makes the charge nurse the sole routing layer
for clinical questions, admits, and family escalations for those
five hours (H12). Marcus has been carrying that load. In 15 minutes
he hands off to the day-shift charge, Anita. He needs to compile a
unit-status summary: which patients have open issues, who's NPO
for AM procedures, who's pending discharge, and whether any beds
are free for the ED to admit into.

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

**Interview anchor:** Marcus is the charge-nurse counterpart to
the staff-nurse stories. Cluster 1 interviewed staff nurses, not
charge nurses, so this story is supported by the hypothesis layer
rather than a direct transcript: **H12** (resource nurses go
offline 12:00–17:00 to cover breaks, leaving the charge nurse as
sole routing layer — explicitly identified in the BMC V2 update
as the specific deployment window where LYNA earns its keep),
**H9** (cognitive overload from batching 28 patient charts at end
of shift is exactly the cog-load dimension that interview-2 of the
problem-validation work flags as a separate validated pain
alongside time-loss), and **H1** (the severity tracks unit
structure: floors without a resource nurse to share the routing
load are the beachhead). Cross-validation against cluster-2
interviews — which include charge-nurse roles — is open
follow-up; transcripts not yet ingested. The 12:00–17:00 window
in H12 is the day-shift mirror of the overnight pattern shown
here (00:00–05:00 on this unit); the BMC V2 hypothesis explicitly
names the day-shift window as the validated deployment slot.

### 4.4 — Jamal, day-shift med-surg nurse, coming onto a 4-patient assignment

It's 7:05 AM. Jamal has just walked onto 4-South for his 12-hour
day shift. He picked up four patients, two of whom carried over
from Sarah's night-shift assignment (the same Sarah from §4.1).
The verbal handoff in the break room was three minutes long. He
needs to fill in the gaps before he sees any of his patients.

**Without LYNA:** Jamal sits down at the workstation, opens Epic,
and reads each patient's chart end-to-end — overnight vitals,
notes from the off-going RN, the MAR, any new orders, pending
results, the problem list. Five minutes per patient on a good day,
eight on a bad one. He's still at the workstation 30 minutes into
his shift; the first call light went off five minutes ago.

**With LYNA:** Jamal pulls his patient list up on the unit tablet
and says:

> "Sign-on summary for my four patients."

In about 10 seconds:

> "Four patients on assignment:
>
> **Bed 4 (Cruz, J., 67M, day 3 post-CABG)** — pain not controlled
> overnight per Sarah's handoff. PRN hydromorphone used 4x, last
> 04:20. Pain service consulted; recommendation note posted 06:32
> by Dr. Patel — start scheduled oxycodone 5 mg q6h, taper PRN.
> Order pending pharmacy verification. Watch for: respiratory
> rate, oversedation. No new abnormal vitals since handoff.
>
> **Bed 7 (Garcia, M., 54F)** — NPO since midnight for colonoscopy
> at 08:00, *but* bowel-prep nurse noted incomplete prep at 23:40;
> GI team aware. Status uncertain — confirm before transport.
>
> **Bed 12 (Whitfield, A., 81F)** — admitted overnight, ESRD on
> HD, dialysis scheduled today at 13:00. Yesterday's pre-HD potassium
> 5.1. Last vitals 06:15 stable. Family meeting at 10 AM per
> charge note.
>
> **Bed 19 (Chen, K., 72M)** — cardiac cath at 09:30, consent
> signed, NPO compliant. No overnight events. Watch for: site
> prep timing.
>
> Open issues that need you in the next 30 minutes:
>  1. Verify the new oxycodone order for Cruz before 09:00 dose
>     window
>  2. Confirm Garcia's prep status with GI before transport
>  3. Whitfield's family meeting prep — review yesterday's care
>     plan note from social work."

Jamal reads it once and walks onto the unit knowing exactly what
each patient needs in the next hour. The first hour isn't lost to
chart-scanning; it goes into rounds.

**Under the hood:**

1. LYNA pulls the same parallel FHIR queries Marcus's handoff
   uses (§4.3) — `Encounter`, `Observation`, `MedicationRequest`,
   `MedicationAdministration`, pending `DiagnosticReport` — but
   scoped to Jamal's 4-patient list instead of the whole unit.
2. The "since handoff" framing comes from a per-shift cutover
   timestamp the Operational KB tracks (when day shift formally
   takes over). Anything that landed between Marcus's handoff
   summary and Jamal's sign-on is flagged.
3. The prioritized "needs you in the next 30 minutes" list is
   templated against the same per-site sign-on shape (some sites
   call this a brain sheet, others a focus card); template
   selection lives in the Operational KB.
4. Cross-reference with Sarah's handoff notes happens because the
   off-going-shift handoff (Marcus → Anita, Sarah → Jamal) is
   structured data the Operational KB keeps for the day — Jamal
   sees both the formal Epic chart AND the colored notes his
   off-going colleague flagged.

**Where in the code:**

- Parallel FHIR fan-out: same downstream EHR adapter as §4.3
  (Marcus), scoped to the assignment instead of the unit.
- Sign-on template selection: Operational KB per-site, same
  metadata mechanism §4.3 uses for handoff template selection.
- Cross-shift continuity: per-shift cutover timestamps + handoff
  artifact storage (per-site, lives alongside the unit board in
  the Operational KB layer).

**Interview anchor:** No cluster-1 nurse explicitly described an
"AI compiles my brain sheet at sign-on" pattern, so this story is
an inference from the validated themes rather than a direct
transcript. The 30-minute "first hour lost to chart-scanning"
framing maps to the time-loss dimension validated across the
BMC V2 update; the "since-handoff" cutover hook is the natural
extension of the per-site Operational KB pattern from §4.2 (Linh)
and §4.3 (Marcus). Maps to **H5** (bypass screens; trade workstation
chart-reading for voice summary), **H9** (cog-load batching across
4 patient charts), and **H1** (med-surg beachhead). Direct
transcript validation is open follow-up. The bowel-prep dialogue
ties back to Sarah's overnight handoff (§4.1 / §4.3) so the nine
stories read as a single unit on continuous coverage.

### 4.5 — Tanya, two weeks out of orientation, with a patient refusing a med

Tanya is fourteen days off her formal preceptor period on 4-North.
Her clinical instincts are still building. At 19:40 she walks into
bed 8 with the evening dose of metoprolol; the patient, Mr.
Donaldson, looks her in the eye and says "no, I don't want it
tonight."

Tanya knows there's a hospital policy for refused meds — she has
to chart the refusal, notify the prescribing provider, document
the patient's stated reason, and update the care plan. She
remembers the broad strokes but not the exact steps. Her preceptor
is off today. The charge nurse is dealing with a fall on the other
end of the unit.

**Without LYNA:** Tanya pages her preceptor and leaves a voicemail.
She digs through the hospital intranet for the policy on refused
medications. She isn't sure which menu in Epic is the correct one
for documenting the refusal. 10-15 minutes of trying not to look
unsure in front of the patient.

**With LYNA:** She steps just outside bed 8 and asks:

> "What's our policy for a patient refusing a scheduled cardiac med?"

In two seconds:

> "Hospital policy NU-MED-027 (Refused Medication, revised
> 2025-08-14): for a refused scheduled cardiac med, you need to:
> (1) chart the refusal in Epic under the MAR with reason code,
> (2) notify the prescribing provider within 30 minutes, (3)
> document the patient's stated reason verbatim, (4) reassess
> within 1 hour and re-offer if clinically appropriate, and (5)
> notify the charge nurse if the refusal is repeated.
>
> For metoprolol specifically: holding a scheduled beta-blocker
> can be appropriate, but the prescribing provider needs to know
> because of risk of rebound tachycardia if the patient has been
> on it >7 days.
>
> Source: hospital policy NU-MED-027 + Drug Info for metoprolol."

Tanya goes back into the room, asks Mr. Donaldson why ("it makes
me feel dizzy"), charts the refusal with the cited reason, pages
the cardiologist on call, and goes back to the rest of her round.
Eight minutes total instead of 25.

**Under the hood:**

1. The query "what's our policy for..." dispatches to the **Policy
   system** (one of the 7 integration systems behind LYNA). The
   Policy system is a per-site index of the hospital's own
   policies and procedures, kept current via a documented ingestion
   process.
2. The drug-specific addendum ("for metoprolol specifically...")
   comes from the **Drug Info system** — a separate integration
   that LYNA reaches into when the query is about a specific
   medication.
3. The answer carries both citations explicitly. Tanya knows where
   the institutional policy ends and where the drug-specific
   guidance begins — important when she charts the rationale.

**Where in the code:**

- Query router classification (policy vs. drug-info vs. EHR vs.
  Epic-doc): `epic_intelligence/assistant/voice_router_stub.py`.
- Policy system + Drug Info system are upstream integrations the
  Intelligence Layer queries through the same contract used for
  Epic-doc lookups (`epic_intelligence/query.py`); only the
  underlying corpus differs.
- Citation strategy: same as §4.1 — every answer carries its
  source, never narrate a claim without a citation.

**Interview anchor:** Tanya's story has the cleanest direct
transcript support of any of the nine, drawn from **Interview #2**
(anonymous ICU travel nurse, 9 years experience): "She uses Policy
Tech but said it often doesn't answer her question, so she ends up
hunting for people to find answers." That's exactly the gap LYNA
closes here — voice access to the *same* hospital policy index,
with the answer formatted for action and cited. Tanya's "two weeks
off orientation" framing maps to the BMC V2 beachhead language
("mixed experience" — floors with new grads alongside seniors),
and to **H4** (nurse educators provide PDFs and training but no
audit of sustained use, so post-orientation nurses fall into the
gap she's in). Maps to **H5** (human-first bypass when the system
fails — pages preceptor, hunts for charge), **H4** (educator gap),
and the Policy + Drug Info routing pattern that the BMC V2 update
identified as a core LYNA capability.

### 4.6 — Robert finds an AI tool the hospital has been paying for

It's 13:50. Robert is admitting Mr. Alvarez to bed 22 — wound
infection, started on ciprofloxacin in the ED, six other active
meds including warfarin for a-fib. Robert is two years into
med-surg. His go-to when he's not sure about a drug combination is
the charge nurse, or sometimes the pharmacist if she happens to be
on the unit. He's never used a computer-based reference tool at
the bedside because the workstation is down the hall and he'd
rather just ask.

What Robert doesn't know — and what nobody on 4-South knows — is
that the hospital bought an **integrated nursing clinical-reference
AI** eight months ago. It sits behind one tile in the Epic
Hyperspace launcher and a second tile in the hospital-issued phone
app. Robert has never clicked either. Nor has Tanya, nor Linh,
nor anyone else on the unit. Hospital leadership counts the purchase
on the FY26 capital report as "AI deployed for nursing." Nursing
informatics has no usage data on Robert's unit — because there
isn't any.

**Without LYNA:** Robert pages the pharmacist. She's on another
unit. While he waits, he writes "check cipro vs. warfarin" on his
brain sheet and starts the rest of the admission. Forty minutes
later the pharmacist calls back; the interaction gets noted. Robert
documents and moves on. The hospital's integrated reference AI was
never touched — same as last week, same as the week before.

**With LYNA:** Robert taps the badge mid-admission.

> "Is the new cipro okay with what Mr. Alvarez is already on?"

In about three seconds:

> "Your hospital integrated **a nursing clinical-reference AI** into
> Epic last September — I'm using it for this answer.
>
> Ciprofloxacin 500 mg PO for Mr. Alvarez, cross-checked against
> his six active meds. **One interaction flagged:** ciprofloxacin
> inhibits warfarin metabolism; INR can rise over 3–5 days.
> Patient's last INR (2026-05-14): 2.4, in range. The reference AI
> recommends a recheck at 48 hours and a routine note to
> anticoagulation pharmacy.
>
> No allergies on file. No renal-dose adjustment needed at the
> patient's current creatinine (1.1).
>
> Source: hospital-integrated nursing reference AI (registry ID
> NU-AI-014) + Epic FHIR MedicationRequest + Observation."

Robert acts on it. Before end of shift he sends the routine note to
anticoag — same destination as before, but the interaction was
named at the moment of admission instead of forty minutes later.
The hospital's reference AI is now in his workflow. Not because
anyone trained him on it, but because LYNA *routed through it and
named it*. Tomorrow when he sees the same situation he'll know the
tool exists.

**What this story is about:** the **AI-awareness gap** (H6). The
I-Corps research surfaced a pattern that holds at every site we've
talked to: hospitals are deploying clinical AI tools, the tools end
up behind a tile nurses never click, and nursing informatics has no
usage data to prove it. The BMC V2 update names this explicitly —
"AI awareness gap: nurses don't know tools exist, LYNA routes
automatically." LYNA's defensibility here is not "we have a better
model than the hospital's reference AI." It's "we are the single
voice surface the nurse already uses, and we surface every clinical
AI tool the hospital already paid for — and we name them, so the
tools get credit, the contract gets renewed, and the nurse learns."

**Under the hood:**

1. The query "is X okay with what they're on?" is classified by
   the query router as a multi-source safety check.
2. The router consults the **hospital AI registry** — a per-site
   catalog the operator maintains of every clinical AI tool
   integrated into Epic, the phone app, the intranet, or any other
   surface. Each registry entry declares: name, integration
   surface, what kinds of questions it answers authoritatively,
   auth flow, citation format, fallback behavior.
3. For this query, the integrated nursing-reference AI is the
   registered authority. LYNA queries it via the documented API,
   names it explicitly in the response, and falls back to native
   Drug Info + FHIR if the integrated AI is unreachable.
4. **Manager visibility (H13).** Every routed query is logged with
   the destination AI named. Tomorrow's unit-manager briefing
   shows "integrated reference AI: used 14× yesterday, average
   response 2.8s, top users: Robert, Tanya, Linh." Silent tool
   abandonment — the V2 BMC concern — becomes visible.
5. **Renewal economics (H18).** When the integrated reference AI
   contract comes up for renewal, the hospital can show
   measurable usage that didn't exist before LYNA. The reference
   AI vendor and LYNA are complementary, not competitive — H17.

**Where in the code:**

- **Hospital AI registry:** per-site Operational KB entry. Same
  data-position story as Linh's door codes — every pilot site
  contributes its own registry, the registry compounds with every
  nurse-shift, and the cumulative registry is one of the most
  defensible data positions LYNA accumulates.
- Query router classification + multi-AI dispatch:
  `epic_intelligence/assistant/voice_router_stub.py`.
- **"Name the source" discipline:** same citation strategy as §4.1
  and §4.5. LYNA never claims a finding without naming where it
  came from — and that *includes* naming the hospital's own AI
  tools when they are the source, because the naming is what
  closes the awareness gap.
- Integrated-AI failover: if the registered AI is unreachable,
  LYNA composes the answer from native Drug Info + FHIR and says
  so ("hospital reference AI unreachable; this answer is from
  LYNA's own Drug Info + Epic FHIR"). Never silent fallback.

**Interview anchor:** Maps to **H6** ("hospitals are deploying
clinical AI but nurses do not know it exists at the point of care.
NI team confirmed no usage data for clinical reference tools on
the phone") — the single strongest validated hypothesis in the
post-39-participants map for the BMC V2 "platform integration
layer" addition. Interview #2 explicitly reported being **unaware
of AI tools** at her own hospital (the AI note-taker on other
units). Also maps to **H13** (managers have no visibility into
silent tool abandonment; no current system tracks it),
**H17** (clinical AI vendors are complementary — LYNA drives
bedside adoption of their products), and **H18** (hospitals will
pay for a device that increases utilization of existing AI
investments — incremental spend additive to the phone, not a
replacement). The cipro-warfarin interaction itself is clinical
flavor; the story would work for any cross-AI routing — the
*point* of the story is the routing through the unloved-and-unused
existing investment, not the specific drug interaction.

### 4.7 — Sofia, cardiac step-down nurse, single patient deteriorating at 04:35

Sofia is the assigned RN for bed 6 on **4-East**, the cardiac
step-down unit — a 68-year-old man on day 2 post-CABG, moved out
of CTICU yesterday afternoon per the standard recovery pathway.
4-East is a typical med-surg/cardiac floor: long hallways, mixed
experience levels, no resource nurse overnight, four-to-one ratio.
This is the LYNA beachhead per the BMC V2 update — exactly the
unit type where the communication gap is real and where the
Vocera-to-smartphone regression hurts most. The unit is quiet at
04:35. The cardiac monitor alarms: heart rate jumped from 78 to
130 with new ST depression in leads II and aVF. Sofia looks at the
patient: he's diaphoretic and gripping his chest. The on-call
resident is two floors away. The attending is at home.

She has 60-90 seconds before this becomes a code.

**Without LYNA:** Sofia hits the overhead-page button for rapid
response, runs to the doorway to flag a colleague to bring the
crash cart, mentally runs through the ACS protocol (aspirin? IV
access? 12-lead?), tries to reach the on-call cardiologist by
pager. Each of those is one action; she can only do them serially.
The patient is unattended for stretches of 20-30 seconds in
between. Best case 3 minutes of coordinated response; worst case
the patient codes before any of it is in place.

**With LYNA:** Sofia hits the LYNA badge once and says:

> "Rapid response, bed 6, ST changes."

LYNA executes in parallel, in under 5 seconds:

> "Rapid response activated for 4-East bed 6 — overhead page sent,
> RRT alerted by direct page, ETA 90 seconds.
>
> **On-call cardiology paged:** Dr. Chen, room 2418, acknowledged.
>
> **ACS protocol on bedside display.** Most recent troponin
> (2026-05-17 00:30): 0.08, positive. Active orders: ASA 81 mg
> daily (last given 06:00 yesterday), heparin SC 5000u q12h (last
> given 04:00 today). No documented aspirin allergy.
>
> **Next-action prompts surfaced:** establish second large-bore
> IV; 12-lead EKG; recheck troponin; prepare for possible cath
> lab activation.
>
> Event logged at 04:35:17."

Sofia never had to take her eyes off the patient. The rapid
response team is already running down the hall. The protocol is
on the wall. Cardiology is already paged. Her hands stay on her
patient.

**Without LYNA, she would have done all of this — but serially,
across three minutes of one-handed multi-tasking.** With LYNA,
the same set of actions happens in five seconds in parallel, and
the patient is never alone.

**Under the hood:**

1. "Rapid response, bed 6, ST changes" is recognized as an
   emergency intent. The query router dispatches it through a
   special emergency path with parallel fan-out.
2. **Execution layer in emergency mode:** the overhead page and
   the rapid-response-team direct page both fire automatically
   (no operator confirmation, because this is an emergency intent
   and the nurse's voice command IS the authorization). Cardiology
   paging IS auto-confirmed for ST-change/MI intents.
3. **Protocol surfacing:** the ACS protocol is pulled from the
   Policy system and rendered on the bedside display (LYNA's v2+
   form factor includes a small display at bedside; the v1 iPhone
   form factor renders to the phone).
4. **Patient context pulled in one breath:** parallel FHIR queries
   for the patient's last 24 hours of relevant observations (this
   is the same parallel fan-out from §4.3 Marcus's handoff,
   scoped to one patient and one clinical concern).
5. **Event logging:** the rapid response activation is logged as
   an event so the case can be reviewed downstream — when, what
   was paged, what protocol was surfaced, what the clinical state
   was at the moment of activation.

**Where in the code:**

- Emergency-intent classification + parallel dispatch: the query
  router has a fast-path for known emergency intents; lives in
  `epic_intelligence/assistant/voice_router_stub.py` (production
  router lives downstream and consumes the same contract).
- Execution layer in emergency mode: not yet implemented at the
  level described here; documented as part of LYNA's v2+ feature
  set, on the roadmap behind the v1 iPhone-app baseline.
- Protocol surfacing from Policy system: same path as Tanya's
  policy lookup in §4.5; the difference is the rendering target
  (bedside display vs. nurse's headset).
- Patient-context fan-out: same parallel FHIR pattern as §4.3 and
  §4.4, scoped to one patient and one clinical concern (ACS).
- Emergency-intent path applies on every floor LYNA is deployed
  on; the choice to set this story on cardiac step-down (and not
  ICU) is a positioning choice driven by the I-Corps findings,
  not a technical limitation.

**Interview anchor:** Sofia's story is set on cardiac step-down
rather than the ICU deliberately. **Interview #2** (anonymous ICU
travel nurse, 9 years experience) reported that ICU layout,
proximity, high experience levels, and teamwork "reduce the
problem significantly" — and she explicitly said she didn't miss
Vocera, "hated wearing something heavy, found it annoying to be
interrupted in patient rooms." The BMC V2 update names this:
"Vocera communication gap validated on med-surg/cardiac, **not**
ICU." Per **H1**, the severity of the communication gap tracks
unit structure, not unit type — ICU's close proximity and resource
sharing buffer the gap LYNA is designed to close. Per the BMC V2
beachhead update, **med-surg and cardiac floors without resource
nurses, long hallways, mixed experience** are the day-one target;
ICU is explicitly flagged as a weaker first market that needs
further validation. The 4-East setting honors that finding while
keeping the emergency-intent capability demo intact: the
parallel-dispatch, autonomous-execution, protocol-surfacing pattern
is the same in ICU when it eventually deploys. Maps to **H1**
(structural severity, not unit type), **H7** (hands-free
restoration, validated on med-surg/cardiac), and the BMC V2
beachhead-sharpening update.

### 4.8 — Priya broadcasts from an isolation room

It's 09:20. Priya is in bed 305 — contact + droplet isolation,
full PPE. She is mid-procedure on a deep wound dressing change.
The sterile field is open. The saline flushes she expected to be
at the bedside aren't there; the night-shift PCA stocked the cart
for a different room. Priya needs **one 10mL flush, right now**,
without breaking the field, without de-gowning, and without
leaving the patient.

This is the most ordinary kind of bedside emergency: nothing
clinical is on fire, but the next ninety seconds will either be
spent finishing the dressing change or spent on a chain of
workarounds that breaks sterility.

**Without LYNA:** Priya pushes the call light. The unit secretary
answers from the desk; Priya has to yell through the door because
she can't touch the call-light intercom while gloved and in the
field. The secretary doesn't know what a "10mL saline flush" looks
like or where they're stocked. She walks to clean utility, looks,
walks back, asks Priya which size again. A PCA two doors down
overhears, grabs the flush, gowns up, brings it in. Best case
four minutes. Worst case ten. Meanwhile the field is open and
Priya is one-handed on the wound.

**With LYNA:** Priya nudges the badge with the side of her wrist.

> "Broadcast 4-South: I need a 10mL saline flush in 305, isolation."

In under two seconds, every available RN, PCA, and the unit
secretary on 4-South hears, each in their own headset:

> "Priya in 305 needs a 10mL saline flush — isolation. First
> available, please acknowledge."

Three seconds later, Devon (the PCA two rooms down) taps
acknowledge. Priya hears:

> "Devon picking it up — 90 seconds. Iso-room, he'll gown before
> entering."

Devon brings the flush. Priya never lifts her hands off the
patient. The field stays sterile. Total elapsed time from request
to delivery: under two minutes.

**Under the hood:**

1. "Broadcast {unit}: I need {item} in {room}" is classified by
   the query router as a **broadcast-with-acknowledgment** request.
   The execution layer fires immediately — no operator
   confirmation, because the content of the request *is* the
   authorization (a nurse asking the unit for help is not the same
   risk profile as placing a clinical order).
2. The broadcast targets the on-shift roster from the Operational
   KB scoped to 4-South: every RN and PCA currently logged in for
   the shift. The unit secretary is included automatically because
   at this site secretaries are routed help requests (configurable
   per-site).
3. **First-acknowledge wins.** The other recipients hear "Devon's
   got it" and dismiss. No three people walking to clean utility
   for the same flush.
4. **Isolation tag is composed in.** The Operational KB knows that
   305 is in contact+droplet isolation today; the broadcast carries
   that tag so Devon knows to gown before approaching.
5. **Event logged:** who asked, who covered, time-to-acknowledge,
   time-to-delivery. The manager dashboard surfaces unit
   responsiveness without surveilling individuals (closes the H13
   abandonment-visibility gap from a different angle than §4.6).

**Where in the code:**

- Broadcast routing + first-acknowledge semantics: execution layer,
  v2 capability per the LYNA product brief, currently documented as
  deferred.
- On-shift roster scope + secretary-included rules: Operational KB
  per-site (same data position as Linh's door codes in §4.2).
- Isolation tag compose-in: Operational KB per-site, populated from
  the unit's current census / isolation board.
- Execution-layer policy: this is the second non-emergency
  execution path in the doc (the first is the "page Devon Park"
  example in §4.2). The discipline is "the request itself is the
  authorization" for broadcasts asking for help, but not for
  clinical actions — which keeps the line between routine and
  emergency clear.

**Interview anchor:** This is the only one of the nine that comes
from a **direct, unprompted feature request** by an interviewee.
**Interview #2** (anonymous ICU travel nurse, 9 years): "She
suggested a group chat feature where nurses could message everyone
on the unit at once, especially useful from isolation rooms when
you need someone to grab something." We took her at her word —
this story is that feature, scoped to a med-surg setting (the
beachhead per BMC V2 — long hallways amplify the value, where in
ICU the close proximity reduces it, per the same interviewee).
Also maps to **H7** (hands-free is the unmet need; Priya cannot
touch a phone or call-light intercom while gloved in a sterile
field), **H14** (phone coexistence — Priya's phone is in her
pocket but useless in this moment; LYNA does what the phone
can't), and the BMC V2 addition of execution layer in non-emergency
mode. Cluster-1 staff nurses described falling back to the **call
bell** when hands were full (Interview #1, David: "phones not the
easiest to use" → defaults to call bell when hands full); the
broadcast-with-ack pattern is the natural upgrade from the
call-bell-as-broadcast workaround.

### 4.9 — Aisha hands off to her phone for a wound photo

It's 10:40. Aisha just admitted Ms. Tate to bed 18 — readmission
from skilled nursing for a worsening sacral pressure injury. Per
hospital wound-care policy, every admission with a documented
pressure injury needs a baseline photo within four hours, uploaded
to the patient's chart with the staging, dimensions, and a
nurse-authored note. The photo is non-negotiable — wound-care
nursing reviews them every morning, and the policy explicitly
requires images for stages 3 and 4.

LYNA can do many things. It cannot take a photo.

**Without LYNA:** Aisha gets the phone-app workflow started, then
spends two minutes hunting for the right form (wound assessment
lives under "documentation" in the Epic Haiku menu, not under
"vitals" where she keeps expecting it). She takes the photo,
remembers there's a staging field, scrolls back, fills it in,
saves, and starts the note. Total time: 12 minutes, broken across
several attempts because Ms. Tate kept asking questions.

**With LYNA:** Aisha taps the badge.

> "LYNA, document a pressure injury on bed 18."

> "Pressure-injury documentation needs your phone camera — I can't
> take photos. I've opened the wound-imaging form in Epic Haiku on
> your phone and pre-filled it for bed 18, sacral, on-admission. Tap
> when you're ready to capture. I'll pick the workflow back up when
> you're done."

Aisha takes the photos: overview, close-up, with the staging
ruler. Two taps; Haiku uploads them. She nudges the badge.

> "Photos uploaded?"

> "Three photos uploaded to bed 18, encounter #4429-A, tagged
> 'sacral, on-admission.' Stage isn't classified yet. Want me to
> walk you through the staging criteria, or do you want to dictate
> the stage and the note?"

Aisha says "stage 3, full-thickness, no slough or eschar visible,
3.4 by 2.1 cm." LYNA renders the note, reads it back, files it.
Total time: under five minutes. Photo, staging, note, all anchored
to the same encounter in Epic.

**Under the hood:**

1. The query router recognizes "document a pressure injury" as a
   **camera-dependent intent** and dispatches it through the
   phone-coexistence path: open the right form in Epic Haiku,
   pre-fill what LYNA already knows (patient, room, anatomical
   site if dictated, on-admission timestamp), and hand off
   gracefully.
2. **Voice-to-Haiku handoff** uses Epic's existing SMART app
   launch into Haiku with context parameters — nothing custom on
   the Epic side; LYNA just composes the launch URL.
3. **Resume after handoff:** LYNA monitors the encounter for the
   photo upload event (via Epic FHIR `DocumentReference` polled or
   subscribed to). When images appear, it resumes the workflow,
   offers the staging dialog, and writes the note via voice
   dictation.
4. **No LYNA replication of camera workflows.** This is a deliberate
   non-feature. We could put a camera on a future LYNA badge form
   factor; we have chosen not to. The phone owns camera-dependent
   workflows because the phone is already in every nurse's pocket
   and every hospital's BYOD/MDM policy already covers it. LYNA's
   defensibility is not "we replace the phone" — it's "we are the
   voice surface the phone never had."

**Where in the code:**

- Camera-dependent intent classification + Haiku handoff:
  `epic_intelligence/assistant/voice_router_stub.py` (the
  production handoff lives downstream; the router contract is the
  same).
- Resume-after-handoff via FHIR `DocumentReference`: same FHIR
  client used by Sarah's `MedicationAdministration` query in §4.1.
- Note dictation + staging dialog: synthesis layer composes a
  structured wound-care note from the dictated fields against the
  per-site Policy system's wound-staging schema (same Policy system
  used by Tanya in §4.5 and surfaced as ACS protocol by Sofia in
  §4.7).

**Interview anchor:** Maps cleanly to **H14** (LYNA must coexist
with the phone, not replace it; the CNIO will redirect to phone
capabilities if positioned as replacement — explicitly named in
the BMC V2 update as "phone coexistence for camera-dependent
workflows (med scanning, pressure injury photos)"). This is the
single most CNIO-sensitive story of the nine: getting this
boundary right is the difference between LYNA being adopted as an
additive incremental device and being killed as "another phone."
Also reinforces **H17** (LYNA is the bedside surfacing layer for
Epic — and for the hospital's phone-side tools — rather than a
competing system) and the BMC V2 framing of LYNA as "screenless
clinical workstation: one voice interface to every tool the
hospital has."

### 4.10 — Maya bridges a language gap at 03:00

It's 03:00. Maya is the night-shift RN on 4-South. Bed 16 just
admitted from the ED four hours ago — Mr. Reyes, post-op day 0,
Spanish-only. His family went home at 22:00. The certified-
interpreter phone line at this hospital averages a 9–14 minute
wait at night because the daytime in-house Spanish interpreters
are off after 23:00 and night coverage is contract video-relay
with a five-position queue.

Maya needs to know two things, now: is Mr. Reyes in pain, and is
he comfortable enough to sleep. These are ad-hoc clarifications,
not the kind of decision that legally requires a certified
interpreter (consent, discharge teaching, clinical decision-
making). She has been using her phone's Google Translate app for
the easy ones — "are you cold?" "do you need water?" — and
calling the interpreter line for anything substantive.

**Without LYNA:** Maya types into Google Translate, shows the
phone to Mr. Reyes, he speaks back, she points the mic at him,
the app translates. Two-handed, screen-mediated, slow. Mr. Reyes
gets tired of looking at her phone and goes back to wincing
silently.

**With LYNA:** Maya taps the badge.

> "Interpreter mode, Spanish."

In two seconds:

> "Interpreter mode active. Spanish–English bidirectional. Speak
> normally; I'll translate both ways. Ad-hoc clarification only —
> say 'queue interpreter' if you need a certified interpreter for
> consent or discharge teaching."

Maya speaks naturally into the badge:

> "Mr. Reyes, are you having any pain right now? On a scale of 0
> to 10."

LYNA reads in Spanish through the room speaker (or through Mr.
Reyes' bedside earpiece if he's been set up with one):

> "Sr. Reyes, ¿tiene dolor en este momento? En una escala del
> cero al diez."

Mr. Reyes responds:

> "Sí, como un siete. Aquí, en el pecho."

LYNA reads in English back to Maya through her earpiece:

> "Yes, about a seven. Here, in the chest."

The exchange continues for ninety seconds. Maya gets the pain
score, the location, the quality, and whether he wants the PRN.
She gives him the morphine, reorients him to the room, sets the
expectation that someone will check on him in two hours, and
leaves him to sleep. Total time: under three minutes. The
interpreter line was never called.

**The discipline LYNA enforces:**

> "I machine-translated this exchange for ad-hoc bedside
> clarification. For consent, discharge teaching, or any clinical
> decision that requires certified interpretation, queue the
> interpreter service. Logged at 03:01 for compliance audit."

This message appears once at the start of every interpreter-mode
session and is logged with the session, so the hospital can audit
machine-translation usage against the cases where certified
interpretation was legally required.

**Under the hood:**

1. "Interpreter mode, {language}" is classified by the query
   router as a session-mode change. The voice pipeline switches
   from query/response to bidirectional translation; the response
   path now goes through translation before TTS.
2. **Per-language model selection.** Spanish has the strongest
   models and is the day-one launch language. The per-site
   Operational KB declares which languages the hospital has
   committed to (driven by patient-mix data); LYNA refuses
   gracefully ("I don't have certified interpreter coverage in
   {language} at this hospital — let me queue the interpreter
   service") for languages outside that set.
3. **Sub-2-second turn latency.** The end-to-end voice path
   (capture → STT → translate → TTS → speaker/earpiece) stays
   under two seconds in either direction. This is the bar that
   makes the conversation feel like a conversation, not a phone
   relay.
4. **Compliance log.** Every interpreter-mode session writes a
   structured event: who initiated, which patient, which language,
   start time, end time, whether 'queue interpreter' was invoked,
   transcripts (PHI-handled per the standard rules). This is the
   audit trail compliance asks for when the hospital signs off on
   machine translation as a permissible ad-hoc tool.
5. **Patient-side delivery.** v1 (iPhone) delivers Spanish through
   the room speaker via Bluetooth or a wired connection — Mr.
   Reyes hears LYNA from the room, not from Maya's phone. v3
   (dedicated LYNA badge) can route through a paired bedside
   earpiece for the patient, keeping the exchange private from
   other beds in shared rooms.
6. **Hand-off to certified interpreter.** "Queue interpreter" is
   an execution-layer action (deferred — operator-confirmed in v1)
   that places the room in the hospital's interpreter queue and
   maintains LYNA's ad-hoc translation in the interim. When the
   certified interpreter joins, LYNA backs off.

**Where in the code:**

- Session-mode classification + bidirectional voice pipeline:
  `epic_intelligence/assistant/voice_router_stub.py` (the
  production router routes session-mode commands through a
  separate path from query/response).
- Translation models: separate from the query/response LLM stack;
  per-language model selection lives in the synthesis layer.
- Per-site language coverage: Operational KB per-site, same data
  position as §4.6's hospital AI registry.
- Compliance logging: extension of the memory-event log; see
  `memory_system/PROTOCOL.md` for the event schema.
- Interpreter queue hand-off: execution layer, v2+ capability per
  the LYNA product brief.

**Interview anchor:** This is the weakest direct-interview anchor
of the ten. Neither Interview #1 (David Hernandez, float pool) nor
Interview #2 (anonymous ICU travel) raised language barriers as a
top-of-mind pain — both interviewees are English-comfortable and
both currently work in English-comfortable units. The story is
kept in the canonical journey set for three reasons: **(a)** Mt.
Sinai's catchment area in Manhattan has a high non-English-
speaking patient mix (35%+ in some service lines), making language
access a Title VI compliance requirement the hospital must address
regardless of nurse-side advocacy; **(b)** the prior interaction-
flows doc (`hardware/opalDevice/docs/ux/opal-interaction-flows.md`
Flow 3, predates the I-Corps work) included interpreter mode as a
core capability, reflecting earlier team consensus that this is
real; **(c)** the pattern maps to **H5** (nurses bypass formal
systems — the interpreter-line queue is the formal system, "Google
Translate at the bedside" is the bypass everyone uses anyway) and
**H8** (chronic-normalized — the 9–14 minute interpreter wait at
night is accepted as just-how-it-is, not a hair-on-fire problem
leadership prioritizes). When cluster-2 transcripts are ingested,
this story should be cross-validated against any interview with an
RN on a unit with a high non-English-speaking patient mix; for now
it's documented as an evidence-thin but operationally important
addition.

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
