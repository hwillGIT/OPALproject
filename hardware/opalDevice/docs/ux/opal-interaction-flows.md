# LYNA Interaction Flows — v1 iPhone App

**Date:** 2026-05-20
**Form factor:** v1 — iPhone app (hospital-issued or BYOD) + Bluetooth earpiece
**Scope:** Per-journey screen flows for the 10 LYNA clinical-staff
journeys in
[`INTELLIGENCE_LAYER.md`](../../../../INTELLIGENCE_LAYER.md) §4
**Status:** Supersedes the 2025-11-19 8-flow draft (pre-I-Corps,
device-touchscreen target). Manager dashboard is documented
separately in [`manager-dashboard.md`](manager-dashboard.md).

---

## 0. Context — what changed and why

### 0.1 Form-factor pivot

The earlier draft of this doc (dated 2025-11-19) targeted a
**dedicated device with an embedded touchscreen** running the LVGL
theme in `implementation/lvgl-theme/`. The design-system, screen
designs, and wireframes in this directory all reflect that
target — large "TALK" button, mode indicator at top, full-screen
modal alerts on a small panel.

After the I-Corps customer-discovery work (`i-corps/`,
post-39-participants `hypothesis-map.md`), v1 has been
**re-targeted to the iPhone** (hospital-issued or BYOD) plus a
Bluetooth earpiece. Reasons:

- **Phone coexistence (H14).** The CNIO will redirect any
  conversation that positions LYNA as a phone replacement; the
  phone owns camera-dependent workflows and is already in every
  nurse's pocket with hospital MDM coverage. v1 sits on top of
  the phone, not next to it.
- **Time-to-pilot.** No hardware certification cycle, no biomedical
  engineering review, no new procurement line. iPhone deploys via
  the hospital's existing MDM in days.
- **Validated bypass-the-screen pattern (H5, H7, H9).** The voice
  surface is the differentiator; the phone is the visual surface
  the voice can hand off to. v1 proves the voice value before v3
  hardware is built.

v3 — the dedicated LYNA badge with mini display, bone-conduction
audio, RFID auth, magnetic charging — is the eventual target form
factor. The existing wireframes (`opal-ui-wireframes.md`),
design system (`opal-design-system.md`), and screen designs
(`opal-screen-designs.md`) document **v3 surfaces** and remain
valid reference material for the v3 pass.

**v2 — Vocera-class wearable or Apple Watch — is intentionally
skipped.** Per the I-Corps interviews, Vocera-flavored hardware
attracts the "I hated wearing something heavy / interrupted in
patient rooms" objection (Interview #2). Going straight from
iPhone (v1) to dedicated optimized hardware (v3) avoids that.

### 0.2 Voice-first principle

LYNA is voice-first. Screens carry what voice cannot:
- Long structured output (a 28-patient unit summary, a 4-patient
  brain sheet)
- Persistent visual state (an active critical alert, an active
  interpreter session)
- Bidirectional interaction needing visual confirmation (broadcast
  acknowledgment tracking)
- Handoffs to apps LYNA doesn't own (Epic Haiku for camera work)

**5 of the 10 journeys require a real screen; 5 are voice-primary
with optional screen affordances.**

| § | Story | Voice-primary | Needs screen |
|---|---|---|---|
| 4.1 | Sarah / pain med | yes | optional response card |
| 4.2 | Linh / float onboarding | yes | optional unit cheat sheet |
| 4.3 | Marcus / unit handoff | partial | **required** (S4 brain sheet) |
| 4.4 | Jamal / sign-on | partial | **required** (S4 brain sheet) |
| 4.5 | Tanya / policy lookup | yes | optional response card |
| 4.6 | Robert / AI routing | yes | optional, but first-time UX wants S3 |
| 4.7 | Sofia / rapid response | yes | **required** (S5 critical alert) |
| 4.8 | Priya / broadcast | yes | **required** for ack tracking (S6) |
| 4.9 | Aisha / camera handoff | yes | **required** (handoff banner + Haiku) |
| 4.10 | Maya / interpreter | yes | **required** (S7 interpreter mode) |

### 0.3 Mapping from the prior 8-flow draft

| Old flow (2025-11-19) | New status | Notes |
|---|---|---|
| 1. Targeted Call | absorbed into §4.7 cardiology paging + §4.2 "page Devon Park" | calling pattern reused as an execution-layer affordance, not its own journey |
| 2. Broadcast Message | §4.8 (Priya) — surface S6 | mode-switcher pattern (TARGETED/BROADCAST) retained, scoped to broadcast composer |
| 3. Interpreter Mode | §4.10 (Maya) — surface S7 | compliance log + "queue interpreter" hand-off added; bidirectional turn-taking same as old draft |
| 4. Critical Alert Response | §4.7 (Sofia) — surface S5 | direct match; haptic + protocol display retained |
| 5. Mode Switching | reusable pattern §3.1 | not a journey on its own — applies to broadcast + interpreter session-mode entry |
| 6. Voice-to-EMR Order | dropped from canonical journeys | old flow was physician-flavored ("Start 2 L of O2 and get a portable CXR"). LYNA positions as "Information OUT for nurses," not order entry. Documentation/dictation reframing tracked in §6 deferred work. |
| 7. Contextual Router | absorbed across all journeys | not a journey; it is how LYNA works. The "intelligent node" idea now lives most explicitly in §4.6 Robert (AI registry routing) |
| 8. Dashboard Monitoring | **separate doc** — [`manager-dashboard.md`](manager-dashboard.md) | dashboard is a different user (unit manager / CNO / informatics), not the nurse. Pulled out so the nurse-facing flows stay coherent. |

