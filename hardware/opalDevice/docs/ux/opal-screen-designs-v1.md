# LYNA v1 iPhone Screen Designs — Pixel-Perfect Specifications

**Date:** 2026-05-20
**Form factor:** v1 iPhone app
**Target device:** iPhone 14 / 15 (390 × 844 pt logical, 3× scale)
**Companion to:** [`opal-ui-wireframes-v1.md`](opal-ui-wireframes-v1.md)
**Design system:** [`opal-design-system.md`](opal-design-system.md)
+ [`design-tokens.json`](design-tokens.json) — colors, typography,
spacing are reusable as-is from v3

This doc specs the surfaces that are **novel for v1** or carry
behavior the design system doesn't already cover. Surfaces that
are simple compositions of design-system primitives (e.g., S10
Settings) are not pixel-spec'd — the design system + the
wireframe in `opal-ui-wireframes-v1.md` is enough.

**Specified here:**
- S1 voice command (all four states + error)
- S2 Home / mode indicator
- S3 Response Card (standard + AI-source pill variant + first-time
  exposure card)
- S4 Brain sheet (unit + assignment variants)
- S5 Critical Alert (full screen + status-bar banner)
- S6 Broadcast composer + ack tracker (sender + receiver banner)
- S7 Interpreter mode (compliance modal + active session)
- S8 Camera handoff banner

**Not specified (simple design-system compositions):**
- S9 Login / Shift Start (standard modal pattern)
- S10 Settings (standard iOS settings list)

---

## 0. iPhone viewport constants

```
Logical viewport: 390 × 844 pt
Safe area insets:
  Top:    47 pt  (status bar + dynamic island clearance)
  Bottom: 34 pt  (home indicator clearance)
Working area:    390 × 763 pt
Side gutter:     16 pt (standard iOS horizontal padding)
Content width:   358 pt
```

All dimensions below are in points (logical), unless noted.

---

## 1. S1 Voice Command surface

### S1.A — Idle (Home / wake-word listening)

```
y=0    ┌─────────────────────────────────┐
       │   iOS status bar (system)       │  47 pt safe-area top
y=47   ├─────────────────────────────────┤
       │   App header                    │  56 pt
       │   ┌───────┐         ┌────┐      │
       │   │ LYNA  │         │ ⚙  │      │
       │   └───────┘         └────┘      │
y=103  │   Sarah M.                      │
       │   4-South · Night Shift         │  44 pt (identity strip)
y=147  ├─────────────────────────────────┤
       │   Mode pill                     │  56 pt total (incl. margin)
y=159  │   ┌─────────────────────────┐  │
       │   │ Mode: NORMAL        ▼   │  │  44 pt height, full-width
       │   └─────────────────────────┘  │
y=215  ├─────────────────────────────────┤
       │                                 │
       │   Recent                        │  Section header 28 pt
       │   ──────────────────────────    │
       │                                 │
       │   ┌─────────────────────────┐  │
       │   │ Pain med for bed 14     │  │  44 pt per row (recents)
       │   ├─────────────────────────┤  │
       │   │ Door code med room      │  │
       │   ├─────────────────────────┤  │
       │   │ Charge nurse tonight    │  │
       │   └─────────────────────────┘  │
y=387  ├─────────────────────────────────┤
       │                                 │
       │   Quick Actions                 │  Section header 28 pt
       │   ──────────────────────────    │
       │                                 │
       │   ┌──────┬──────┬──────┐       │  3-tile grid, 88 pt each
       │   │ 📋   │ 📢   │ 🌐   │       │
       │   │Brain │Broad-│Intpr-│       │
       │   │sheet │cast  │eter  │       │
       │   └──────┴──────┴──────┘       │
y=531  │                                 │
       │   (flex spacer)                 │
       │                                 │
y=697  ├─────────────────────────────────┤
       │      ┌──────────────┐           │  TALK button
       │      │              │           │  120 × 120 pt circular
       │      │     🎤       │           │  Min touch target 88×88 pt
       │      │    TALK      │           │  Glove-friendly
       │      │              │           │
       │      └──────────────┘           │
y=817  │   "Hey LYNA" — always listening │  14 pt caption
y=841  ├─────────────────────────────────┤
       │   Home indicator (system)       │  34 pt safe-area bottom
y=844  └─────────────────────────────────┘
```

**App header (y=47–103):**
- Background: `#FFFFFF`
- Padding: 16 pt horizontal, 12 pt vertical
- "LYNA" logo wordmark: 24 pt SF Pro Display Semibold, `#111827`
- Settings icon ⚙: 24×24 pt, `#6B7280`, 44×44 pt touch target
- Identity strip (Sarah M. / 4-South · Night Shift): 16 pt body + 13 pt caption, `#6B7280`

