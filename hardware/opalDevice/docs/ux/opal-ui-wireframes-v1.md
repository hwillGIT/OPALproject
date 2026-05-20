# LYNA v1 iPhone Wireframes

**Date:** 2026-05-20
**Form factor:** v1 — iPhone app (hospital-issued or BYOD) + Bluetooth earpiece
**Companion to:** [`opal-interaction-flows.md`](opal-interaction-flows.md)
(canonical v1 UX spec — read first for surface inventory + per-journey
flows)
**Design tokens:** [`opal-design-system.md`](opal-design-system.md)
+ [`design-tokens.json`](design-tokens.json) — reusable as-is

This doc renders the 10 surfaces (S1–S10) from
`opal-interaction-flows.md` as ASCII wireframes against the iPhone
viewport, then composes them into per-journey screen sequences for
each of the 10 LYNA clinical-staff journeys.

For pixel-perfect specs (dimensions, colors, typography), see
[`opal-screen-designs-v1.md`](opal-screen-designs-v1.md).

---

## 0. iPhone viewport assumptions

- **Target device:** iPhone 14 / 15 (390 × 844 pt, safe area
  insets accounted for in screen designs)
- **Orientation:** Portrait only. Critical alerts and brain sheet
  rotate to landscape on tablet form factors (Epic Haiku does the
  same).
- **Audio output:** Bluetooth earpiece primary; phone speaker
  fallback only. Patient-side audio (interpreter mode) routes
  through phone speaker on a bedside tray, or a paired bedside
  Bluetooth speaker if the site provides one.
- **Wake word:** "Hey LYNA" — always-on while the app is in
  foreground; backgrounded behavior governed by per-site policy
  (some hospitals disable background wake; respected via
  Operational KB flag).

---

## 1. S1 — Voice Command surface

Used by every journey. Four states (Idle, Listening, Processing,
Speaking), plus Error.

### S1.A — Idle (wake-word listening)

```
┌─────────────────────────────────┐
│ ●●● 9:41 AM           5G  ▣ 87% │ ← iOS status bar
├─────────────────────────────────┤
│                                 │
│   [LYNA]                ⚙       │ ← App header + settings affordance
│   Sarah M.                      │
│   4-South · Night Shift         │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Mode: NORMAL        ▼   │  │ ← Mode pill (blue). Tap → switcher
│   └─────────────────────────┘  │
│                                 │
│                                 │
│   Recent                        │
│   ──────                        │
│   • Pain med for bed 14         │ ← Recent queries (tap to re-ask /
│   • Door code med room          │   re-view cited response)
│   • Charge nurse tonight        │
│                                 │
│   Quick Actions                 │
│   ─────────────                 │
│   [📋 Brain sheet]              │ ← Quick affordances → S4, S6, S7
│   [📢 Broadcast]                │
│   [🌐 Interpreter]              │
│                                 │
│                                 │
│                                 │
│              ┌──────────┐       │
│              │  TALK    │       │ ← Large hold-to-talk button
│              │   🎤     │       │   (glove-friendly)
│              └──────────┘       │
│   "Hey LYNA" — always listening │ ← Wake-word indicator
└─────────────────────────────────┘
```

**Touch targets:** TALK button ≥88×88pt for gloved hands. Mode
pill ≥44×44pt. Recent queries ≥44pt row height.

### S1.B — Listening (active capture)

```
┌─────────────────────────────────┐
│ ●●● 9:41 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   ◀ Cancel                      │ ← Cancel affordance always visible
│                                 │
│                                 │
│      ╱╲    ╱╲    ╱╲             │ ← Animated waveform (height responds
│     ╱  ╲  ╱  ╲  ╱  ╲            │   to mic input level)
│    ╱    ╲╱    ╲╱    ╲           │
│                                 │
│                                 │
│   Listening...                  │ ← State label, voiced once on entry
│                                 │
│   ┌─────────────────────────┐  │
│   │ "what's the last pain   │  │ ← Live transcription preview
│   │  med for bed fourteen"  │  │   (updates as recognized)
│   └─────────────────────────┘  │
│                                 │
│                                 │
│                                 │
│              ┌──────────┐       │
│              │  STOP    │       │ ← Tap to commit
│              │   ⏹      │       │
│              └──────────┘       │
└─────────────────────────────────┘
```

**Behavior:**
- Auto-commits after 1.2s of silence
- Tap STOP to commit immediately
- Cancel returns to S1.A with no event logged

### S1.C — Processing