---

## 1. Surface inventory

Ten reusable surfaces. Most journeys compose 2–4 of these.

### S1 — Voice Command surface

Always reachable from anywhere in the app. Voice surface is where
every journey starts and ends.

**States:**
- Idle (wake word listening)
- Listening (active capture, waveform, transcription preview)
- Processing (spinner, latency indicator)
- Speaking (response readback; tap to mute readback and read on
  screen instead)
- Error (network down, transcription confidence too low)

**Input affordances:**
- Wake word ("Hey LYNA") — primary
- Hold-to-talk (TALK button) — secondary, for noisy environments
- Tap-to-talk + tap-to-stop — accessibility / glove-friendly

**Output affordances:**
- Voice through Bluetooth earpiece (primary)
- Phone speaker (if no earpiece paired)
- Visual transcript (always shown on screen during interaction;
  scrollable history)

**v3 implications:** the wake word + earpiece pattern survives
identically; the phone-speaker fallback is replaced by
bone-conduction audio on the badge.

### S2 — Home / Mode Indicator

The app's default screen. Shows the nurse who they are, what mode
LYNA is in right now, recent queries, and quick actions.

**Top:**
- Nurse identity (RFID-linked, voiceprint-verified)
- Unit assignment for this shift
- Mode pill — NORMAL (blue), BROADCAST (orange), INTERPRETER
  (purple). Always visible; tapping it opens the mode switcher.

**Body:**
- Recent queries (last 5–10) — tap to re-ask or to see the
  cited response again
- Quick actions: "Brain sheet" (→ S4), "Page someone," "Start
  broadcast" (→ S6), "Interpreter mode" (→ S7)

**Bottom:**
- TALK button (large, glove-friendly)
- Settings affordance (rare; see S10)

**v3 implications:** the persistent mode pill carries over; the
recent-queries scroll collapses to a single most-recent-query
view because the v3 display is smaller.

### S3 — Response Card

Formatted output for queries that produce a single structured
answer. Used by every journey that returns a discrete fact.

**Shape:**
- Header — the question (echoed back so the nurse can confirm
  LYNA heard correctly)
- Body — the answer in plain English. Bold the key value (dose,
  time, INR, policy number).
- AI-source pill (§4.6, §3.2) — names the underlying source by
  name when it's a hospital-integrated tool. Tap for source detail.
- Citation footer — every response, no exceptions. Shows the
  exact source LYNA pulled from (FHIR endpoint, policy doc,
  hospital AI registry entry, etc.).
- Action affordances — "Chart this," "Page X," "Send to anticoag
  pharmacy" — surface execution-layer actions inline when the
  answer suggests one.

**Used by:** §4.1, §4.5, §4.6 (with AI-source pill), §4.7 (within
the critical-alert surface), §4.10 (per-turn within interpreter
session).

**v3 implications:** Response Card is the surface most affected by
v3 display constraints. The v3 badge shows only the bold-key-value
+ citation pill; tap for the full body view on the v3 display
(if present) or readback via voice.

### S4 — Patient/Unit Brain Sheet

Used by Marcus (§4.3) and Jamal (§4.4). The voice trigger pulls
the structured query; the result is too dense for voice readback,
so it renders to a brain-sheet surface.

**Shape:**
- Header bar — unit name, time of pull, "data current as of HH:MM"
- For each patient (compact, scrollable list):
  - Bed / name / age / day of admit
  - Open clinical issues (red dot if anything overnight)
  - Pending procedures / NPO status
  - Pending discharge
  - "Watch for" — the prioritized next-30-minute items
- Sticky bottom bar — "These N items need attention now" — the
  prioritized list from the voice readback, shown as a tappable
  checklist
- Per-patient detail tap — expands into a full per-patient view
  with the same data Sarah saw at the bedside (§4.1) but for
  the whole assignment

**Refresh:**
- Pull-to-refresh re-fires the parallel FHIR fan-out
- Auto-refresh every 5 minutes unless the nurse is mid-readback
- "Live since 06:42 AM" indicator when stale

**v3 implications:** the brain sheet is too dense for the v3
badge display. The nurse either holds the phone for the brain
sheet (and uses voice for everything else) or the brain sheet
casts to the unit tablet / workstation via SMART app launch.

### S5 — Critical Alert (Full Screen)

Used by §4.7 Sofia receiving an alert, by the rapid-response-team
members hearing the page, and by any nurse who triggers an
emergency intent.

**Shape:**
- Full-screen takeover — preempts whatever was on the phone
- Haptic — strong, repeated, escalating if not acknowledged
  within 5s
- Audio — alarm tone + voice readback through earpiece
- Visual:
  - Red background, pulsing border
  - Alert type — "Rapid Response" / "Code Blue" / "Bleed Alert"
  - Location — unit + bed number, large
  - Patient — name + age + relevant clinical summary (one line)
  - **ACK button** — single big tap, glove-friendly
  - "View Protocol" affordance — pulls ACS / sepsis / fall
    protocol from the Policy system (cited)
  - "View Vitals" affordance — pulls the last hour of relevant
    `Observation` data from FHIR
- After ACK:
  - Alert badge moves to top status bar (still visible but no
    longer modal)
  - Nurse can issue voice commands while alert remains live
  - "End response" closes the alert once the situation has
    resolved (logged)

**Logged event:** every alert (received, acknowledged, viewed
protocol, viewed vitals, ended) writes a memory event.

**v3 implications:** v3 badge gets the haptic + audio + a
single-button ACK; full protocol viewing renders to the v3
mini-display or escalates to the phone.