**Mode pill (y=159–203):**
- Container: 358 × 44 pt, corner radius 22 pt (fully rounded)
- Background: `#EFF6FF` (NORMAL — light blue tint)
- Border: 1.5 pt solid `#2563EB` (NORMAL — primary blue)
- Text: "Mode: NORMAL" 16 pt SF Pro Text Semibold, `#2563EB`
- Trailing chevron ▼: 12 pt, `#2563EB`
- Tap target: full 358 × 44 pt
- Mode-specific colors (overrides):
  - **BROADCAST** — background `#FFF7ED`, border `#F97316`, text `#F97316`
  - **INTERPRETER** — background `#FAF5FF`, border `#9333EA`, text `#9333EA`

**Recents (y=215–387):**
- Section header "Recent": 13 pt SF Pro Text Semibold, `#6B7280`, all caps optional
- Each row: 44 pt height, 16 pt horizontal padding
- Row text: 16 pt SF Pro Text Regular, `#111827`
- Row tap → re-runs the query or re-opens the cached S3 Response Card
- Divider between rows: 1 pt `#E5E7EB`

**Quick Actions (y=387–531):**
- Section header: same as Recents
- 3-tile grid: each tile 110 × 88 pt, 16 pt gap, 16 pt outer margin
- Tile background: `#F9FAFB`
- Tile corner radius: 12 pt
- Tile content: 32 pt emoji icon centered, label 13 pt SF Pro Text Regular `#111827` below
- Tap target: full tile area

**TALK button (y=697–817):**
- Diameter: 120 pt circle
- Centered horizontally
- Background: `#2563EB` (primary blue; mode-color when not NORMAL)
- Icon 🎤: 40 × 40 pt centered above text
- Text: "TALK" 18 pt SF Pro Text Semibold, `#FFFFFF`
- Shadow: 0 8 pt 24 pt rgba(37, 99, 235, 0.32)
- Hold-to-talk: long-press triggers S1.B Listening; release commits
- Single tap: also triggers S1.B (toggle behavior)
- Wake-word caption: 14 pt SF Pro Text Regular, `#6B7280`, centered

### S1.B — Listening

```
y=47   ├─────────────────────────────────┤
       │   ◀ Cancel                      │  44 pt header
y=91   ├─────────────────────────────────┤
       │                                 │
       │                                 │
       │       (waveform animation)      │  height ~120 pt
       │      ╱╲    ╱╲    ╱╲             │  Bars: 4 pt wide,
       │     ╱  ╲  ╱  ╲  ╱  ╲            │  2 pt gap, height
       │    ╱    ╲╱    ╲╱    ╲           │  responds to mic level
       │                                 │  Color: #2563EB
       │                                 │
y=263  │   Listening...                  │  20 pt SF Pro Text
       │                                 │  Medium, #111827
y=295  │                                 │
       │   ┌─────────────────────────┐  │
       │   │ "what's the last pain   │  │  Transcript preview
       │   │  med for bed fourteen"  │  │  16 pt Regular #6B7280
       │   └─────────────────────────┘  │  Updates live
y=403  │                                 │
       │   (flex spacer)                 │
       │                                 │
y=697  ├─────────────────────────────────┤
       │      ┌──────────────┐           │  STOP button
       │      │              │           │  120 × 120 pt
       │      │     ⏹        │           │  Background: #EF4444
       │      │    STOP      │           │  (red)
       │      │              │           │
       │      └──────────────┘           │
```

**Waveform:**
- 24 vertical bars
- Bar width: 4 pt
- Gap: 2 pt
- Min height: 4 pt (idle baseline)
- Max height: 120 pt (peak input)
- Height = function(mic input level), 60fps smoothed

**Auto-commit:** 1.2 s of silence after the last detected speech
edge.

**Cancel affordance:** standard iOS back-chevron pattern, 44×44 pt
touch target.

### S1.C — Processing

```
y=47   ├─────────────────────────────────┤
       │   ◀ Cancel                      │  44 pt header
y=91   ├─────────────────────────────────┤
       │                                 │
       │                                 │
       │            ◌                    │  Animated spinner
       │           ◌ ◌                   │  48 pt diameter
       │            ◌                    │  Color: #2563EB
       │                                 │
y=263  │   Processing...    ~2s          │  20 pt text + 14 pt
       │                                 │  latency badge
y=295  │                                 │
       │   ┌─────────────────────────┐  │
       │   │ "What's the last pain   │  │  Confirmed transcription
       │   │  med for bed 14?"       │  │  16 pt Regular #111827
       │   └─────────────────────────┘  │
y=403  │                                 │
       │   Querying: Epic MAR via FHIR   │  14 pt SF Pro Text
       │                                 │  Regular #6B7280
       │                                 │
```