```
┌─────────────────────────────────┐
│ ●●● 9:41 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   ◀ Cancel                      │
│                                 │
│                                 │
│            ◌                    │ ← Spinner
│           ◌ ◌                   │
│            ◌                    │
│                                 │
│   Processing...    ~2s          │ ← Latency estimate
│                                 │
│   ┌─────────────────────────┐  │
│   │ "What's the last pain   │  │ ← Confirmed transcription
│   │  med for bed 14?"       │  │
│   └─────────────────────────┘  │
│                                 │
│   Querying: Epic MAR via FHIR   │ ← What LYNA is doing right now
│                                 │
│                                 │
│                                 │
└─────────────────────────────────┘
```

**Behavior:**
- Latency indicator: green <2s, orange 2–5s, red >5s
- At 5s: voice fallback "I'm slower than usual on the network"
- At 10s: auto-cancel with retry affordance

### S1.D — Speaking (response readback)

```
┌─────────────────────────────────┐
│ ●●● 9:41 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   ◀ Done             🔇 Mute    │ ← Mute readback; read on screen
│                                 │
│                                 │
│         🔊 ))) ))) )))          │ ← Speaker icon animates with TTS
│                                 │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Mrs. Reynolds, bed 14   │  │ ← Live transcript of LYNA's
│   │ Last hydromorphone      │  │   response (synced with audio)
│   │ 0.5 mg IV at 11:43 PM   │  │
│   │ ~2.5 hours ago. PRN q3h │  │
│   │ Due in 30 min.          │  │
│   └─────────────────────────┘  │
│                                 │
│   Citation:                     │
│   Epic MAR via FHIR             │ ← Persistent citation footer
│   Observation                   │
│                                 │
│   [Say it again] [Show on card]│ ← Affordances
└─────────────────────────────────┘
```

**Behavior:**
- Mute → response continues on-screen, audio stops
- "Show on card" → transitions to S3 Response Card (full body view)
- Auto-returns to S1.A 5s after readback completes

### S1.E — Error states

```
┌─────────────────────────────────┐
│ ●●● 9:41 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   ◀ Cancel                      │
│                                 │
│   ⚠ Offline                     │
│                                 │
│   I can't reach Epic right now. │
│   The workstation in the        │
│   corridor has the MAR.         │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Retry when reconnected  │  │
│   └─────────────────────────┘  │
│                                 │
│   Last known data available:    │ ← Shows cached S4 if applicable
│   • Brain sheet (06:42 AM)     │
│   • Unit on-call roster         │
│                                 │
└─────────────────────────────────┘
```

---

## 2. S2 — Home / Mode Indicator

Already wireframed as S1.A (Home and Idle voice surface are the
same screen). The mode pill drives navigation to the mode
switcher.

### S2.A — Mode switcher (modal)

```
┌─────────────────────────────────┐
│ ●●● 9:41 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│                                 │
│   ✕ Close                       │
│                                 │
│   Select mode                   │
│   ───────────                   │
│                                 │
│   ┌─────────────────────────┐  │
│   │ ● NORMAL                │  │ ← Currently selected (blue dot)
│   │   Single-recipient      │  │
│   │   queries & answers     │  │
│   └─────────────────────────┘  │
│                                 │
│   ┌─────────────────────────┐  │
│   │ ○ BROADCAST    [Select  │  │ ← Tap → group selector below
│   │   Help requests to      │  │
│   │   the whole unit        │  │
│   │   Group: ──────────  ▼  │  │
│   └─────────────────────────┘  │
│                                 │
│   ┌─────────────────────────┐  │
│   │ ○ INTERPRETER  [Select  │  │ ← Tap → language selector below
│   │   Bidirectional         │  │
│   │   ad-hoc translation    │  │
│   │   Language: ────────  ▼ │  │
│   └─────────────────────────┘  │
│                                 │
└─────────────────────────────────┘
```

---

## 3. S3 — Response Card

Used for any query that returns a discrete structured answer.

### S3.A — Standard response card

```
┌─────────────────────────────────┐
│ ●●● 9:41 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   ◀ Back                        │
│                                 │
│   ┌─────────────────────────┐  │
│   │ ❝ What's the last pain  │  │ ← Echo of the question
│   │   med for bed 14?       │  │
│   └─────────────────────────┘  │
│                                 │
│   Mrs. Reynolds, bed 14         │
│                                 │
│   Last dose:                    │
│   ▸ Hydromorphone 0.5 mg IV     │ ← Bold key value
│   ▸ 11:43 PM — 2.5 hours ago    │
│                                 │
│   Next dose:                    │
│   ▸ Available in 30 minutes     │ ← Bold key value
│   ▸ PRN q3h; sooner needs MD    │
│                                 │
│   ┌─────────────────────────┐  │
│   │ 🧠 LYNA · Epic FHIR     │  │ ← AI-source pill (S3.B detail)
│   └─────────────────────────┘  │
│                                 │
│   Source: Epic MAR via          │ ← Citation footer
│   FHIR Observation              │   (always present)
│   Pulled 09:41:12               │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Chart this              │  │ ← Execution-layer affordance
│   └─────────────────────────┘  │   (deferred v1.1)
│                                 │
└─────────────────────────────────┘
```