### S6 — Broadcast Composer + Ack Tracker

Used by §4.8 Priya. Splits into two views: sender and receivers.

#### S6a — Sender (broadcaster)

Entry — voice trigger ("Broadcast 4-South: I need a 10mL saline
flush in 305, isolation"). LYNA parses and shows:

- Confirmation card — "Broadcasting to 4-South: 10mL saline flush
  to 305 (isolation tag)" — sender sees and hears for 1.5s
- After auto-confirm: Ack Tracker view
  - Roster of available recipients (RNs, PCAs, secretary)
  - First responder highlighted as they ack
  - ETA shown ("Devon picking it up — 90 seconds")
  - "Cancel broadcast" affordance

#### S6b — Receivers

Each recipient's phone shows:

- Lighter-weight non-modal banner at the top of S2 Home
- Voice readback through earpiece
- "Acknowledge" button — single tap, sets the first-ack-wins
- After someone acks: banner updates to "Devon's got it" and
  auto-dismisses after 3s

**Logged event:** broadcast emit, each ack attempt, the winning
ack, delivery confirmation.

**v3 implications:** v3 badge has a dedicated broadcast button
(physical, satisfying tactile click) → enters mode S6a via voice;
receivers feel haptic + hear voice and ack via single button.

### S7 — Interpreter Mode (Bidirectional Session)

Used by §4.10 Maya. A session mode, not a query/response.

**Entry:** "Interpreter mode, {language}" or tap the mode pill
in S2 and select INTERPRETER.

**Compliance moment (every session):**
- Modal card on entry: "Machine translation for ad-hoc bedside
  clarification only. For consent, discharge teaching, or
  clinical decisions, certified interpreter required. 'Queue
  interpreter' is available at any time."
- Tap "Got it" — logged as acknowledgment

**Active-session shape:**
- Dual-language indicator at top: "English ↔ Spanish (machine
  translation)"
- Active-speaker indicator — pulsing dot under whichever language
  is currently being captured
- Last-3-turns transcript visible — both languages, side by side
- "Queue interpreter" affordance — taps into the hospital
  interpreter-service queue while LYNA keeps translating in the
  interim
- "End interpreter mode" affordance — single tap, logged with
  duration

**Patient-side audio:** v1 routes through the phone's speaker
(positioned on the bedside tray, or paired with a bedside
Bluetooth speaker if the hospital provides one). v3 routes
through a paired patient earpiece.

**Logged event per session:** start, language, end, turn count,
whether "queue interpreter" was invoked. PHI handled per the
standard event-log policy.

**v3 implications:** session-mode framing carries over; the
v3 badge supports a paired patient earpiece for privacy in
shared rooms.

### S8 — Camera Handoff Banner

Used by §4.9 Aisha. Always paired with the Epic Haiku app.

**Shape:**
- Banner card on S2 Home: "Pressure-injury photo needs your
  phone camera — I've opened Haiku to bed 18, sacral,
  on-admission. Tap when done."
- Tapping the banner switches to Haiku (SMART app launch with
  pre-filled context)
- LYNA detects Haiku upload via FHIR `DocumentReference`
  subscription
- Banner updates: "3 photos uploaded — want to dictate the
  staging note?"
- Tapping resumes the LYNA workflow; voice surface activates

**v3 implications:** v3 badge has no camera. The hand-off still
goes to the phone — the phone is the camera in every form factor.

### S9 — Login / Shift Start

Once per shift.

**Steps:**
1. Nurse opens app → prompted to badge-tap (RFID, if available)
   or PIN (fallback)
2. Voiceprint verification — read a sample sentence, system
   confirms voice profile
3. Patient assignment pull — LYNA queries the hospital's assignment
   system (per-site, lives in Operational KB) and confirms:
   "You're on 4-South, beds 7, 12, 18, 22 today."
4. Mode selection — defaults to NORMAL; nurse can pre-set BROADCAST
   for a shift on a high-acuity unit
5. "Ready" — drops into S2 Home

**v3 implications:** v3 has hardware RFID (badge tap on the device);
v1 uses the phone's hardware (camera-based badge scan or NFC if
the phone has it; PIN otherwise).

### S10 — Settings / Preferences

Rarely used. Surfaces:

- Wake word ("Hey LYNA" / custom)
- Voice volume + earpiece selection
- Default mode at shift start
- Interpreter language defaults (which languages are pre-loaded for
  the units the nurse covers most)
- Privacy: "Show me what LYNA has logged about my queries"
  (compliance affordance)
- Sign out

Not detailed in this pass.

---

## 2. Per-journey flows

Each flow names the surfaces it uses, lists the steps, and notes
v3 implications.

### Flow 4.1 — Sarah, bedside pain-med lookup

**Surfaces used:** S1 voice command, optionally S3 response card.

```
[S2 Home, NORMAL mode]
    │
    ├─ Wake word: "Hey LYNA, what's the last pain med for bed 14?"
    │
[S1 Voice Command — Listening → Processing]
    │
    ├─ Router classifies: live-data query (Epic FHIR
    │   MedicationAdministration)
    ├─ Parallel: query Epic FHIR for bed 14's MAR
    │
[S1 Voice Command — Speaking through earpiece]
    │
    ├─ "Mrs. Reynolds in bed 14 last had hydromorphone 0.5 mg IV
    │   at 11:43 PM, about 2.5 hours ago. PRN q3h. Due in 30 min;
    │   sooner is a call to the resident."
    ├─ Citation: Epic MAR via FHIR Observation
    │
[Optional: S3 Response Card persists for 10s on screen]
    │
    └─ Returns to S2 Home
```