**Latency badge:**
- ≤2s: `#10B981` (green)
- 2–5s: `#F59E0B` (orange)
- >5s: `#EF4444` (red) + voice fallback "I'm slower than usual"
- >10s: auto-cancel with retry affordance

### S1.D — Speaking

Identical layout to S1.C, but:
- Spinner replaced by animated speaker icon 🔊 with concentric
  ripples (`#2563EB` at 60% opacity, expanding outward, 1.5s loop)
- Body content is the LYNA response transcript (16 pt SF Pro Text
  Regular `#111827`), synced with TTS playback
- Citation footer at bottom (12 pt SF Pro Text Regular `#6B7280`)
- Affordance row: "[Say it again] [Show on card]" — 44 pt button
  row at bottom

### S1.E — Error states

Standard iOS empty-state pattern. Background: `#FFFFFF`. Centered:
- Warning icon ⚠: 48 × 48 pt, `#F59E0B`
- Title (e.g., "Offline"): 20 pt Semibold, `#111827`
- Body: 16 pt Regular, `#6B7280`, max-width 280 pt
- Primary action button: 48 pt height, `#2563EB`, full-width
- Secondary affordances: 44 pt rows below

---

## 2. S2 Home

Same as S1.A above. See §1.A.

### S2.A — Mode switcher (modal sheet)

Standard iOS bottom sheet, ~85% screen height, dimmed backdrop
(rgba(0,0,0,0.4)).

```
y=130  ├─────────────────────────────────┤  Sheet starts ~130 pt
       │ ──── (drag handle)              │  Drag handle 36×4 pt #D1D5DB
y=152  │                                 │
       │ ✕ Close            Select mode  │  44 pt header
y=196  ├─────────────────────────────────┤
       │                                 │
       │   ┌─────────────────────────┐  │
       │   │ ● NORMAL                │  │  120 pt tall card
       │   │ ────────                │  │  Selected: solid border
       │   │ Single-recipient        │  │  Background:
       │   │ queries & answers       │  │    NORMAL: #EFF6FF
       │   └─────────────────────────┘  │
       │                                 │
       │   ┌─────────────────────────┐  │
       │   │ ○ BROADCAST             │  │
       │   │ ────────────            │  │
       │   │ Help requests to the    │  │
       │   │ whole unit              │  │
       │   │ Group:           ▼      │  │  Group selector, disabled
       │   └─────────────────────────┘  │  until BROADCAST selected
       │                                 │
       │   ┌─────────────────────────┐  │
       │   │ ○ INTERPRETER           │  │
       │   │ ──────────────          │  │
       │   │ Bidirectional ad-hoc    │  │
       │   │ translation             │  │
       │   │ Language:        ▼      │  │  Language selector,
       │   └─────────────────────────┘  │  disabled until selected
       │                                 │
y=748  ├─────────────────────────────────┤
       │   Confirm                       │  Primary action 48 pt
y=796  └─────────────────────────────────┘
```

**Selection states:**
- Selected card: solid 2 pt border in mode color, ● filled dot
- Unselected card: 1 pt border `#E5E7EB`, ○ empty dot

---

## 3. S3 Response Card

### S3.A — Standard response card

```
y=47   ├─────────────────────────────────┤
       │   ◀ Back                        │  44 pt header
y=91   ├─────────────────────────────────┤
       │                                 │
       │   ┌─────────────────────────┐  │  Question echo
       │   │ ❝ What's the last pain  │  │  Background: #F3F4F6
       │   │   med for bed 14?       │  │  Border-left: 3 pt #6B7280
       │   └─────────────────────────┘  │  Padding: 12 pt
       │                                 │  Text: 14 pt italic #6B7280
y=183  │                                 │
       │   Mrs. Reynolds, bed 14         │  Patient header
       │                                 │  20 pt Semibold #111827
y=219  │                                 │
       │   Last dose:                    │  Section label 13 pt
       │   ▸ Hydromorphone 0.5 mg IV     │  Bold value 18 pt #111827
       │   ▸ 11:43 PM — 2.5 hours ago    │  Detail 16 pt #6B7280
       │                                 │
       │   Next dose:                    │
       │   ▸ Available in 30 minutes     │
       │   ▸ PRN q3h; sooner needs MD    │
y=391  │                                 │
       │   ┌─────────────────────────┐  │  AI-source pill (S3.B var)
       │   │ 🧠 LYNA · Epic FHIR     │  │  See S3.B for richer
       │   └─────────────────────────┘  │  hospital-AI variant
y=435  │                                 │
       │   Source: Epic MAR via          │  Citation footer
       │   FHIR Observation              │  12 pt Regular #6B7280
       │   Pulled 09:41:12               │
y=499  │                                 │
       │   (flex spacer)                 │
       │                                 │
y=697  ├─────────────────────────────────┤
       │   ┌─────────────────────────┐  │  Action affordance
       │   │ Chart this              │  │  48 pt, secondary
       │   └─────────────────────────┘  │  Border-only, #2563EB
y=745  └─────────────────────────────────┘
```