### S3.B — Response card with hospital AI-source pill (Flow 4.6)

```
┌─────────────────────────────────┐
│ ●●● 9:41 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   ◀ Back                        │
│                                 │
│   ┌─────────────────────────┐  │
│   │ ❝ Is the new cipro okay │  │
│   │   with what Mr. Alvarez │  │
│   │   is already on?        │  │
│   └─────────────────────────┘  │
│                                 │
│   ┌─────────────────────────┐  │
│   │ ⚡ Answered via your    │  │ ← AI-source pill (prominent,
│   │   hospital's nursing    │  │   colored for awareness)
│   │   reference AI    ⓘ →   │  │   Tap ⓘ → registry detail (S3.C)
│   └─────────────────────────┘  │
│                                 │
│   ⚠ One interaction flagged    │
│                                 │
│   Cipro inhibits warfarin       │
│   metabolism. INR can rise      │
│   over 3–5 days.                │
│                                 │
│   Last INR (2026-05-14): 2.4    │
│   ▸ In range.                   │
│                                 │
│   Recommendation:               │
│   ▸ Recheck INR at 48h          │
│   ▸ Routine note to anticoag    │
│                                 │
│   No allergies. No renal-dose   │
│   adjustment needed             │
│   (creatinine 1.1).             │
│                                 │
│   Source: Hospital nursing      │ ← Multi-source citation
│   reference AI (ID NU-AI-014)   │
│   + Epic FHIR MedicationRequest │
│   + Observation                 │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Send note to anticoag   │  │
│   └─────────────────────────┘  │
│                                 │
└─────────────────────────────────┘
```

### S3.C — First-time AI-tool exposure card (slides up from S3.B)

```
┌─────────────────────────────────┐
│                                 │
│   New for you!                  │
│                                 │
│   Your hospital has the         │
│   nursing reference AI          │
│   integrated for this kind of   │
│   safety check.                 │
│                                 │
│   I'll route through it         │
│   automatically when it's the   │
│   right tool for the question.  │
│                                 │
│   What else it answers:         │
│   • Drug-drug interactions      │
│   • Renal/hepatic dose checks   │
│   • Pregnancy/lactation         │
│   • Geriatric dosing            │
│                                 │
│   Added by NI team: Sep 2025    │
│   Vendor: [vendor name]         │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Got it                  │  │ ← Tap to dismiss; logged
│   └─────────────────────────┘  │
│                                 │
└─────────────────────────────────┘
```

**Behavior:** appears one-time-per-nurse-per-tool. Dismissal
logged. Re-accessible from S10 settings if the nurse wants to
review what tools her hospital has registered.

---

## 4. S4 — Patient/Unit Brain Sheet

Two variants — full unit (Marcus §4.3, ~28 patients) and assigned
patients (Jamal §4.4, 4 patients).

### S4.A — Unit brain sheet (Marcus, §4.3)