**Errors:**
- FHIR endpoint unreachable → "I can't reach Epic right now;
  the workstation in the corridor has the MAR" (honest about the
  limit; no fake data)
- Ambiguous bed reference (multiple Reynolds in the unit) →
  "There are two Reynolds — bed 14 in 4-South or bed 14 in 6-North?"

**v3:** identical flow. No screen needed at all in the typical
case; v3 badge mini-display can render the dose + time + due-time
as a glanceable card.

### Flow 4.2 — Linh, float onboarding queries

**Surfaces used:** S1 voice command, optionally S3 response card.

```
[S9 Login completes → S2 Home, NORMAL mode]
    │
    ├─ Wake word: "Where are the sterile dressings on this unit?"
    │
[S1 Voice Command]
    │
    ├─ Router classifies: Operational KB query (supplies)
    │
[S1 Voice Command — Speaking]
    │
    ├─ "On 4-South, sterile dressings are in clean utility across
    │   from bed 12, second cabinet from left, second shelf.
    │   Sizes 4x4 and 2x2 stocked..."
    │
    └─ Returns to S2 Home (S3 card optional)

[Repeated for: med-room door code, charge nurse, on-call attending]

Each query is short; the cumulative "I am oriented" moment happens
across 3–5 queries in the first 30 minutes of shift.
```

**Errors:**
- Operational KB doesn't have the entry → "I don't have that for
  4-South — ask Devon (your charge tonight). I'll log this gap
  so it gets added to the unit's KB." (logged for KB curation)

**v3:** identical. Voice-only.

### Flow 4.3 — Marcus, charge-nurse unit handoff

**Surfaces used:** S1 voice command, S4 brain sheet (REQUIRED).

```
[S2 Home, NORMAL mode]
    │
    ├─ Wake word: "Give me a unit status for 4-South for handoff."
    │
[S1 Voice Command — Processing]
    │
    ├─ Router classifies: unit-status query
    ├─ Parallel FHIR fan-out across all 28 patients on 4-South
    │   (Encounter, Observation, MedicationAdministration,
    │    Procedure, DiagnosticReport)
    ├─ Operational KB pull: per-site handoff template (I-PASS /
    │   SBAR / local)
    │
[S4 Brain Sheet renders — Marcus sees full unit on screen]
    │
    ├─ Voice readback: top-line summary only ("28/32, 4 free, 3
    │   open issues, 2 NPO AM procedures, 2 discharges pending,
    │   1 ED admit holding")
    ├─ Marcus scans, edits one line manually (Garcia's prep
    │   actually incomplete)
    ├─ "Send to Anita" → exports as Epic-attached handoff doc OR
    │   shared S4 view to Anita's phone
    │
    └─ Returns to S2 Home
```

**Errors:**
- One or more FHIR queries time out → S4 shows partial data with
  "stale" badge per patient; voice readback names the gaps
  ("Couldn't refresh beds 7 and 12 — using last-known")
- Unit roster off (someone admitted but not yet rostered) →
  shows "1 patient missing from roster — bed 31, check assignment"

**v3:** the brain sheet doesn't fit on the v3 mini-display. Marcus
holds the phone for this flow; v3 badge does voice trigger + voice
readback only. The phone is the right surface for dense structured
output regardless of v3 hardware.

### Flow 4.4 — Jamal, sign-on summary

**Surfaces used:** S1 voice command, S4 brain sheet (REQUIRED;
scoped to 4-patient assignment).

```
[S9 Login completes → S2 Home, NORMAL mode]
    │
    ├─ Patient assignment auto-pulled in S9: beds 4, 7, 12, 19
    │
    ├─ Wake word: "Sign-on summary for my four patients."
    │
[S1 Voice Command — Processing]
    │
    ├─ Same fan-out as Flow 4.3, scoped to 4 beds
    ├─ Operational KB: per-shift cutover timestamp, sign-on
    │   template (brain sheet vs focus card)
    │
[S4 Brain Sheet renders — 4-patient scoped view]
    │
    ├─ Voice readback: prioritized 30-minute action list
    │   ("Verify oxycodone for bed 4 before 09:00; confirm bed 7's
    │    prep status before transport; bed 12 family meeting prep")
    ├─ Each action is tappable for detail
    │
    └─ Returns to S2 Home
```

**Errors:** same as Flow 4.3.

**v3:** same as Flow 4.3 — brain sheet needs the phone.

### Flow 4.5 — Tanya, refused-med policy lookup

**Surfaces used:** S1 voice command, S3 response card.

```
[S2 Home, NORMAL mode]
    │
    ├─ Wake word: "What's our policy for a patient refusing a
    │   scheduled cardiac med?"
    │
[S1 Voice Command — Processing]
    │
    ├─ Router classifies: policy query (vs FHIR vs drug-info vs
    │   Epic-doc). The "our policy" cue is the signal.
    ├─ Policy system query — hospital-specific
    ├─ Drug Info pull — addendum for "specifically metoprolol"
    │   if the patient context indicates beta-blocker
    │
[S1 Voice Command — Speaking + S3 Response Card]
    │
    ├─ Voice readback: full 5-step policy with metoprolol addendum
    ├─ S3 Card persists with the citation visible (NU-MED-027
    │   + Drug Info)
    ├─ Action affordance: "Chart this refusal" → opens Epic
    │   refusal-charting flow with policy reference pre-attached
    │   (deferred for v1.1; not in v1)
    │
    └─ Returns to S2 Home
```