**AI-source pill (standard):**
- Container: 358 × 36 pt, corner radius 18 pt
- Background: `#F3F4F6`
- Border: 1 pt `#E5E7EB`
- Icon 🧠: 16×16 pt
- Text: "LYNA · Epic FHIR" 14 pt SF Pro Text Medium, `#374151`

### S3.B — AI-source pill (hospital-integrated AI)

```
y=131  │   ┌─────────────────────────┐  │  Distinguished pill
       │   │ ⚡ Answered via your    │  │  Background: #FEF3C7
       │   │   hospital's nursing    │  │  Border: 1.5 pt #F59E0B
       │   │   reference AI    ⓘ →   │  │  Icon ⚡: amber #F59E0B
       │   └─────────────────────────┘  │  Text: 14 pt Medium
       │                                 │       #92400E
       │                                 │  Height: 64 pt (2 lines)
       │                                 │  ⓘ → opens S3.C
```

**Why amber:** the AI-source pill for hospital-integrated tools is
visually distinct from native (gray) — this is the H6 visibility
moment. The nurse should see that LYNA routed to a different
authority than usual.

### S3.C — First-time AI-tool exposure card (slide-up modal)

Sheet from bottom, ~70% screen height.

```
y=250  ├─────────────────────────────────┤
       │ ──── (drag handle)              │
y=272  │                                 │
       │   🎉 New for you!               │  24 pt Semibold #111827
       │                                 │
       │   Your hospital has the         │  16 pt Regular #374151
       │   nursing reference AI          │
       │   integrated for this kind of   │
       │   safety check.                 │
       │                                 │
       │   I'll route through it         │
       │   automatically when it's the   │
       │   right tool for the question.  │
       │                                 │
       │   What else it answers:         │  13 pt Semibold #6B7280
       │   ┌─────────────────────────┐  │
       │   │ • Drug-drug interactions │  │  16 pt Regular #111827
       │   │ • Renal/hepatic dosing  │  │
       │   │ • Pregnancy/lactation   │  │
       │   │ • Geriatric dosing      │  │
       │   └─────────────────────────┘  │
       │                                 │
       │   Added by NI team: Sep 2025    │  13 pt Regular #6B7280
       │   Vendor: [vendor name]         │
       │                                 │
y=744  ├─────────────────────────────────┤
       │   ┌─────────────────────────┐  │  Primary action 48 pt
       │   │ Got it                  │  │  Background #2563EB
       │   └─────────────────────────┘  │  Text 16 pt Semibold #FFF
y=796  └─────────────────────────────────┘
```

---

## 4. S4 Brain sheet

### S4.A — Unit brain sheet (Marcus, §4.3)

Dense, scrolling layout. Header sticky on scroll.