```
┌─────────────────────────────────┐
│ ●●● 6:42 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   ◀ Back              ↻ Refresh │
│                                 │
│   4-South · Unit Status         │
│   Data current as of 06:42 AM   │
│   ────────────────────────────  │
│                                 │
│   28/32 occupied · 4 free       │ ← Top KPI strip
│                                 │
│   ┌─────────────────────────┐  │
│   │ 🔴 Open clinical issues │  │
│   │                         │  │
│   │ Bed 4 · Cruz, J. (67M)  │  │ ← Each patient: bed + name + age
│   │   Pain not controlled;  │  │   + one-line summary
│   │   PRN 4× last 04:20;    │  │
│   │   pain service noted    │  │
│   │   06:32                  │  │
│   │   ▸ Tap for detail      │  │
│   │                         │  │
│   │ Bed 18 · Patel, A. (52F)│  │
│   │   Temp 38.9 at 02:15;   │  │
│   │   cultures drawn;       │  │
│   │   q4h vitals; broad     │  │
│   │   spectrum              │  │
│   │   ▸ Tap for detail      │  │
│   │                         │  │
│   │ Bed 22 · Williams, R.   │  │
│   │   Fall this shift;      │  │
│   │   IR filed; q1h neuro   │  │
│   │   ▸ Tap for detail      │  │
│   └─────────────────────────┘  │
│                                 │
│   ┌─────────────────────────┐  │
│   │ 🍽 NPO — AM procedures  │  │
│   │                         │  │
│   │ Bed 7  · Garcia, M.     │  │
│   │   Colonoscopy 08:00     │  │
│   │   ⚠ Prep INCOMPLETE     │  │ ← Marcus's manual edit (red flag)
│   │   (per bowel-prep nurse,│  │
│   │    23:40)               │  │
│   │                         │  │
│   │ Bed 19 · Chen, K.       │  │
│   │   Cardiac cath 09:30    │  │
│   │   ✓ Consent obtained    │  │
│   └─────────────────────────┘  │
│                                 │
│   ┌─────────────────────────┐  │
│   │ 🏠 Pending discharge    │  │
│   │ Bed 11 · Roberts, T.    │  │
│   │   Transport 11:00 ✓     │  │
│   │ Bed 25 · Liu, S.        │  │
│   │   PT clearance pending  │  │
│   └─────────────────────────┘  │
│                                 │
│   ┌─────────────────────────┐  │
│   │ 🚑 Pending admits       │  │
│   │ ED: 1 (chest pain r/o)  │  │
│   │ → bed 4 once repositd   │  │
│   └─────────────────────────┘  │
│                                 │
│   Citations: Epic 06:42 AM      │
│   + unit board cross-check      │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Send to Anita →         │  │ ← Export to incoming charge
│   └─────────────────────────┘  │
│                                 │
└─────────────────────────────────┘
```

**Behavior:**
- Pull-to-refresh re-fires the FHIR fan-out
- Per-patient tap → full per-patient detail view (same shape as
  Sarah's S3 bedside view but for the whole patient)
- "Stale" badge per patient if their query failed; voice readback
  names the gaps
- "Send to Anita" → exports as Epic-attached handoff doc OR shares
  S4 view to Anita's phone (Mt. Sinai's choice per pilot config)

### S4.B — Assignment brain sheet (Jamal, §4.4)

```
┌─────────────────────────────────┐
│ ●●● 7:05 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   ◀ Back              ↻ Refresh │
│                                 │
│   Jamal's 4 patients · 4-South  │
│   Sign-on at 07:05              │
│   ────────────────────────────  │
│                                 │
│   ⚡ Next 30 minutes             │ ← Sticky priority list, voiced
│   ─────────────────             │   in readback
│   1. ☐ Verify oxycodone for     │
│      bed 4 before 09:00         │
│   2. ☐ Confirm bed 7's prep     │
│      status with GI             │
│   3. ☐ Bed 12 family meeting    │
│      prep (10 AM)               │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Bed 4 · Cruz, J. (67M)  │  │ ← Per-patient card
│   │ Day 3 post-CABG         │  │
│   │                         │  │
│   │ ⚠ Pain not controlled   │  │
│   │   PRN 4× overnight per  │  │
│   │   Sarah's handoff       │  │
│   │   New order: oxycodone  │  │
│   │   5mg q6h (pending      │  │
│   │   pharmacy)             │  │
│   │   Watch: resp rate,     │  │
│   │   oversedation           │  │
│   │   ▸ Tap for full view   │  │
│   └─────────────────────────┘  │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Bed 7 · Garcia, M. (54F)│  │
│   │ NPO since midnight      │  │
│   │ Colonoscopy 08:00       │  │
│   │ ⚠ Prep incomplete       │  │
│   │   GI team aware         │  │
│   │   ▸ Tap for full view   │  │
│   └─────────────────────────┘  │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Bed 12 · Whitfield, A.  │  │
│   │ ESRD on HD              │  │
│   │ Dialysis today 13:00    │  │
│   │ K+ 5.1 yesterday        │  │
│   │ Family meeting 10 AM    │  │
│   │   ▸ Tap for full view   │  │
│   └─────────────────────────┘  │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Bed 19 · Chen, K. (72M) │  │
│   │ Cardiac cath 09:30      │  │
│   │ ✓ Consent · ✓ NPO       │  │
│   │ No overnight events     │  │
│   │   ▸ Tap for full view   │  │
│   └─────────────────────────┘  │
│                                 │
└─────────────────────────────────┘
```

---

## 5. S5 — Critical Alert (full screen)

Highest-priority surface in the app. Preempts everything.

### S5.A — Incoming alert (Sofia or RRT member)