**Errors:**
- Policy system doesn't have the policy → "I don't have a policy
  on this — ask Devon or check Policy Tech directly. I'll flag
  this for the hospital's KB team."
- Policy is over 12 months old without re-attestation → flags
  "policy last revised YYYY-MM-DD — confirm with charge" so Tanya
  doesn't act on a stale doc.

**v3:** identical voice flow; S3 card collapses to dose + policy
number on the v3 mini-display.

### Flow 4.6 — Robert, AI-tool routing

**Surfaces used:** S1 voice command, S3 response card with
prominent AI-source pill.

```
[S2 Home, NORMAL mode]
    │
    ├─ Wake word: "Is the new cipro okay with what Mr. Alvarez
    │   is already on?"
    │
[S1 Voice Command — Processing]
    │
    ├─ Router classifies: multi-source safety check
    ├─ Consult hospital AI registry (Operational KB extension)
    ├─ Registry returns: integrated nursing-reference AI
    │   (registry ID NU-AI-014) is the authority for this intent
    ├─ Query the integrated AI via documented API
    ├─ Parallel: pull Mr. Alvarez's active meds from FHIR
    │   MedicationRequest + last INR from Observation
    │
[S1 Voice Command — Speaking + S3 Response Card]
    │
    ├─ Voice readback NAMES the integrated AI:
    │   "Your hospital integrated a nursing clinical-reference AI
    │    into Epic last September — I'm using it for this answer.
    │    One interaction flagged: cipro inhibits warfarin
    │    metabolism..."
    ├─ S3 Card AI-source pill prominent at top:
    │   "Answered via [hospital nursing-reference AI]"
    ├─ Tap the AI-source pill: shows the registry entry — what
    │   the tool is, what it answers, when the hospital added it
    │   (the first-time UX moment)
    ├─ Action affordance: "Send note to anticoag pharmacy"
    │
    └─ Returns to S2 Home

[First-time-this-shift UX moment:]
    │
    ├─ The first time the AI-source pill names a tool the nurse
    │   has not seen LYNA route through before, an information
    │   card slides up:
    │   "New: your hospital has the [tool name] integrated for
    │    this kind of question. I'll use it automatically when
    │    relevant. Tap to learn what else it answers."
    ├─ One-time per nurse per tool. Acknowledgment logged.
```

