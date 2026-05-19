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

Seven stories from the floor, spanning the day-to-day shape of
nursing work: a routine bedside lookup, onboarding to an unfamiliar
unit, a multi-patient handoff, taking over patients at the start of
shift, a new graduate building confidence, a safety check at the
point of medication administration, and a single-patient
deterioration in the ICU. All seven are nurses, because LYNA is
positioned for nurses specifically — "Information OUT for nurses,"
distinct from physician-documentation tools like Suki or Abridge.

### Story index — what's covered, at a glance

Quick scan before you commit to reading each one in full. Each row
points at the section that has the full narrative, the dialogue,
and the "under the hood" walkthrough.

| §    | Nurse  | Setting                                | Trigger phrase                             | Layer capability exercised                                            |
|------|--------|----------------------------------------|--------------------------------------------|------------------------------------------------------------------------|
| 4.1  | Sarah  | Med-surg, 2:15 AM bedside              | "What's the last pain med for bed 14?"     | Live Epic FHIR (MedicationAdministration) + Epic-doc citation         |
| 4.2  | Linh   | Float pool, first shift on 4-South     | "Where are the sterile dressings?"         | Operational Knowledge Base (door codes, supplies, on-call)            |
| 4.3  | Marcus | Charge nurse, end of 7p–7a shift       | "Give me a unit status for 4-South"        | Parallel FHIR fan-out + per-site handoff template (I-PASS / SBAR)     |
| 4.4  | Jamal  | Day-shift, taking over 4 patients      | "Sign-on summary for my four patients"     | Per-shift cutover + sign-on template + cross-shift continuity         |
| 4.5  | Tanya  | 2 weeks off orientation, refused med   | "Policy for a patient refusing a cardiac med?" | Policy system + Drug Info (both cited explicitly)                  |
| 4.6  | Robert | Med-surg, new cipro at bedside         | "Verify safety for bed 22"                 | Drug Info interaction matrix + FHIR med list + renal dose check       |
| 4.7  | Sofia  | ICU, single patient deteriorating      | "Rapid response, bed 6, ST changes"        | Emergency-intent path: parallel paging + protocol surfacing + FHIR    |

**Cross-cutting themes the seven stories establish:**

- **Sub-2-second answer latency** is the bar in every story — the
  voice round-trip must complete fast enough that the nurse never
  takes her hands off the patient (§4.1, §4.7) or her eyes off the
  task (§4.6).
- **Every answer carries a citation.** Sarah sees "via Epic MAR /
  FHIR Observation"; Tanya sees "hospital policy NU-MED-027 + Drug
  Info"; Marcus sees "all data pulled from Epic at 06:42 AM." LYNA
  is never allowed to make a claim without its source.
- **Three knowledge surfaces** appear across the seven: the live
  EHR (Epic via FHIR), the per-site Operational Knowledge Base
  (Linh, Marcus, Jamal), and indexed published documentation (Epic
  developer docs in §4.1, hospital policy in §4.5).
- **The execution layer** (page, call, broadcast, render to a
  bedside display) shows up in §4.2 (deferred — operator-confirmed),
  §4.6 (deferred — operator-confirmed), and §4.7 (autonomous within
  declared emergency intents). The discipline is consistent:
  routine actions need confirmation; emergency-intent actions don't.

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

### 4.6 — Robert verifies a new medication at the point of administration

It's 14:20. Robert is administering a first dose of ciprofloxacin
500 mg to Mr. Alvarez in bed 22. The order is new — it came in
from infectious disease this morning for a wound infection.
Mr. Alvarez is on six other active medications, including warfarin
for a-fib.

**Without LYNA (current best practice):** Robert scans the
medication barcode, the system confirms it matches the order, and
the dose is administered. The check-against-everything-else
happens at pharmacy verification before the order goes live. *In
theory* it catches interactions. *In practice* the cipro-warfarin
interaction (cipro inhibits warfarin metabolism, raising INR over
3-5 days) is a known one but routinely missed if the patient's INR
isn't already trending high.

**With LYNA:** Robert scans the barcode at bedside as usual, then
adds:

> "Verify safety for bed 22."

In about 4 seconds:

> "Ciprofloxacin 500 mg PO for Mr. Alvarez, bed 22 — verified
> against active orders and barcode.
>
> **Allergies:** no documented cipro or fluoroquinolone allergy.
>
> **Interaction flag:** ciprofloxacin + warfarin. Cipro inhibits
> warfarin metabolism and typically raises INR over 3-5 days.
> Patient's last INR (2026-05-14) was 2.4, in range. Recommend:
> recheck INR in 48 hours, communicate to anticoag service.
>
> **Other:** no max-dose issues, no renal-dose adjustment needed
> at the patient's most recent creatinine (1.1)."

Robert administers the dose. Before the end of his shift, he sends
a routine message to anticoagulation pharmacy flagging the new
cipro start and the INR recheck recommendation. The interaction
gets handled the same shift it was introduced — not 72 hours later
when the patient's INR is suddenly 4.8.

**Under the hood:**

1. The barcode scan is normal Epic / BCMA flow; LYNA layers on a
   second, broader safety pass.
2. The interaction check pulls from the **Drug Info system**
   (cross-reference: meds the patient is actively on per FHIR
   `MedicationRequest`, plus the one being administered).
3. The dose-adjustment check uses the patient's recent `Observation`
   values (creatinine) via Epic FHIR.
4. The "flag and recommend" output is structured so Robert can act
   immediately without having to go back to a workstation to look
   things up.
5. LYNA does **not** auto-page anticoagulation pharmacy here —
   that's an action that needs Robert's deliberate confirmation
   via the execution layer. The recommendation is surfaced; the
   action is operator-initiated.

**Where in the code:**

- Drug Info + Epic FHIR pull: query router dispatches based on the
  intent ("verify safety" classifies as a multi-source safety
  check) — `epic_intelligence/assistant/voice_router_stub.py`.
- Interaction matrix: the Drug Info system carries pairwise + n-way
  interactions; the Intelligence Layer composes them with the
  patient's active med list to produce a per-patient verdict.
- Execution-layer paging (when Robert chooses to send): same path
  as Linh's "page Devon Park" in §4.2, requires explicit operator
  confirmation.

### 4.7 — Sofia, ICU nurse, single patient deteriorating at 04:35

Sofia is the assigned RN for bed 6 in the ICU — a 68-year-old man
on day 2 post-CABG. The unit is quiet. At 04:35 the cardiac
monitor alarms: heart rate jumped from 78 to 130 with new ST
depression in leads II and aVF. Sofia looks at the patient: he's
diaphoretic and gripping his chest. The on-call resident is on
another unit. The attending is at home.

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

> "Rapid response activated for ICU bed 6 — overhead page sent,
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