```
┌─────────────────────────────────┐
│                                 │ ← Red gradient background
│        🚨 RAPID RESPONSE        │   #FFEAEC base, pulsing border
│                                 │
│         4-East · Bed 6          │
│                                 │
│         Mr. Hernandez · 68M     │
│         Day 2 post-CABG         │
│                                 │
│      HR 130 · new ST↓ II,aVF    │
│      Diaphoretic, chest pain    │
│                                 │
│      Last troponin 0.08 (+)     │
│      ASA 81 mg yesterday 06:00  │
│      Heparin SC 5000u 04:00     │
│      No ASA allergy             │
│                                 │
│                                 │
│      ┌─────────────────────┐   │
│      │                     │   │
│      │   ✓ ACKNOWLEDGE     │   │ ← Single big button
│      │                     │   │   Min 88×88pt
│      └─────────────────────┘   │
│                                 │
│      [View Protocol]            │ ← ACS protocol from Policy system
│      [View Vitals]              │ ← Last 1h Observation data
│                                 │
│      Activated 04:35:17         │
│                                 │
└─────────────────────────────────┘
```

**Behavior:**
- Haptic: strong, escalating pattern (1s on, 0.5s off, then 1.5s
  on, 0.5s off, etc.) until ACK or 30s timeout
- Audio: alarm tone + voice readback through earpiece
- ACK timeout 10s → escalates to second-tier (charge nurse pinged)
- After ACK: alert moves to status-bar pill, no longer modal,
  but persists until "End response"

### S5.B — Active alert in status bar (post-ACK)

```
┌─────────────────────────────────┐
│ ●●● 4:36 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   🔴 RR active · 4-East bed 6   │ ← Sticky banner, tappable to
│      Tap to expand              │   re-open S5.A
├─────────────────────────────────┤
│   (rest of S2 Home or whatever  │
│    nurse was doing)             │
│                                 │
└─────────────────────────────────┘
```

### S5.C — Protocol view (drill-down from S5.A)

```
┌─────────────────────────────────┐
│ ●●● 4:36 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   ◀ Back to alert               │
│                                 │
│   ACS Protocol                  │
│   ─────────────                 │
│                                 │
│   Per hospital protocol         │
│   NU-CARD-014 (revised          │
│   2025-11-02):                  │
│                                 │
│   1. ✓ Activate RRT             │ ← Items checked as Sofia / team
│   2. ✓ Page cardiology          │   completes them
│   3. ☐ Establish 2nd IV         │
│      (large bore)               │
│   4. ☐ 12-lead EKG              │
│   5. ☐ Recheck troponin         │
│   6. ☐ Prepare for possible     │
│      cath lab activation        │
│                                 │
│   Source: Hospital policy       │
│   NU-CARD-014                   │
│                                 │
└─────────────────────────────────┘
```

---

## 6. S6 — Broadcast Composer + Ack Tracker

Splits into sender (S6a) and receivers (S6b).

### S6a — Sender, after broadcast emit (Priya §4.8)

```
┌─────────────────────────────────┐
│ ●●● 9:21 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   ◀ Cancel broadcast            │
│                                 │
│   📢 Broadcasting · 4-South     │
│                                 │
│   ┌─────────────────────────┐  │
│   │ I need a 10mL saline    │  │ ← Echo of the broadcast content
│   │ flush in 305, isolation │  │
│   └─────────────────────────┘  │
│                                 │
│   Sent 09:20:14                 │
│                                 │
│   Waiting for ack ...           │
│   ┌─────────────────────────┐  │
│   │ 7 recipients reached    │  │
│   │ ─────────────────────── │  │
│   │ ○ Maya  RN              │  │
│   │ ○ Tanya RN              │  │ ← Roster + ack state (●/○)
│   │ ○ Linh  RN              │  │
│   │ ○ Devon PCA             │  │
│   │ ○ Carlos PCA            │  │
│   │ ○ Yvonne Secretary      │  │
│   └─────────────────────────┘  │
│                                 │
│                                 │
└─────────────────────────────────┘
```

### S6a — Sender, after first ack

```
┌─────────────────────────────────┐
│ ●●● 9:21 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   ◀ Back                        │
│                                 │
│   📢 Broadcast covered          │
│                                 │
│   ┌─────────────────────────┐  │
│   │ ✓ Devon picking it up   │  │
│   │   ETA 90 seconds        │  │
│   │   Iso-room: gowning     │  │
│   └─────────────────────────┘  │
│                                 │
│   You'll hear voice confirm     │
│   when he's en route.           │
│                                 │
│   Logged 09:20:17               │
│                                 │
│                                 │
└─────────────────────────────────┘
```

### S6b — Receiver (non-modal banner on S2 Home)