```
y=47   ├─────────────────────────────────┤
       │   ◀ Back        ↻ Refresh        │  44 pt header
y=91   ├─────────────────────────────────┤
       │   4-South · Unit Status         │  Sticky on scroll
       │   Data current as of 06:42 AM   │  20 pt Semibold + 13 pt
       │   ─────────────────────────     │
       │   28/32 occupied · 4 free       │  KPI strip 18 pt Medium
y=171  ├─────────────────────────────────┤
       │                                 │
       │   ┌─────────────────────────┐  │  Section card
       │   │ 🔴 OPEN CLINICAL ISSUES │  │  Section header bar
       │   │     ──────────────────  │  │  Background: #FEE2E2
       │   │                         │  │  Header text 13 pt Bold
       │   │  Bed 4 · Cruz, J. (67M) │  │  #991B1B all caps
       │   │  Pain not controlled    │  │
       │   │  PRN 4× last 04:20      │  │  Patient row:
       │   │  Pain service noted     │  │  - Header 16 pt Semibold
       │   │  06:32                  │  │  - Body 14 pt Regular
       │   │     ▸ Tap for detail    │  │    #374151
       │   │  ─────────────────      │  │  - 8 pt gap between
       │   │  Bed 18 · Patel, A...   │  │
       │   │   (...)                 │  │
       │   │  ─────────────────      │  │
       │   │  Bed 22 · Williams, R.  │  │
       │   │   (...)                 │  │
       │   └─────────────────────────┘  │
       │                                 │
       │   ┌─────────────────────────┐  │  Next section card
       │   │ 🍽 NPO — AM PROCEDURES   │  │  Background: #FEF3C7
       │   │     ──────────────────  │  │  Header #92400E
       │   │                         │  │
       │   │  Bed 7 · Garcia, M.     │  │
       │   │  Colonoscopy 08:00      │  │
       │   │  ⚠ Prep INCOMPLETE      │  │  Manual edit, red flag
       │   │   (per bowel-prep      │  │  Inline #DC2626 text
       │   │    nurse, 23:40)        │  │
       │   │  ─────────────────      │  │
       │   │  Bed 19 · Chen, K.      │  │
       │   │  (...)                  │  │
       │   └─────────────────────────┘  │
       │                                 │
       │   ┌─────────────────────────┐  │
       │   │ 🏠 PENDING DISCHARGE    │  │  Background: #DBEAFE
       │   │     ──────────────────  │  │  Header #1E40AF
       │   │   (...)                 │  │
       │   └─────────────────────────┘  │
       │                                 │
       │   ┌─────────────────────────┐  │
       │   │ 🚑 PENDING ADMITS       │  │  Background: #F3E8FF
       │   │     ──────────────────  │  │  Header #6B21A8
       │   │   (...)                 │  │
       │   └─────────────────────────┘  │
       │                                 │
       │   Citations: Epic 06:42 AM      │  Footer 12 pt #6B7280
       │   + unit board cross-check      │
       │                                 │
y=697  ├─────────────────────────────────┤
       │   ┌─────────────────────────┐  │  Primary action 48 pt
       │   │ Send to Anita →         │  │
       │   └─────────────────────────┘  │
y=745  └─────────────────────────────────┘
```

**Section card pattern:**
- Container: 358 pt width, corner radius 12 pt
- 12 pt padding all sides
- Section header bar at top: 36 pt height, full-width, color per
  section type
- Each patient row: ≥80 pt min height; 1 pt `#E5E7EB` divider
  between rows