**Errors:**
- Integrated AI unreachable → LYNA answers from native Drug Info
  + FHIR and says so explicitly ("Hospital reference AI
  unreachable; this answer is from LYNA's own Drug Info + Epic
  FHIR")
- AI registry says "this kind of question has no registered
  authority" → LYNA answers from its own knowledge with the same
  citation discipline

**v3:** the first-time UX card needs the phone (too long for the
v3 mini-display). The subsequent flow is voice-only on v3, with
the AI-source pill rendered as a glanceable badge.

### Flow 4.7 — Sofia, rapid response

**Surfaces used:** S1 voice command, S5 critical alert (REQUIRED).

```
[S2 Home, NORMAL mode]
    │
    ├─ Wake word: "Rapid response, bed 6, ST changes."
    │
[S1 Voice Command — emergency-intent path]
    │
    ├─ Router classifies: emergency intent (rapid response)
    ├─ Parallel fan-out (no operator confirmation — content IS
    │   authorization):
    │     - Overhead page
    │     - RRT direct page
    │     - On-call cardiology page
    │     - ACS protocol pull from Policy system
    │     - Patient FHIR pull (last 24h relevant Observations,
    │       active meds, troponin trend, allergies)
    │
[S5 Critical Alert — Sofia's phone]
    │
    ├─ Full-screen takeover
    ├─ Haptic + audio readback through earpiece:
    │   "Rapid response activated for 4-East bed 6 — overhead
    │    page sent, RRT 90s, cardiology paged. ACS protocol on
    │    screen. Troponin 0.08 positive..."
    ├─ S5 displays: protocol, last troponin, active orders,
    │   allergies, next-action checklist
    ├─ ACK button (single tap, glove-friendly) — confirms Sofia
    │   has the situation in hand
    ├─ Alert remains visible (status bar) until "End response"
    │
[Parallel: S5 Critical Alert — RRT members' phones]
    │
    ├─ Same full-screen takeover for each RRT member
    ├─ "4-East bed 6, ST changes — Sofia activated, ETA you 90s"
    ├─ ACK button — confirms they're en route
    │
[Event logged: timestamp 04:35:17]
```

**Errors:**
- One of the parallel pages fails → S5 shows the failed page in
  red ("Cardiology page failed — paged backup Dr. Patel
  automatically")
- Sofia doesn't ACK within 10s → escalates to a second-level
  alert (charge nurse pinged)

**v3:** the v3 badge gets haptic + audio + a single hardware ACK
button. Full protocol view escalates to the phone (Sofia still has
the phone in her pocket; the badge handles the "stop everything
and act" moment).

### Flow 4.8 — Priya, isolation-room broadcast

**Surfaces used:** S1 voice command, S6a broadcast composer
(sender), S6b receivers.

```
[S2 Home — sender's phone]
    │
    ├─ Mode pill could be NORMAL or BROADCAST — voice trigger
    │   recognizes either
    ├─ Wake word + content (gloved tap on badge if hands-free
    │   not possible):
    │   "Broadcast 4-South: I need a 10mL saline flush in 305,
    │    isolation."
    │
[S1 Voice Command — Processing]
    │
    ├─ Router classifies: broadcast-with-acknowledgment
    ├─ Execution-layer dispatch (no operator confirmation —
    │   content IS authorization for help broadcasts)
    │
[S6a Sender view]
    │
    ├─ 1.5s confirmation card: "Broadcasting to 4-South: 10mL
    │   saline flush to 305 (isolation tag)"
    ├─ Roster of recipients visible (4 RNs, 3 PCAs, 1 secretary
    │   currently on shift)
    │
[Parallel: S6b on each recipient's phone]
    │
    ├─ Non-modal banner at top of S2 Home
    ├─ Voice readback through earpiece:
    │   "Priya in 305 needs a 10mL saline flush — isolation.
    │    First available, please acknowledge."
    ├─ Single-tap ACK
    │
[Devon ACKs first]
    │
    ├─ S6a sender view updates: "Devon picking it up — 90 seconds"
    ├─ S6b receivers update: "Devon's got it" → auto-dismiss 3s
    ├─ Voice readback to Priya through her earpiece:
    │   "Devon is bringing your flush in 90 seconds."
    │
[Event logged: broadcast emit, attempts, winning ack, delivery]
```

**Errors:**
- No recipient ACKs within 30s → escalates to charge nurse
  ("No one on 4-South responded — escalating to Devon, charge")
- Sender cancels mid-broadcast → all recipients see "cancelled"
  and dismiss

**v3:** v3 badge has a dedicated broadcast hardware button (firm
tactile click for confirmation in noisy environments) — enters
S6a via voice immediately on press.

### Flow 4.9 — Aisha, pressure-injury photo handoff

**Surfaces used:** S1 voice command, S8 camera handoff banner,
Epic Haiku (external).

```
[S2 Home, NORMAL mode]
    │
    ├─ Wake word: "LYNA, document a pressure injury on bed 18."
    │
[S1 Voice Command — Processing]
    │
    ├─ Router classifies: camera-dependent intent
    ├─ Dispatch through phone-coexistence path
    ├─ Pre-fill: patient bed 18, sacral (if dictated), on-admission
    │   timestamp
    │
[S8 Camera Handoff Banner — Aisha's phone]
    │
    ├─ Banner: "Pressure-injury photo needs your phone camera —
    │   I've opened Haiku to bed 18, sacral, on-admission. Tap
    │   when ready to capture."
    ├─ Tap → SMART app launch into Haiku with context params
    │
[Epic Haiku takes over — outside LYNA's control]
    │
    ├─ Aisha captures overview + close-up + with staging ruler
    ├─ Haiku uploads photos to bed 18 encounter
    │
[FHIR DocumentReference subscription fires — back in LYNA]
    │
    ├─ S8 banner updates: "3 photos uploaded to bed 18,
    │   encounter ##. Stage not yet classified. Want me to walk
    │   you through staging, or dictate stage and note?"
    ├─ Voice option: "Stage 3, full-thickness, no slough or
    │   eschar visible, 3.4 by 2.1 cm"
    │
[S3 Response Card — wound note]
    │
    ├─ LYNA composes the structured wound-care note from the
    │   dictation against the Policy system's staging schema
    ├─ Reads back the note for confirmation
    ├─ Aisha: "Yes" → note filed in Epic with the photos attached
    │
    └─ Returns to S2 Home
```

**Errors:**
- Haiku not installed on this nurse's phone → S8 shows "Install
  Haiku from hospital MDM and try again" + link to the hospital's
  MDM page (does not deep-link the install, since MDM authorizes
  apps not LYNA)
- Photo upload doesn't fire FHIR event within 60s → S8 says
  "I don't see the upload — give it another minute or check
  Haiku" and remains open for resume
- Staging dictation is incomplete (e.g., no dimensions) → LYNA
  asks the missing field before composing the note

**v3:** v3 badge has no camera. The handoff still goes to the
phone (the phone is the camera in every form factor). v3 voice
trigger + phone handoff is the same.

### Flow 4.10 — Maya, interpreter mode

**Surfaces used:** S1 voice command, S7 interpreter mode
(REQUIRED — session mode, not query/response).

```
[S2 Home, NORMAL mode]
    │
    ├─ Wake word: "Interpreter mode, Spanish."
    │
[S1 Voice Command — session-mode entry]
    │
    ├─ Router classifies: session-mode change
    ├─ Voice pipeline reconfigures: bidirectional + translation
    │   path active
    │
[S7 Interpreter Mode — compliance moment]
    │
    ├─ Modal: "Machine translation for ad-hoc bedside
    │   clarification only. For consent, discharge teaching, or
    │   clinical decisions, certified interpreter required.
    │   'Queue interpreter' is available at any time."
    ├─ Tap "Got it" → logged
    │
[S7 Interpreter Mode — active session]
    │
    ├─ Dual-language indicator: "English ↔ Spanish (machine
    │   translation)"
    ├─ Patient-side audio: routes through phone speaker on the
    │   bedside tray
    │
    ├─ Maya speaks (earpiece pickup):
    │   "Mr. Reyes, are you having any pain right now?
    │    On a scale of 0 to 10."
    │
    ├─ LYNA translates → patient hears Spanish through phone speaker:
    │   "Sr. Reyes, ¿tiene dolor en este momento?
    │    En una escala del cero al diez."
    │
    ├─ Patient responds in Spanish (phone mic pickup):
    │   "Sí, como un siete. Aquí, en el pecho."
    │
    ├─ LYNA translates → Maya hears English through earpiece:
    │   "Yes, about a seven. Here, in the chest."
    │
    ├─ Per-turn transcript appears in S7 view (last 3 turns
    │   visible, scrollable history)
    │
[Maya ends session]
    │
    ├─ "End interpreter mode" or "LYNA, end interpreter"
    ├─ Voice confirms: "Interpreter session ended at 03:03.
    │   Logged."
    │
    └─ Returns to S2 Home (NORMAL mode)

[Event logged: session start, language, turn count, end, whether
'queue interpreter' was invoked]
```

**Errors:**
- Language not in the per-site coverage set → "I don't have
  certified interpreter coverage in {language} at this hospital —
  let me queue the certified interpreter service." Triggers the
  queue hand-off path.
- Sub-2s latency violated (network issue) → LYNA inserts
  "translating..." filler so the conversation pacing stays
  comfortable; if latency exceeds 5s, "I'm slower than usual on
  the network — let me queue the certified interpreter for you."
- Patient turn ambiguous (LYNA hears "Sí" alone with no context) →
  voices "Just 'yes' — was that the answer to the pain question?"

**v3:** session-mode framing identical. v3 routes patient-side
audio through a paired bedside earpiece (rather than the phone
speaker) for privacy in shared rooms.

---

## 3. Reusable patterns

Cross-cutting patterns that show up in multiple flows. Spec them
once here; reference from individual flows above.

### 3.1 Mode indicator + mode switching

Mode pill in S2 Home is ALWAYS visible:
- **NORMAL** (blue) — query/response default
- **BROADCAST** (orange) — voice utterances go through S6a
  broadcast composer
- **INTERPRETER** (purple) — session mode S7

Visual discipline:
- Blue = single-recipient (default)
- Orange = group / multi-recipient
- Purple = session-mode (bidirectional, ongoing)

Tap pill → mode-switcher sheet:
- Three options (NORMAL / BROADCAST / INTERPRETER)
- Group selector if BROADCAST is selected
- Language selector if INTERPRETER is selected

Modes are persistent until explicitly changed. Visual feedback on
mode change (brief 300ms flash) so the nurse never confuses what
mode she's in.

### 3.2 AI-source pill

Every S3 response card carries the AI-source pill. The pill
states the *source authority* for this specific answer:

- **Native** — LYNA's own indexed knowledge (Drug Info, Epic docs,
  Operational KB): rendered as "LYNA / source category"
- **Hospital-integrated AI** — surfaced from the hospital AI
  registry: rendered with the tool's registered name
- **Live FHIR** — pulled from Epic at query time: rendered as
  "Epic via FHIR — {resource}"
- **Hospital policy** — Policy system: rendered with the policy ID
- **Mixed** — multiple sources composed: rendered as a stack
  ("via X + Y")

The first time a nurse sees a hospital-integrated AI named, the
"new tool" awareness card appears (Flow 4.6 first-time UX).

### 3.3 Citation footer

Every S3 response card has a citation footer. Always specific
enough to be auditable:

- "Epic MAR via FHIR MedicationAdministration, 11:43 PM today"
- "Hospital policy NU-MED-027 (Refused Medication, revised
  2025-08-14) + Drug Info: metoprolol"
- "Hospital-integrated nursing-reference AI (registry ID NU-AI-014)
  + Epic FHIR MedicationRequest"

If LYNA falls back from a registered AI to its own knowledge, the
citation footer explicitly says so ("Hospital reference AI
unreachable — this answer is from LYNA's Drug Info + Epic FHIR").
**Never silent fallback.**

### 3.4 Voice-surface states

Standard four states for S1, every flow:

- **Idle** — wake word listening; quiet UI; battery + connectivity
  indicators only
- **Listening** — animated waveform; transcription preview updates
  in near-real-time; cancel affordance
- **Processing** — spinner + estimated latency ("~2s"); user can
  tap to cancel
- **Speaking** — readback through earpiece; tap to mute readback
  and read the response on screen instead; affordance to "say
  that again" or "show on screen"

State transitions are visible and audible (subtle audio cues at
each transition, configurable).

### 3.5 Wake word vs button-tap

The wake word ("Hey LYNA") is the primary input. The TALK button
is for:
- Noisy environments where the wake word doesn't reliably fire
- The nurse explicitly wants to push-to-talk for a private query
- Accessibility / glove behaviors that prefer tap over voice

Both routes enter the same S1 voice-command flow. No behavior
diverges.

### 3.6 Execution-layer affordances

LYNA can act, not just retrieve. Action affordances on S3
response cards:

- "Page X" — calls the hospital paging system with structured
  context
- "Send to {team}" — composes a templated message to a service
  (anticoag, pharmacy, dietary)
- "Chart this" — opens the relevant Epic flow with the LYNA
  answer pre-attached as a reference (v1.1; not v1.0)
- "Queue interpreter" — routes to hospital interpreter service

Discipline:
- **Routine actions need explicit confirmation.** Tap the
  affordance → "I'll page Dr. Chen now?" → confirm → action.
- **Emergency-intent actions (Flow 4.7) and broadcast-with-ack
  (Flow 4.8) don't.** The content of the request IS the
  authorization.
- **Camera handoff (Flow 4.9)** is not "execution" in the same
  sense — it's a context-pre-filled hand-off, not an autonomous
  action.

### 3.7 Compliance moments

Three moments where LYNA surfaces a compliance message:

- **Interpreter mode entry (Flow 4.10):** machine-translation
  scope disclaimer. Acknowledged once per session, logged.
- **First broadcast of a shift (Flow 4.8):** the broadcast is
  logged, the disclosure that broadcasts are logged is voiced once
  ("Broadcasts are logged with who-asked, who-covered, and
  delivery time. Helps your manager see when the unit is
  responsive.").
- **Critical alert activation (Flow 4.7):** the activation, the
  pages sent, the ACKs received, and the protocol viewed are all
  logged for the post-event review the hospital does on every
  rapid response.

Compliance moments are not modal interruptions in the working
flow — they're brief, voiced, and visible-once-then-dismissable.
The audit log is what compliance cares about; the on-screen
moment is just a courtesy notice.

---

## 4. Cross-cutting error handling

Across every flow:

### 4.1 Network errors
- **Phone offline:** S1 shows "Offline — I can't reach Epic right
  now" and offers the last-known cached unit/patient data (S4) if
  available, marked "stale since HH:MM." Queue retry-on-reconnect.
- **Slow network:** processing-state latency indicator goes
  orange at >3s, red at >5s, with "I'm slower than usual" voiced
  at the 5s threshold.

### 4.2 Voice recognition errors
- **Transcription confidence low:** S1 shows the transcribed text
  with a "didn't catch that — try again?" voiced prompt.
- **Persistent failure (3 attempts):** offer to type the query
  via S1 keyboard fallback.
- **Wake word missed in noise:** TALK button remains the
  always-available fallback.

### 4.3 Auth errors
- **Voiceprint doesn't match:** S1 voices "I don't recognize your
  voice — let me confirm by badge tap." Drops to S9 partial
  re-auth.
- **Session expired mid-shift:** S9 partial re-auth without
  re-pulling patient assignment.

### 4.4 Data errors
- **FHIR endpoint timeout:** S3 / S4 marks the affected fields
  "stale" with the last-known timestamp; voice readback names the
  gaps explicitly.
- **Patient identity mismatch (e.g., bed reassigned between
  query start and response):** LYNA refuses to render the
  response and voices "Bed 14 reassigned during my lookup — let
  me re-query."

### 4.5 Policy / safety errors
- **LYNA can't find the answer:** silent over wrong. "I don't have
  that documented — ask Devon (your charge) or check Policy Tech
  directly. I'll log this gap." Logged for the per-site KB
  curation work.

---

## 5. Cross-references to the existing design assets

The wireframes, screen designs, and design tokens in this
directory predate the v1 iPhone pivot and were drawn against the
v3 dedicated-device form factor. They remain valid reference for
the v3 pass and contain reusable design-system bones (color,
typography, spacing, component patterns).

- [`opal-ui-wireframes.md`](opal-ui-wireframes.md) — v3 device
  wireframes; the dashboard wireframes are partly applicable to
  the manager dashboard ([`manager-dashboard.md`](manager-dashboard.md))
- [`opal-design-system.md`](opal-design-system.md) — color
  palette, typography, spacing, components. **Reusable as-is for
  v1 iPhone.** Specifically: the mode-color scheme
  (blue/orange/purple — see §3.1 above) and the response-card
  pattern (see S3 above) carry forward.
- [`opal-screen-designs.md`](opal-screen-designs.md) — v3
  high-fidelity screens. Useful as visual reference for v3 pass.
- [`design-tokens.json`](design-tokens.json) — color, spacing,
  typography tokens. Reusable as-is for v1.
- [`implementation/`](implementation/) — HTML mockups, LVGL
  theme, React dashboard. **LVGL is v3-specific; HTML mockups
  and React dashboard are applicable to v1 (web view) and
  manager dashboard.**

A separate v3 design pass will re-anchor wireframes/screens
against the 10 journeys and the v3 hardware spec. Not in scope
here.

---

## 6. Deferred / out of scope for v1

- **v2 form factor** (Vocera-class wearable, Apple Watch) —
  intentionally skipped.
- **v3 dedicated LYNA badge** — separate design pass after v1
  pilot data.
- **Nurse-initiated documentation dictation** — old Flow 6
  (Voice-to-EMR Order) is reframed as a v1.1 capability. Within
  scope: dictating a wound-care note in Flow 4.9 (because LYNA
  composes against a policy-system template, not authoring
  free-text orders). Out of scope: ordering meds, ordering
  imaging, or any prescribing-flavored voice command. LYNA stays
  "Information OUT for nurses" at v1.
- **Settings / preferences detailed UX** — S10 surface
  acknowledged; detailed UX deferred.
- **Multi-language interpreter beyond launch set** — the
  per-site Operational KB declares which languages have certified
  in-house coverage; v1 launches with Spanish (highest patient-mix
  at the Mt. Sinai pilot site) and expands per-site.
- **Manager dashboard nurse-facing view** — managers and CNOs
  use the dashboard, not the nurses; see
  [`manager-dashboard.md`](manager-dashboard.md).

---

## 7. Update protocol for this file

This doc is the canonical v1 UX spec. Update when:
- A new journey lands in INTELLIGENCE_LAYER.md §4 (add a flow in
  §2)
- A reusable pattern emerges across 2+ journeys (add to §3)
- A surface inventory item changes (update §1)
- v3 design pass begins (add cross-references to the v3 spec doc;
  keep this doc v1-scoped)

Cross-check against:
- [`../../../../INTELLIGENCE_LAYER.md`](../../../../INTELLIGENCE_LAYER.md) §4 — must stay synchronized
- [`manager-dashboard.md`](manager-dashboard.md) — surface S8a
  dashboard cross-link
- [`opal-design-system.md`](opal-design-system.md) — design system
  is authoritative for color / typography / spacing

---

**Last updated:** 2026-05-20
**Supersedes:** 2025-11-19 8-flow draft (preserved in git history)
**Next pass:** v3 dedicated LYNA badge surfaces, after v1 pilot
data lands.