```
┌─────────────────────────────────┐
│ ●●● 9:20 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│ 📢 Priya · 305 (iso)            │ ← Banner at top of any screen,
│ Needs 10mL saline flush         │   dismissible
│ ┌──────────────┬──────────────┐ │
│ │ Acknowledge  │ Pass         │ │ ← Single-tap ack
│ └──────────────┴──────────────┘ │
├─────────────────────────────────┤
│   (rest of S2 Home)             │
│                                 │
└─────────────────────────────────┘
```

**Behavior:**
- Voice readback through earpiece concurrent with banner
- First-tap-wins; other recipients see "Devon's got it" and
  banner auto-dismisses after 3s
- "Pass" lets the recipient explicitly opt out (e.g., they're in
  a patient room with hands full); logged

---

## 7. S7 — Interpreter Mode (bidirectional session)

Session mode, not query/response.

### S7.A — Compliance entry modal (Maya §4.10)

```
┌─────────────────────────────────┐
│ ●●● 3:00 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│                                 │
│   🌐 Interpreter mode           │
│                                 │
│   I'll machine-translate        │
│   between English and Spanish.  │
│                                 │
│   Use this for ad-hoc bedside   │
│   clarification only.           │
│                                 │
│   For consent, discharge        │
│   teaching, or clinical         │
│   decisions, you need a         │
│   certified interpreter.        │
│                                 │
│   ▸ Say "queue interpreter"     │
│     at any time and I'll        │
│     route you to the hospital   │
│     interpreter service.        │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Got it                  │  │ ← Acknowledged; logged
│   └─────────────────────────┘  │
│                                 │
└─────────────────────────────────┘
```

### S7.B — Active session (after entry)

```
┌─────────────────────────────────┐
│ ●●● 3:02 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   ◀ End interpreter             │
│                                 │
│   🌐 English ⇄ Spanish          │
│   Machine translation · ad-hoc  │
│                                 │
│   Patient audio: 🔊 phone speaker│
│                                 │
│   ─────────────────────────     │
│                                 │
│   ● You (English):              │ ← Pulsing dot = active speaker
│   "Mr. Reyes, are you having    │
│    any pain right now? On a     │
│    scale of 0 to 10."           │
│                                 │
│   ○ Patient (Spanish):          │
│   "Sí, como un siete.           │
│    Aquí, en el pecho."          │
│                                 │
│   You (English):                │
│   ↳ "Yes, about a seven.        │
│      Here, in the chest."       │
│                                 │
│   ─────────────────────────     │
│                                 │
│   Turn 4 · Session 02:18        │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Queue certified         │  │ ← Hand off to interpreter line
│   │ interpreter             │  │
│   └─────────────────────────┘  │
│                                 │
└─────────────────────────────────┘
```

**Behavior:**
- Last 3 turns visible, scrollable history
- Active-speaker indicator (pulsing ● vs static ○) for each
  language
- Patient-side audio routes through phone speaker on bedside tray
- "End interpreter" → S2 Home; "Queue certified interpreter" →
  routes to hospital queue while LYNA continues translating in
  the interim

---

## 8. S8 — Camera Handoff Banner

Used by Aisha §4.9.

### S8.A — Initial handoff (banner on S2 Home)

```
┌─────────────────────────────────┐
│ ●●● 10:40 AM          5G  ▣ 87% │
├─────────────────────────────────┤
│ 📸 Wound photo needs your camera│ ← Banner at top
│ I've opened Haiku for bed 18,   │
│ sacral, on-admission.           │
│ ┌─────────────────────────────┐ │
│ │ Open Haiku →                │ │ ← SMART app launch with context
│ └─────────────────────────────┘ │
├─────────────────────────────────┤
│   (rest of S2 Home)             │
│                                 │
└─────────────────────────────────┘
```

### S8.B — After Haiku upload (banner updates)

```
┌─────────────────────────────────┐
│ ●●● 10:43 AM          5G  ▣ 87% │
├─────────────────────────────────┤
│ ✓ 3 photos uploaded · bed 18    │ ← Banner update after FHIR
│ Stage not yet classified.       │   DocumentReference event
│ Want to dictate the note?       │
│ ┌──────────────┬──────────────┐ │
│ │ Dictate now  │ Later        │ │
│ └──────────────┴──────────────┘ │
├─────────────────────────────────┤
│   (rest of S2 Home)             │
│                                 │
└─────────────────────────────────┘
```

### S8.C — Dictation flow (returns to S1.B/D)

After "Dictate now," LYNA enters S1.B Listening:

> Aisha: "Stage 3, full-thickness, no slough or eschar visible,
> 3.4 by 2.1 cm."

Then S1.D Speaking with the composed wound-care note read back
for confirmation, then S3 Response Card shows the filed note.