- Tap any patient row → per-patient detail view (modal sheet, same
  shape as Sarah's S3 response card scoped to that patient)

**"Stale" badge per patient (if FHIR query failed):**
- Tag in patient header: 12 pt SF Pro Text Bold `#92400E`,
  background `#FEF3C7`, padding 2pt × 6pt, corner radius 4pt
- Voice readback names the gaps explicitly

### S4.B — Assignment brain sheet (Jamal, §4.4)

Similar to S4.A but scoped to 4 patients with a prominent sticky
priority list at the top.

```
y=47   ├─────────────────────────────────┤
       │   ◀ Back        ↻ Refresh        │
y=91   ├─────────────────────────────────┤
       │   Jamal's 4 patients · 4-South  │  Sticky header
       │   Sign-on at 07:05              │  20 + 13 pt
y=147  ├─────────────────────────────────┤
       │                                 │
       │   ┌─────────────────────────┐  │  Priority strip
       │   │ ⚡ NEXT 30 MINUTES      │  │  Background: #FEF3C7
       │   │ ─────────────────────── │  │  Header #92400E bold
       │   │ 1. ☐ Verify oxycodone   │  │  Each line tappable
       │   │    for bed 4 before     │  │  to mark done
       │   │    09:00                │  │  Checkbox + 14 pt text
       │   │ 2. ☐ Confirm bed 7's    │  │
       │   │    prep status with GI  │  │
       │   │ 3. ☐ Bed 12 family      │  │
       │   │    meeting prep         │  │
       │   └─────────────────────────┘  │
       │                                 │
       │   ┌─────────────────────────┐  │  Per-patient card
       │   │ Bed 4 · Cruz, J. (67M)  │  │  ≥160 pt tall
       │   │ Day 3 post-CABG         │  │
       │   │ ─────────────────────── │  │
       │   │ ⚠ Pain not controlled   │  │  Issue flag 14 pt #DC2626
       │   │ PRN 4× overnight per    │  │
       │   │ Sarah's handoff         │  │  14 pt Regular #374151
       │   │ New order: oxycodone    │  │
       │   │ 5mg q6h (pending        │  │
       │   │ pharmacy)               │  │
       │   │ Watch: resp rate,       │  │
       │   │ oversedation            │  │
       │   │ ────────────────────    │  │
       │   │      ▸ Tap for full     │  │  Affordance 14 pt #2563EB
       │   └─────────────────────────┘  │
       │                                 │
       │   ... (3 more patient cards)    │
```

---

## 5. S5 Critical Alert

### S5.A — Incoming alert (full screen takeover)

```
y=0    ┌─────────────────────────────────┐
       │                                 │  Full-screen, no nav
       │                                 │  Background: #FFEAEC
       │                                 │  with pulsing border
       │      🚨 RAPID RESPONSE          │  Title 28 pt Bold
       │         ───────────────         │  #DC2626 all caps
       │                                 │
       │         4-East · Bed 6          │  Location 20 pt Medium
       │                                 │  #111827
       │      Mr. Hernandez · 68M        │  Patient 18 pt Regular
       │      Day 2 post-CABG            │  #374151
       │                                 │
       │   HR 130 · new ST↓ II,aVF       │  Clinical 16 pt Regular
       │   Diaphoretic, chest pain       │  #111827
       │                                 │
       │   Last troponin 0.08 (+)        │  Context 14 pt Regular
       │   ASA 81 mg yesterday 06:00     │  #374151
       │   Heparin SC 5000u 04:00        │
       │   No ASA allergy                │
       │                                 │
       │                                 │
       │      ┌─────────────────────┐   │
       │      │                     │   │  ACK button
       │      │   ✓ ACKNOWLEDGE     │   │  300 × 88 pt
       │      │                     │   │  Background #DC2626
       │      └─────────────────────┘   │  Text 20 pt Semibold #FFF
       │                                 │  Shadow #DC262640 0/8/24
       │                                 │
       │      [View Protocol]            │  Secondary 44 pt buttons
       │      [View Vitals]              │  Border-only #DC2626
       │                                 │
       │      Activated 04:35:17         │  Timestamp 12 pt #6B7280
       │                                 │
       └─────────────────────────────────┘
```

**Pulsing border:**
- 6 pt wide solid `#DC2626` border
- Opacity animates 0.4 → 1.0 → 0.4 over 1.2 s loop

**Haptic pattern:**
- Pattern A (first 5s): strong (1s on, 0.5s off) ×2
- Pattern B (5–15s): escalating (1.5s on, 0.5s off, increasing
  intensity)
- Stops on ACK or escalates to second-tier alert at 10s timeout

**Audio:**
- Alarm tone: 880 Hz sine, 0.2s on, 0.2s off, looped
- Voice readback over the tone in earpiece
- Volume defaults to system max for safety; respects mute switch
  ONLY if hospital policy permits (per-site Operational KB flag)

### S5.B — Active alert in status bar (post-ACK)

```
y=0    ┌─────────────────────────────────┐
       │ iOS status bar                  │
y=47   ├─────────────────────────────────┤
       │ 🔴 RR active · 4-East bed 6     │  44 pt sticky banner
       │ Tap to expand                   │  Background #FEE2E2
       │                                 │  Text 14 pt #991B1B
y=91   ├─────────────────────────────────┤
       │ (rest of S2 Home, normal)       │
```

Banner persists until "End response" action in re-opened S5.A.

### S5.C — Protocol view

Standard scrolling view, header pattern same as S3. Item checklist
rendered with checkboxes; checkboxes update in real time as Sofia
or any team member marks items complete via voice
("LYNA, mark IV access done").

---

## 6. S6 Broadcast composer + ack tracker

### S6a — Sender, ack tracker

```
y=47   ├─────────────────────────────────┤
       │   ◀ Cancel broadcast            │  44 pt header
y=91   ├─────────────────────────────────┤
       │                                 │
       │   📢 Broadcasting · 4-South     │  Title 20 pt Semibold
       │                                 │  #F97316 (broadcast orange)
       │                                 │
       │   ┌─────────────────────────┐  │  Echo card
       │   │ I need a 10mL saline    │  │  Background #FFF7ED
       │   │ flush in 305, isolation │  │  Border-left 3 pt #F97316
       │   └─────────────────────────┘  │
       │                                 │
       │   Sent 09:20:14                 │  14 pt Regular #6B7280
       │                                 │
       │   Waiting for ack ...           │  18 pt Medium #111827
       │   ┌─────────────────────────┐  │  Roster panel
       │   │ 7 recipients reached    │  │  Background #F9FAFB
       │   │                         │  │  Border #E5E7EB
       │   │ ○ Maya  RN              │  │  Each row 36 pt
       │   │ ○ Tanya RN              │  │  Icon ○ → ● on ack
       │   │ ○ Linh  RN              │  │  Text 16 pt Regular
       │   │ ○ Devon PCA             │  │  #111827
       │   │ ○ Carlos PCA            │  │
       │   │ ○ Yvonne Secretary      │  │
       │   └─────────────────────────┘  │
       │                                 │
```

After first ack, view replaces with covered-state:

```
       │   📢 Broadcast covered           │  Title #10B981 (green)
       │                                 │
       │   ┌─────────────────────────┐  │
       │   │ ✓ Devon picking it up   │  │  Background #D1FAE5
       │   │   ETA 90 seconds        │  │  Border-left #10B981
       │   │   Iso-room: gowning     │  │
       │   └─────────────────────────┘  │
```

### S6b — Receiver banner (on any screen)

```
y=47   ├─────────────────────────────────┤
       │ 📢 Priya · 305 (iso)            │  60 pt non-modal banner
       │ Needs 10mL saline flush         │  Background #FFF7ED
       │ ┌──────────────┬──────────────┐ │  Border-bottom 1 pt
       │ │ Acknowledge  │ Pass         │ │  Buttons 44 pt each
       │ └──────────────┴──────────────┘ │  Ack: filled #F97316
y=107  ├─────────────────────────────────┤  Pass: outline #6B7280
       │ (rest of underlying screen)     │
```

**Voice readback through earpiece is concurrent.**

After someone acks, banner updates to "Devon's got it" then
auto-dismisses after 3s.

---

## 7. S7 Interpreter mode

### S7.A — Compliance entry modal

Standard centered modal, 320 × 480 pt, dimmed backdrop.

```
       ┌─────────────────────────────────┐
       │                                 │  320 × 480 pt centered
       │   🌐 Interpreter mode           │  20 pt Semibold #111827
       │                                 │
       │   I'll machine-translate        │  16 pt Regular #374151
       │   between English and Spanish.  │
       │                                 │
       │   Use this for ad-hoc bedside   │
       │   clarification only.           │
       │                                 │
       │   For consent, discharge        │
       │   teaching, or clinical         │  Important paragraph
       │   decisions, you need a         │  16 pt Medium #111827
       │   certified interpreter.        │  (bolded for emphasis)
       │                                 │
       │   ▸ Say "queue interpreter"     │  14 pt Regular #374151
       │     at any time and I'll        │
       │     route you to the hospital   │
       │     interpreter service.        │
       │                                 │
       │                                 │
       │   ┌─────────────────────────┐  │  Primary action 48 pt
       │   │ Got it                  │  │  Background #9333EA
       │   └─────────────────────────┘  │  (interpreter purple)
       │                                 │
       └─────────────────────────────────┘
```

**Tap "Got it"** logs the acknowledgment to the compliance event.

### S7.B — Active session

```
y=47   ├─────────────────────────────────┤
       │   ◀ End interpreter             │  44 pt header
y=91   ├─────────────────────────────────┤
       │                                 │
       │   🌐 English ⇄ Spanish          │  20 pt Semibold #9333EA
       │   Machine translation · ad-hoc  │  13 pt Regular #6B7280
       │                                 │
       │   Patient audio: 🔊 phone speaker│  13 pt Medium #374151
       │                                 │
y=187  ├─────────────────────────────────┤
       │                                 │
       │   ┌─────────────────────────┐  │  Transcript card
       │   │ ● You (English):        │  │  Active speaker: pulsing
       │   │   "Mr. Reyes, are you   │  │  green dot
       │   │   having any pain right │  │
       │   │   now? On a scale of 0  │  │  Text 16 pt Regular
       │   │   to 10."               │  │  #111827
       │   │                         │  │
       │   │ ○ Patient (Spanish):    │  │  Static dot (gray)
       │   │   "Sí, como un siete.   │  │
       │   │   Aquí, en el pecho."   │  │
       │   │                         │  │
       │   │ You (English):          │  │  Translation rendered
       │   │ ↳ "Yes, about a seven.  │  │  Indented 16 pt
       │   │   Here, in the chest."  │  │  Italic 14 pt #6B7280
       │   └─────────────────────────┘  │
       │                                 │
       │   Turn 4 · Session 02:18        │  Footer 13 pt #6B7280
       │                                 │
y=697  ├─────────────────────────────────┤
       │   ┌─────────────────────────┐  │  Hand-off affordance
       │   │ Queue certified         │  │  48 pt border-only button
       │   │ interpreter             │  │  Border 1.5 pt #9333EA
       │   └─────────────────────────┘  │  Text 16 pt Medium #9333EA
y=745  └─────────────────────────────────┘
```

**Active-speaker dot:**
- Pulsing ● (`#10B981` green, 1.2 s loop, 0.4 → 1.0 → 0.4 opacity)
  for whichever language is currently being captured
- Static ○ (1.5 pt `#9CA3AF` outline) for the other language

**Scroll:** transcript card is scrollable; auto-scrolls to latest
turn unless user scrolls up (then "pinned" until next turn arrives,
matching iMessage scroll behavior).

---

## 8. S8 Camera handoff banner

Non-modal banner, sits at top of S2 Home.

### S8.A — Initial handoff

```
y=47   ├─────────────────────────────────┤
       │ 📸 Wound photo needs your camera│  88 pt banner
       │ I've opened Haiku for bed 18,   │  Background #EFF6FF
       │ sacral, on-admission.           │  Border-left 3 pt #2563EB
       │ ┌─────────────────────────────┐ │  Heading 14 pt Semibold
       │ │ Open Haiku →                │ │  #111827
       │ └─────────────────────────────┘ │  Body 13 pt Regular
y=135  ├─────────────────────────────────┤  #6B7280
       │ (rest of S2 Home)               │  Button 36 pt, primary
       │                                 │  blue, full-width
       │                                 │  Tap → SMART app launch
```

### S8.B — After Haiku upload

Banner content changes on FHIR `DocumentReference` subscription
firing:

```
       │ ✓ 3 photos uploaded · bed 18    │  Heading 14 pt Semibold
       │ Stage not yet classified.       │  #047857 (green check)
       │ Want to dictate the note?       │
       │ ┌──────────────┬──────────────┐ │  Two buttons 36 pt each
       │ │ Dictate now  │ Later        │ │  Dictate: filled #2563EB
       │ └──────────────┴──────────────┘ │  Later: outline #6B7280
```

---

## 9. Animation specifications

| Element | Duration | Easing | Notes |
|---|---|---|---|
| Mode pill color change | 300 ms | ease-out | Brief flash on mode change |
| Sheet slide-up | 400 ms | spring | iOS default sheet animation |
| Waveform bars | 16 ms | linear (per frame) | 60 fps, height = mic level |
| Spinner | 1000 ms | linear | Rotates continuously |
| Speaker icon ripples | 1500 ms | ease-out | Concurrent with TTS |
| Critical alert border pulse | 1200 ms | ease-in-out | Opacity 0.4 ↔ 1.0 |
| Banner slide-down | 250 ms | spring | S6b receiver banner entry |
| Banner auto-dismiss | 3000 ms | linear hold | Then 250 ms slide-up |
| Active-speaker dot pulse | 1200 ms | ease-in-out | Opacity 0.4 ↔ 1.0 |
| First-time AI exposure card slide-up | 400 ms | spring | One-time per nurse per tool |

---

## 10. Accessibility

- **Touch targets:** ≥44×44 pt everywhere; ≥88×88 pt for TALK,
  STOP, ACK
- **Color contrast:** all text meets WCAG AA (4.5:1 normal, 3:1
  large)
- **Voice-over:** every actionable element has explicit
  `accessibilityLabel`; mode pill announces current mode
- **Dynamic type:** body text scales 13 → 28 pt with system
  setting; section headers and titles scale proportionally; layout
  re-flows
- **Reduced motion:** all animations disabled or replaced with
  simple opacity transitions when "Reduce Motion" is enabled
- **High contrast:** all section-card background tints darken to
  preserve text contrast when "Increase Contrast" is enabled

---

## 11. Cross-references

- [`opal-ui-wireframes-v1.md`](opal-ui-wireframes-v1.md) — ASCII
  wireframes for the same surfaces (read first for layout)
- [`opal-interaction-flows.md`](opal-interaction-flows.md) —
  canonical UX spec (what these surfaces do and why)
- [`opal-design-system.md`](opal-design-system.md) — design system
  is authoritative for color / typography / spacing
- [`design-tokens.json`](design-tokens.json) — design tokens
- [`opal-screen-designs.md`](opal-screen-designs.md) — **v3
  reference** (dedicated-device target, 240 × 320 px; preserved
  for the eventual v3 design pass)

---

**Last updated:** 2026-05-20