---

## 9. S9 — Login / Shift Start

Once per shift, drops into S2 Home on completion.

### S9.A — Badge tap / PIN

```
┌─────────────────────────────────┐
│ ●●● 6:55 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│                                 │
│   Welcome to LYNA               │
│                                 │
│                                 │
│       👤                        │
│   Tap your badge                │ ← Camera-based badge scan OR
│   to sign in                    │   NFC if available
│                                 │
│   ─── or ───                    │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Enter PIN               │  │
│   └─────────────────────────┘  │
│                                 │
│                                 │
└─────────────────────────────────┘
```

### S9.B — Voiceprint check

```
┌─────────────────────────────────┐
│ ●●● 6:56 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│                                 │
│   Hello, Sarah                  │
│                                 │
│   Quick voice check —           │
│   tap and read this aloud:      │
│                                 │
│   ┌─────────────────────────┐  │
│   │ "The quick brown fox    │  │
│   │  jumps over the lazy    │  │
│   │  dog at four-South      │  │
│   │  this morning."         │  │
│   └─────────────────────────┘  │
│                                 │
│      ┌──────────┐               │
│      │  RECORD  │               │
│      │   🎤     │               │
│      └──────────┘               │
│                                 │
└─────────────────────────────────┘
```

### S9.C — Patient assignment confirmation

```
┌─────────────────────────────────┐
│ ●●● 6:58 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│                                 │
│   You're on 4-South tonight     │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Your patients:          │  │
│   │ ── Bed 4 · Cruz, J.     │  │
│   │ ── Bed 7 · Garcia, M.   │  │
│   │ ── Bed 12 · Whitfield   │  │
│   │ ── Bed 19 · Chen, K.    │  │
│   └─────────────────────────┘  │
│                                 │
│   Mode at shift start:          │
│   ● NORMAL                      │
│   ○ BROADCAST (pre-set)         │
│                                 │
│   ┌─────────────────────────┐  │
│   │ Ready                   │  │ ← → S2 Home
│   └─────────────────────────┘  │
│                                 │
└─────────────────────────────────┘
```

---

## 10. S10 — Settings / Preferences

Brief wireframe (rare use).

```
┌─────────────────────────────────┐
│ ●●● 9:41 AM           5G  ▣ 87% │
├─────────────────────────────────┤
│   ◀ Back                        │
│                                 │
│   Settings                      │
│   ────────                      │
│                                 │
│   Voice                         │
│   ──────                        │
│   Wake word        "Hey LYNA" > │
│   Earpiece         AirPods Pro >│
│   Voice volume     ─────●────── │
│                                 │
│   Modes                         │
│   ──────                        │
│   Default mode     NORMAL    >  │
│   Interpreter lang Spanish   >  │
│                                 │
│   Privacy                       │
│   ───────                       │
│   My queries log              > │
│   Compliance audit            > │
│                                 │
│   ──────                        │
│   Sign out                      │
└─────────────────────────────────┘
```

---

## 11. Per-journey screen sequences

Each journey composes 2–4 surfaces. Sequences below name surfaces
used in order.

### Journey 4.1 — Sarah, bedside pain-med lookup

```
S2 Home (Idle, NORMAL mode)
  → wake word
S1.B Listening
  → auto-commit after silence
S1.C Processing (~2s)
  → answer ready
S1.D Speaking (response read through earpiece)
  → auto-return after readback
S2 Home (with the query in Recent)
```

Optional: from S1.D, tap "Show on card" → S3.A persists.

### Journey 4.2 — Linh, float onboarding queries

```
S9 Login completes
  → S2 Home (Idle, NORMAL mode)
  → "Where are the sterile dressings?"
S1.B → S1.C → S1.D
  → S2 Home
  → "Med-room door code?"
S1.B → S1.C → S1.D
  → ... (repeat 3-5 times)
```

### Journey 4.3 — Marcus, charge handoff

```
S2 Home (Idle, NORMAL mode)
  → "Give me a unit status for 4-South for handoff"
S1.B → S1.C (~8s — parallel FHIR fan-out across 28 patients)
S4.A Unit brain sheet (top-line voiced; full visual on screen)
  → Marcus reviews, taps to edit Garcia's prep status
  → "Send to Anita" → exports
S2 Home
```

### Journey 4.4 — Jamal, sign-on summary

```
S9 Login completes
  → S2 Home (Idle, NORMAL mode)
  → "Sign-on summary for my four patients"
S1.B → S1.C (~10s)
S4.B Assignment brain sheet (priority list voiced; full view on
   screen)
  → Jamal taps to check off the 3 priorities as he handles them
S2 Home (still with brain sheet in Recent, re-openable)
```

### Journey 4.5 — Tanya, refused-med policy lookup

```
S2 Home (NORMAL mode)
  → "What's our policy for a patient refusing a scheduled cardiac
     med?"
S1.B → S1.C → S1.D (voice readback)
  + S3.A Response Card persists with the policy number cited
  → Tanya goes back into the room, charts the refusal
S2 Home
```

### Journey 4.6 — Robert, AI-tool routing

```
S2 Home (NORMAL mode)
  → "Is the new cipro okay with what Mr. Alvarez is already on?"
S1.B → S1.C → S1.D (voice readback NAMES the integrated AI)
  + S3.B Response Card with prominent AI-source pill
[FIRST TIME THIS NURSE SEES THIS TOOL]
  → S3.C First-time exposure card slides up
  → Robert taps "Got it"; logged
  → S3.B persists with action affordance "Send note to anticoag"
  → Robert taps the affordance, confirms
S2 Home
```

### Journey 4.7 — Sofia, rapid response

```
S2 Home (NORMAL mode)
  → "Rapid response, bed 6, ST changes"
S1.B → S1.C (~3s — parallel pages + FHIR pulls)
S5.A Critical Alert — FULL SCREEN TAKEOVER
  → Haptic, voice readback, full info on screen
  → Sofia taps ACK
S5.B Status-bar banner (post-ACK)
  → Sofia can issue more voice commands while alert is active
  → "View Protocol" → S5.C; checks items off as team completes
[RRT members get same S5.A treatment in parallel on their phones]
[RRT members tap ACK]
  → Sofia's S5.A receives updates ("RRT: 3 acknowledged, en route")
  → Once situation resolves: Sofia "End response"
S2 Home
```

### Journey 4.8 — Priya, isolation-room broadcast

```
S2 Home (mode could be NORMAL or pre-set BROADCAST)
  → "Broadcast 4-South: I need a 10mL saline flush in 305,
     isolation"
S1.B → S1.C (~1.5s)
S6a Broadcast composer with confirmation card
  → roster + waiting-for-ack view
[On every recipient's phone]
  → S6b non-modal banner with ack/pass affordances
  → Devon taps "Acknowledge"
S6a updates to "Devon picking it up, ETA 90s"
  → voice readback to Priya through her earpiece
  → other recipients see "Devon's got it" and dismiss
[After 90s, Devon arrives — manual; no LYNA prompt needed]
S2 Home for everyone
```

### Journey 4.9 — Aisha, pressure-injury photo handoff

```
S2 Home (NORMAL mode)
  → "LYNA, document a pressure injury on bed 18"
S1.B → S1.C
S8.A Camera handoff banner appears on S2 Home
  → Aisha taps "Open Haiku →"
[Haiku takes over — Aisha captures 3 photos]
[FHIR DocumentReference subscription fires back in LYNA]
S8.B Banner updates: photos uploaded; dictate now?
  → Aisha taps "Dictate now"
S1.B → S1.D (LYNA composes wound note from dictation)
  + S3.A Response Card showing the filed note for confirmation
  → Aisha says "Yes" → note files in Epic
S2 Home
```

### Journey 4.10 — Maya, interpreter session

```
S2 Home (NORMAL mode)
  → "Interpreter mode, Spanish"
S1.C session-mode entry
S7.A Compliance modal
  → Maya taps "Got it"
S7.B Active session
  → Maya speaks English (earpiece pickup)
  → LYNA translates to Spanish through phone speaker on bedside
  → Patient speaks Spanish (phone mic pickup)
  → LYNA translates to English through Maya's earpiece
  → ~5 turns; S7.B updates each turn
  → Maya: "End interpreter"
S2 Home (NORMAL mode restored)
```

---

## 12. Cross-references

- [`opal-interaction-flows.md`](opal-interaction-flows.md) — canonical
  spec for what these surfaces do and why
- [`opal-screen-designs-v1.md`](opal-screen-designs-v1.md) —
  pixel-perfect specs for the surfaces wireframed here
- [`opal-design-system.md`](opal-design-system.md) — color,
  typography, spacing, components (reusable as-is)
- [`design-tokens.json`](design-tokens.json) — design tokens
  (reusable as-is)
- [`opal-ui-wireframes.md`](opal-ui-wireframes.md) — **v3
  reference** (dedicated-device target, predates I-Corps work)
- [`v3-design-alignment.md`](v3-design-alignment.md) — maps the
  v3 reference assets to the 10 journeys; identifies what's
  reusable and what needs new v3 surfaces

---

**Last updated:** 2026-05-20
