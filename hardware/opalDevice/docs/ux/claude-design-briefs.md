# Claude Design Briefs — LYNA v1 iPhone + Manager Dashboard

**Date:** 2026-05-20
**For use with:** Claude Design (claude.ai/design, Anthropic Labs)
**Source specs:** [`opal-ui-wireframes-v1.md`](opal-ui-wireframes-v1.md),
[`opal-screen-designs-v1.md`](opal-screen-designs-v1.md),
[`manager-dashboard-wireframes.md`](manager-dashboard-wireframes.md),
[`manager-dashboard-screen-designs.md`](manager-dashboard-screen-designs.md)

Each section below is a self-contained brief ready to paste into a
fresh Claude Design prototype. Each brief is ~30–60 lines, scoped
to one surface or view at a time, and references the LYNA design
tokens so the generated mock matches the rest of the system.

---

## 0. How to use this doc

For each surface or view you want to mock:

1. Open `claude.ai/design`
2. Click **Prototype** → name the project (use the suggested name
   in each brief)
3. Pick **High fidelity** for finished screens, **Wireframe** for
   layout exploration
4. Leave the design-system selector at its default (the named
   default is just Claude Design's placeholder — the brief itself
   declares LYNA's colors and typography, which Claude Design
   will honor).
5. Paste the brief content into the prompt box
6. Iterate — the brief is a starting point, not a final spec

The order suggested below front-loads the **highest-impact
surfaces** (those that are most novel or carry the most weight in
demos): S3.B (AI pill), S5.A (critical alert), S6a/b (broadcast),
S7.B (interpreter), D2 (AI tool routing), D10 (buyer ROI).

---

## 1. LYNA design system (paste into every brief)

Paste this near the top of every brief; the brief-specific
content follows below it.

```
LYNA design system:

Colors:
- Primary blue (NORMAL mode):       #2563EB
  Tint:                              #EFF6FF
- Broadcast orange (BROADCAST mode): #F97316
  Tint:                              #FFF7ED
- Interpreter purple (INTERPRETER):  #9333EA
  Tint:                              #FAF5FF
- Critical red (alerts):             #DC2626
  Tint:                              #FEE2E2
- Success green:                     #10B981
- Warning amber:                     #F59E0B
- Text primary:                      #111827
- Text secondary:                    #6B7280
- Surface:                           #F9FAFB
- Card border:                       #E5E7EB
- Background:                        #FFFFFF

Typography (iPhone): SF Pro Display for titles, SF Pro Text for
body. Section headers 13pt bold uppercase letter-spaced. Body
16pt regular. Large numbers 32pt bold.

Typography (Dashboard web): same family stack; titles 28pt
semibold; section headers same; tables 14-16pt regular.

Spacing: 8pt baseline; 16pt standard padding; 24pt card padding;
12pt card corner radius; 18pt or 22pt pill corner radius.

Touch targets: minimum 44×44pt, prefer 88×88pt for primary
actions (TALK, ACK, STOP, broadcast).
```

---

## Part A — v1 iPhone surfaces

### Brief S1.A — Voice Command Idle (Home screen)

**Project name:** "LYNA v1 · S1.A Home"
**Mode:** High fidelity
**Viewport:** iPhone 14, 390 × 844 pt portrait

**Prompt:**
> Design an iPhone app home screen for **LYNA**, a voice-first
> clinical assistant for hospital nurses. The home screen is
> always visible when LYNA isn't actively processing — the
> nurse opens the app, sees who she is, what mode LYNA is in,
> and a large TALK button for voice queries.
>
> [paste the LYNA design system block from §1]
>
> **Layout (top to bottom):**
> 1. App header (56pt): "LYNA" wordmark left, settings ⚙ icon
>    right.
> 2. Nurse identity strip (44pt): "Sarah M." (semibold) +
>    "4-South · Night Shift" (regular, secondary).
> 3. Mode pill (44pt, fully rounded, full-width): "Mode: NORMAL ▼"
>    in NORMAL-blue style. Tap target opens mode switcher (separate
>    brief). Pill colors switch with mode: NORMAL blue, BROADCAST
>    orange, INTERPRETER purple.
> 4. "Recent" section (header 13pt bold uppercase): list of 3-5
>    recent queries (44pt rows, 16pt padding, 1pt divider). Sample
>    items: "Pain med for bed 14", "Door code med room", "Charge
>    nurse tonight".
> 5. "Quick Actions" section: 3-tile grid (110×88pt each, 16pt
>    gap). Tiles: 📋 Brain sheet, 📢 Broadcast, 🌐 Interpreter.
>    Tile background #F9FAFB, corner 12pt, emoji 32pt centered,
>    label 13pt below.
> 6. Flex spacer.
> 7. TALK button (120pt circle, centered): blue #2563EB
>    background, 🎤 icon (40pt) above "TALK" text (18pt semibold
>    white). Shadow 0/8/24 rgba(37,99,235,0.32).
> 8. Caption below TALK: "'Hey LYNA' — always listening" (14pt
>    secondary).
>
> Status bar at top, home indicator at bottom (system).

---

### Brief S1.B — Voice Command Listening

**Project name:** "LYNA v1 · S1.B Listening"
**Mode:** High fidelity

**Prompt:**
> Design the **Listening** state of LYNA's voice command screen
> on iPhone. Triggered immediately after the wake word fires or
> the TALK button is held. The nurse sees an animated waveform
> as LYNA captures her voice, plus a live transcription preview.
>
> [paste LYNA design system block from §1]
>
> **Layout (top to bottom):**
> 1. Header (44pt): "◀ Cancel" affordance (left).
> 2. Centered animated waveform (~120pt height): 24 vertical bars,
>    4pt wide, 2pt gap, height responds to mic input level. Color
>    #2563EB. Bars min 4pt, max 120pt.
> 3. State label: "Listening..." (20pt medium, primary text).
> 4. Live transcription card (full-width minus 16pt margins,
>    12pt padding, background #F3F4F6, corner 12pt): sample text
>    italic 16pt secondary — `"what's the last pain med for bed
>    fourteen"`. Text updates in near-real-time as recognition
>    progresses.
> 5. Flex spacer.
> 6. STOP button at bottom (120pt circle): red #EF4444 background,
>    ⏹ icon + "STOP" text (18pt semibold white). Tap to commit
>    immediately. Auto-commits after 1.2s of silence regardless.

---

### Brief S1.C — Voice Command Processing

**Project name:** "LYNA v1 · S1.C Processing"
**Mode:** High fidelity

**Prompt:**
> Design the **Processing** state of LYNA's voice command screen.
> After listening commits, LYNA is querying its sources (Epic
> FHIR, hospital policy, integrated AI). The nurse sees a
> spinner and a latency estimate.
>
> [paste LYNA design system block from §1]
>
> **Layout:**
> 1. Header (44pt): "◀ Cancel".
> 2. Centered animated spinner (~48pt, primary blue), with three
>    rotating dots arrangement.
> 3. State row: "Processing..." (20pt medium) + small latency
>    badge to the right "~2s". Badge colors: ≤2s green #10B981,
>    2-5s orange #F59E0B, >5s red #EF4444.
> 4. Confirmed transcription card (same style as S1.B but with
>    primary text not italic): `"What's the last pain med for
>    bed 14?"`.
> 5. Activity caption: "Querying: Epic MAR via FHIR" (14pt
>    secondary).
> 6. (No action button. Cancel via header.)

---

### Brief S1.D — Voice Command Speaking (response readback)

**Project name:** "LYNA v1 · S1.D Speaking"
**Mode:** High fidelity

**Prompt:**
> Design the **Speaking** state of LYNA's voice command screen.
> LYNA is reading the response aloud through the nurse's
> earpiece; the screen shows a synced live transcript with the
> citation at the bottom.
>
> [paste LYNA design system block from §1]
>
> **Layout:**
> 1. Header (44pt): "◀ Done" (left), "🔇 Mute readback" (right —
>    mutes audio, leaves transcript on screen).
> 2. Centered speaker icon 🔊 with three concentric ripples
>    expanding outward (primary blue, 60% opacity, 1.5s loop).
> 3. Response transcript card (16pt regular, primary text,
>    16pt padding, no card border):
>    `"Mrs. Reynolds in bed 14 last had hydromorphone 0.5 mg IV
>    at 11:43 PM — about 2.5 hours ago. PRN q3h. Due in 30
>    minutes."`
> 4. Citation footer (12pt regular secondary, 16pt top-margin):
>    "Source: Epic MAR via FHIR Observation. Pulled 09:41:12."
> 5. Two affordance buttons at bottom (44pt height, 16pt gap):
>    "Say it again" (border-only blue) and "Show on card"
>    (border-only blue).

---

### Brief S2.A — Mode switcher modal

**Project name:** "LYNA v1 · S2.A Mode Switcher"
**Mode:** High fidelity

**Prompt:**
> Design a bottom-sheet modal for switching LYNA's mode. The
> nurse taps the mode pill on the home screen, this sheet slides
> up from the bottom covering ~85% of the screen.
>
> [paste LYNA design system block from §1]
>
> **Layout:**
> 1. Drag handle at top (36×4pt, #D1D5DB).
> 2. Sheet header (44pt): "✕ Close" (left) + "Select mode"
>    title (right).
> 3. Three mode cards stacked vertically (120pt each, 16pt
>    gap):
>    - **NORMAL** (currently selected): solid 2pt border in
>      NORMAL-blue, filled ● dot, "Single-recipient queries and
>      answers" body text. Background #EFF6FF.
>    - **BROADCAST**: 1pt border #E5E7EB (unselected), empty ○
>      dot, "Help requests to the whole unit" body text. Below
>      the body: a disabled "Group: ────  ▼" selector (enabled
>      when BROADCAST tapped, shows: All Nurses / Charge Nurse /
>      RRT / Department).
>    - **INTERPRETER**: same unselected style, "Bidirectional
>      ad-hoc translation" body text, disabled
>      "Language: ────  ▼" selector (enabled when tapped:
>      Spanish / Mandarin / Russian / Bengali / Korean).
> 4. Sticky bottom action: "Confirm" primary button (48pt height,
>    full-width minus margins, NORMAL-blue background, 16pt
>    semibold white text).

---

### Brief S3.A — Response Card (standard)

**Project name:** "LYNA v1 · S3.A Response Card"
**Mode:** High fidelity

**Prompt:**
> Design a response card for LYNA — shown after a query when the
> nurse wants to see the answer visually (also used as the
> persistent "show on card" state from S1.D).
>
> [paste LYNA design system block from §1]
>
> **Layout (full-screen, iPhone portrait):**
> 1. Header (44pt): "◀ Back".
> 2. Question echo (above the answer, indented): "❝ What's the
>    last pain med for bed 14?" — 14pt italic secondary text,
>    left border-stripe 3pt #6B7280, padding 12pt, background
>    #F3F4F6.
> 3. Patient header: "Mrs. Reynolds, bed 14" — 20pt semibold
>    primary text.
> 4. Section "Last dose:" (13pt medium uppercase secondary, 0.5pt
>    letter-spacing). Body two lines:
>    - "▸ Hydromorphone 0.5 mg IV" (bold 18pt primary)
>    - "▸ 11:43 PM — 2.5 hours ago" (regular 16pt secondary)
> 5. Section "Next dose:" same style:
>    - "▸ Available in 30 minutes" (bold)
>    - "▸ PRN q3h; sooner needs MD" (regular)
> 6. AI-source pill (full-width, 36pt height, 18pt corner radius,
>    background #F3F4F6, border 1pt #E5E7EB): "🧠 LYNA · Epic
>    FHIR" (14pt medium #374151).
> 7. Citation footer (12pt regular secondary): "Source: Epic MAR
>    via FHIR Observation. Pulled 09:41:12."
> 8. Flex spacer.
> 9. Action button at bottom: "Chart this" (48pt height, secondary
>    style: border-only NORMAL-blue, blue text).

---

### Brief S3.B — Response Card with AI-source pill (Hospital AI)

**Project name:** "LYNA v1 · S3.B AI Pill"
**Mode:** High fidelity

**Prompt:**
> Design a response card variant where LYNA routed the answer
> through a hospital-integrated AI tool. The AI-source pill is
> visually distinctive (amber) so the nurse notices that a
> different authority answered.
>
> [paste LYNA design system block from §1]
>
> **Layout:** same overall structure as S3.A, but:
> 1. Question echo at top: "❝ Is the new cipro okay with what
>    Mr. Alvarez is already on?"
> 2. **AI-source pill at the TOP of the body** (above content,
>    not below): full-width, 64pt height (2-line), corner 18pt,
>    background #FEF3C7 (amber tint), border 1.5pt #F59E0B,
>    text "⚡ Answered via your hospital's nursing reference AI
>    ⓘ →" — 14pt medium #92400E. The ⓘ → at right is tappable
>    and opens the first-time exposure card (S3.C).
> 3. Warning row: "⚠ One interaction flagged" (16pt semibold
>    #DC2626).
> 4. Body content paragraphs:
>    - "Cipro inhibits warfarin metabolism. INR can rise over
>      3–5 days." (regular)
>    - "Last INR (2026-05-14): 2.4" + bullet "▸ In range."
>    - "Recommendation:" header + bullets:
>      "▸ Recheck INR at 48h"
>      "▸ Routine note to anticoag"
>    - "No allergies. No renal-dose adjustment needed (creatinine
>      1.1)."
> 5. Multi-source citation footer (12pt regular secondary):
>    "Source: Hospital nursing reference AI (registry ID
>    NU-AI-014) + Epic FHIR MedicationRequest + Observation."
> 6. Action button at bottom: "Send note to anticoag" (48pt,
>    NORMAL-blue filled, white text).

---

### Brief S3.C — First-time AI-tool exposure card

**Project name:** "LYNA v1 · S3.C First-Time AI Exposure"
**Mode:** High fidelity

**Prompt:**
> Design a bottom-sheet modal that slides up the first time a
> nurse sees LYNA route through a specific hospital-integrated
> AI tool. The point of the moment is awareness — the nurse
> learns the hospital has invested in this tool and what else
> it can answer.
>
> [paste LYNA design system block from §1]
>
> **Layout (sheet, ~70% screen height, slides from bottom):**
> 1. Drag handle (36×4pt, #D1D5DB).
> 2. Title with celebration affordance: "🎉 New for you!" — 24pt
>    semibold primary.
> 3. Body paragraph 1 (16pt regular #374151):
>    "Your hospital has the nursing reference AI integrated for
>    this kind of safety check."
> 4. Body paragraph 2 (16pt regular #374151):
>    "I'll route through it automatically when it's the right
>    tool for the question."
> 5. Section header (13pt semibold uppercase secondary): "What
>    else it answers:"
> 6. Bullet list in a card (background #F9FAFB, corner 12pt, 16pt
>    padding):
>    - Drug-drug interactions
>    - Renal/hepatic dosing
>    - Pregnancy/lactation
>    - Geriatric dosing
> 7. Footer metadata (13pt regular secondary):
>    "Added by NI team: Sep 2025"
>    "Vendor: [vendor name]"
> 8. Primary action at bottom: "Got it" (48pt, NORMAL-blue filled,
>    16pt semibold white).

---

### Brief S4.A — Unit brain sheet (charge nurse handoff)

**Project name:** "LYNA v1 · S4.A Unit Brain Sheet"
**Mode:** High fidelity

**Prompt:**
> Design a unit-wide brain sheet for a charge nurse compiling
> end-of-shift handoff. Dense scrolling layout with sticky
> header. The screen replaces walking around with a paper sheet
> for 20 minutes.
>
> [paste LYNA design system block from §1]
>
> **Layout:**
> 1. Sticky header section (top of scroll):
>    - "◀ Back" (left) and "↻ Refresh" (right) in 44pt nav row
>    - "4-South · Unit Status" 20pt semibold primary
>    - "Data current as of 06:42 AM" 13pt regular secondary
>    - 1pt divider
>    - KPI strip: "28/32 occupied · 4 free" 18pt medium
> 2. Section cards (24pt vertical gap between), each one a card
>    with:
>    - colored header bar (40pt height, color-coded background +
>      darker text)
>    - bottom content with patient rows
>
>    **Section 1 — OPEN CLINICAL ISSUES** (background #FEE2E2,
>    header text #991B1B): 3 patient entries, each ≥80pt:
>      - "🔴 Bed 4 · Cruz, J. (67M)" header (16pt semibold)
>      - "Pain not controlled" + "PRN 4× last 04:20" + "Pain
>        service noted 06:32" (14pt regular #374151)
>      - "▸ Tap for detail" (14pt #2563EB link)
>      - 1pt #E5E7EB divider before next patient
>      - "🔴 Bed 18 · Patel, A. (52F)" + 14pt body lines (temp
>        spike, cultures, etc.)
>      - "🔴 Bed 22 · Williams, R. (78F)" + body (fall, IR filed)
>
>    **Section 2 — NPO AM PROCEDURES** (background #FEF3C7,
>    header #92400E):
>      - "🍽 Bed 7 · Garcia, M." + "Colonoscopy 08:00" + "⚠
>        Prep INCOMPLETE (per bowel-prep nurse, 23:40)" in
>        red #DC2626
>      - "🍽 Bed 19 · Chen, K." + "Cardiac cath 09:30" + "✓
>        Consent obtained"
>
>    **Section 3 — PENDING DISCHARGE** (background #DBEAFE,
>    header #1E40AF):
>      - "🏠 Bed 11 · Roberts, T." + "Transport 11:00 ✓"
>      - "🏠 Bed 25 · Liu, S." + "PT clearance pending"
>
>    **Section 4 — PENDING ADMITS** (background #F3E8FF, header
>    #6B21A8):
>      - "🚑 ED: 1 (chest pain r/o) → bed 4 once repositioned"
> 3. Citations footer (12pt secondary): "Citations: Epic 06:42
>    AM + unit board cross-check."
> 4. Sticky bottom action: "Send to Anita →" (48pt, NORMAL-blue
>    filled).

---

### Brief S4.B — Assignment brain sheet (sign-on)

**Project name:** "LYNA v1 · S4.B Sign-On Brain Sheet"
**Mode:** High fidelity

**Prompt:**
> Design a sign-on brain sheet for a day-shift nurse taking over
> 4 patients at the start of shift. Similar to S4.A but scoped
> to 4 patients with a prominent priority list at top.
>
> [paste LYNA design system block from §1]
>
> **Layout:**
> 1. Sticky header: "◀ Back" + "↻ Refresh" nav row + "Jamal's 4
>    patients · 4-South" + "Sign-on at 07:05" (smaller).
> 2. **Priority card** (background #FEF3C7, header bar #92400E):
>    - Header "⚡ NEXT 30 MINUTES"
>    - 3 checkbox rows (44pt each):
>      - "1. ☐ Verify oxycodone for bed 4 before 09:00"
>      - "2. ☐ Confirm bed 7's prep status with GI"
>      - "3. ☐ Bed 12 family meeting prep"
>    - Checkboxes are tappable; ☐ becomes ✓ when checked
> 3. Four per-patient cards (160pt each, 16pt gap):
>    - **Bed 4 · Cruz, J. (67M)** card:
>      - "Day 3 post-CABG" subtitle
>      - "⚠ Pain not controlled" red warning row
>      - Body: "PRN 4× overnight per Sarah's handoff. New order:
>        oxycodone 5mg q6h (pending pharmacy). Watch: resp rate,
>        oversedation."
>      - Bottom link: "▸ Tap for full view"
>    - **Bed 7 · Garcia, M. (54F)** card:
>      - "NPO since midnight. Colonoscopy 08:00."
>      - "⚠ Prep incomplete" red row + "GI team aware"
>      - "▸ Tap for full view"
>    - **Bed 12 · Whitfield, A. (81F)** card:
>      - "ESRD on HD. Dialysis today 13:00. K+ 5.1 yesterday.
>        Family meeting 10 AM."
>      - "▸ Tap for full view"
>    - **Bed 19 · Chen, K. (72M)** card:
>      - "Cardiac cath 09:30. ✓ Consent · ✓ NPO. No overnight
>        events."
>      - "▸ Tap for full view"

---

### Brief S5.A — Critical Alert (full-screen takeover)

**Project name:** "LYNA v1 · S5.A Critical Alert"
**Mode:** High fidelity

**Prompt:**
> Design the **full-screen critical alert** that preempts
> everything on the nurse's phone when a rapid response is
> activated (either she activated it via voice, or she's being
> notified she's on the response team). This is LYNA's most
> visually-prominent and behaviorally-strict surface.
>
> [paste LYNA design system block from §1]
>
> **Layout (full-screen, no nav):**
> 1. Background: #FFEAEC (alert pink-red).
> 2. Pulsing border: 6pt wide #DC2626 solid, opacity animates
>    0.4 ↔ 1.0 over 1.2s loop.
> 3. Title (centered, top): "🚨 RAPID RESPONSE" 28pt bold
>    uppercase #DC2626.
> 4. Location: "4-East · Bed 6" — 20pt medium primary.
> 5. Patient identity: "Mr. Hernandez · 68M" + "Day 2 post-CABG"
>    18pt regular #374151.
> 6. Clinical state (boxed paragraph, 16pt primary):
>    "HR 130 · new ST↓ II, aVF"
>    "Diaphoretic, chest pain"
> 7. Context (14pt regular #374151, smaller):
>    "Last troponin 0.08 (+)"
>    "ASA 81 mg yesterday 06:00"
>    "Heparin SC 5000u 04:00"
>    "No ASA allergy"
> 8. **ACK button** — large primary action, centered horizontally,
>    300×88pt. Background #DC2626, "✓ ACKNOWLEDGE" 20pt
>    semibold white. Drop shadow 0/8/24 rgba(220, 38, 38, 0.25).
> 9. Two secondary action buttons below (44pt height):
>    "View Protocol" (border-only #DC2626 text) and
>    "View Vitals" (same style).
> 10. Timestamp at bottom: "Activated 04:35:17" — 12pt regular
>     secondary.

---

### Brief S5.B — Critical Alert status bar (post-ACK)

**Project name:** "LYNA v1 · S5.B Alert Status Bar"
**Mode:** High fidelity

**Prompt:**
> Design the sticky status banner that replaces the full-screen
> alert after the nurse acknowledges. The alert is still active
> (the situation is ongoing) but no longer takes over the screen.
>
> [paste LYNA design system block from §1]
>
> **Layout:**
> 1. Top of screen (below iOS status bar), 44pt height sticky
>    banner.
> 2. Background: #FEE2E2 (red tint).
> 3. Content: "🔴 RR active · 4-East bed 6" (14pt medium #991B1B)
>    + "Tap to expand" (12pt regular #991B1B, right-aligned).
> 4. Below: the underlying screen content (e.g., S2 Home) shows
>    normally with this banner pinned at top.
> 5. Tap behavior: re-opens S5.A full-screen view.

---

### Brief S6a — Broadcast Sender (ack tracker)

**Project name:** "LYNA v1 · S6a Broadcast Sender"
**Mode:** High fidelity

**Prompt:**
> Design the screen the broadcaster sees after sending a
> help-request broadcast to her unit. She's mid-procedure in an
> isolation room and needs something. The screen shows the
> broadcast was sent and tracks who's available + who responds.
>
> [paste LYNA design system block from §1]
>
> **Layout:**
> 1. Header (44pt): "◀ Cancel broadcast".
> 2. Title row: "📢 Broadcasting · 4-South" 20pt semibold
>    #F97316 (broadcast orange).
> 3. Echo card (background #FFF7ED, border-left 3pt #F97316,
>    12pt padding):
>    "I need a 10mL saline flush in 305, isolation"
> 4. Timestamp: "Sent 09:20:14" 14pt regular secondary.
> 5. State header: "Waiting for ack ..." 18pt medium primary.
> 6. Roster panel (background #F9FAFB, border #E5E7EB, corner
>    12pt, 16pt padding):
>    - "7 recipients reached" header
>    - Divider
>    - 7 rows, each 36pt: "○ Maya  RN", "○ Tanya RN", "○ Linh
>      RN", "○ Devon PCA", "○ Carlos PCA", "○ Yvonne Secretary"
>    - Each row has the empty ○ icon left, name + role text 16pt
>      regular primary.
> 7. As the broadcast gets acked, the screen transitions: title
>    becomes "📢 Broadcast covered" #10B981 (success green) +
>    new card (background #D1FAE5, border-left #10B981):
>    "✓ Devon picking it up. ETA 90 seconds. Iso-room: gowning"
>    + caption "You'll hear voice confirm when he's en route" +
>    "Logged 09:20:17".

---

### Brief S6b — Broadcast Receiver banner

**Project name:** "LYNA v1 · S6b Broadcast Receiver"
**Mode:** High fidelity

**Prompt:**
> Design the non-modal banner that appears on every recipient's
> phone when someone on their unit broadcasts a help request.
> The banner sits at the top of whatever screen the recipient is
> on and offers single-tap ack.
>
> [paste LYNA design system block from §1]
>
> **Layout:**
> 1. Top of screen (below iOS status bar), 60pt banner height.
> 2. Background: #FFF7ED (broadcast orange tint), 1pt bottom
>    border #F97316.
> 3. First line: "📢 Priya · 305 (iso)" 14pt semibold primary.
> 4. Second line: "Needs 10mL saline flush" 13pt regular #374151.
> 5. Two button row (44pt each, equal width):
>    - "Acknowledge" — filled #F97316 background, white text
>      semibold
>    - "Pass" — border-only #6B7280 (gray)
> 6. Below the banner: the underlying screen content (S2 Home or
>    anywhere) shows normally.

---

### Brief S7.A — Interpreter compliance modal

**Project name:** "LYNA v1 · S7.A Interpreter Compliance"
**Mode:** High fidelity

**Prompt:**
> Design the compliance modal that appears every time a nurse
> enters interpreter mode. The point is to make the
> machine-translation-vs-certified-interpreter boundary
> unambiguous. The nurse acknowledges once per session.
>
> [paste LYNA design system block from §1]
>
> **Layout (centered modal, 320×480pt, dimmed backdrop):**
> 1. Title: "🌐 Interpreter mode" 20pt semibold primary.
> 2. Body paragraph 1 (16pt regular #374151):
>    "I'll machine-translate between English and Spanish."
> 3. Body paragraph 2 (16pt regular #374151):
>    "Use this for ad-hoc bedside clarification only."
> 4. **Body paragraph 3 (emphasis — 16pt medium primary):**
>    "For consent, discharge teaching, or clinical decisions,
>    you need a certified interpreter."
> 5. Tip paragraph (14pt regular #374151):
>    "▸ Say 'queue interpreter' at any time and I'll route you
>    to the hospital interpreter service."
> 6. Primary action at bottom: "Got it" (48pt, background
>    #9333EA interpreter purple, 16pt semibold white).

---

### Brief S7.B — Interpreter active session

**Project name:** "LYNA v1 · S7.B Interpreter Active Session"
**Mode:** High fidelity

**Prompt:**
> Design the active interpreter session screen. The nurse and
> patient take turns; LYNA translates each turn in both
> directions. The screen shows a live bidirectional transcript
> and indicates which side is speaking right now.
>
> [paste LYNA design system block from §1]
>
> **Layout:**
> 1. Header (44pt): "◀ End interpreter".
> 2. Title block:
>    - "🌐 English ⇄ Spanish" 20pt semibold #9333EA (interpreter
>      purple)
>    - "Machine translation · ad-hoc" 13pt regular secondary
> 3. Audio routing indicator: "Patient audio: 🔊 phone speaker"
>    (13pt medium #374151).
> 4. Transcript card (background #F9FAFB, border #E5E7EB, corner
>    12pt, 16pt padding) showing last 3 turns:
>    - Turn 1 (current speaker — active dot ● green pulsing):
>      "● You (English):" header, then quoted text 16pt regular
>      primary.
>    - Turn 2 (other speaker — static dot ○ gray): "○ Patient
>      (Spanish):" header, then quoted text.
>    - Translation rendered below each captured turn, indented
>      with "↳" prefix, italic 14pt secondary.
>
>    Sample turns:
>    - You (English): "Mr. Reyes, are you having any pain right
>      now? On a scale of 0 to 10."
>    - ↳ "Sr. Reyes, ¿tiene dolor en este momento? En una escala
>      del cero al diez."
>    - ○ Patient (Spanish): "Sí, como un siete. Aquí, en el
>      pecho."
>    - ↳ "Yes, about a seven. Here, in the chest."
> 5. Footer (below the card): "Turn 4 · Session 02:18" 13pt
>    regular secondary.
> 6. Sticky bottom action: "Queue certified interpreter" (48pt,
>    border-only #9333EA, 16pt medium #9333EA text).

---

### Brief S8 — Camera Handoff Banner (initial + after-upload)

**Project name:** "LYNA v1 · S8 Camera Handoff"
**Mode:** High fidelity

**Prompt:**
> Design the two states of the camera handoff banner. LYNA can't
> take photos; it opens Epic Haiku for the nurse and resumes
> when photos are uploaded. The banner sits at the top of the
> home screen.
>
> [paste LYNA design system block from §1]
>
> **State A — Initial handoff (88pt banner):**
> 1. Background: #EFF6FF (blue tint), border-left 3pt #2563EB
>    (NORMAL-blue).
> 2. Top line (14pt semibold primary): "📸 Wound photo needs
>    your camera"
> 3. Body (13pt regular secondary): "I've opened Haiku for bed
>    18, sacral, on-admission."
> 4. Button (36pt height, full-width, primary blue filled):
>    "Open Haiku →"
>
> **State B — After upload (banner updates):**
> 1. Same banner container.
> 2. Top line (14pt semibold #047857 success green): "✓ 3 photos
>    uploaded · bed 18"
> 3. Body: "Stage not yet classified. Want to dictate the note?"
> 4. Two buttons (36pt each, 12pt gap):
>    - "Dictate now" filled NORMAL-blue
>    - "Later" border-only #6B7280
>
> Show both states stacked vertically for review (with a divider
> label between them).

---

### Brief S9 — Login / shift start (3-step flow)

**Project name:** "LYNA v1 · S9 Login"
**Mode:** High fidelity

**Prompt:**
> Design the three-step shift-start flow: badge tap / PIN →
> voiceprint check → assignment confirmation. Show all three
> screens stacked for review.
>
> [paste LYNA design system block from §1]
>
> **Screen 1 — Badge tap / PIN:**
> - Title: "Welcome to LYNA"
> - Large badge icon 👤 with caption "Tap your badge to sign in"
> - "─── or ───" divider
> - "Enter PIN" input field (44pt height, full-width)
>
> **Screen 2 — Voiceprint check:**
> - Greeting: "Hello, Sarah"
> - Prompt: "Quick voice check — tap and read this aloud:"
> - Card with sample sentence (16pt regular primary, 12pt
>   padding, background #F3F4F6, corner 12pt):
>   "The quick brown fox jumps over the lazy dog at four-South
>   this morning."
> - RECORD button at bottom (120pt circle, NORMAL-blue, 🎤
>   icon)
>
> **Screen 3 — Assignment confirmation:**
> - Title: "You're on 4-South tonight"
> - Patient list card (background #F9FAFB, corner 12pt, 16pt
>   padding):
>   "Your patients:"
>   "── Bed 4 · Cruz, J."
>   "── Bed 7 · Garcia, M."
>   "── Bed 12 · Whitfield, A."
>   "── Bed 19 · Chen, K."
> - Section "Mode at shift start:"
>   - "● NORMAL" (currently selected radio)
>   - "○ BROADCAST (pre-set)" radio option
> - Bottom action: "Ready" (48pt NORMAL-blue filled) — taps to
>   S2 Home.

---

### Brief S10 — Settings

**Project name:** "LYNA v1 · S10 Settings"
**Mode:** Wireframe (low priority — standard iOS settings
pattern)

**Prompt:**
> Design a standard iOS-style settings screen for LYNA. Grouped
> list with section headers and chevron rows.
>
> [paste LYNA design system block from §1]
>
> **Sections:**
> - **Voice:**
>   - "Wake word" (right value: "Hey LYNA" with chevron)
>   - "Earpiece" (right value: "AirPods Pro" with chevron)
>   - "Voice volume" (slider row)
> - **Modes:**
>   - "Default mode" (right value: "NORMAL" with chevron)
>   - "Interpreter language" (right value: "Spanish" with
>     chevron)
> - **Privacy:**
>   - "My queries log" (chevron)
>   - "Compliance audit" (chevron)
> - Bottom: "Sign out" — red text, single row, no chevron.

---

## Part B — Manager dashboard views

### Brief D1 — Adoption Overview

**Project name:** "LYNA Dashboard · D1 Adoption"
**Mode:** High fidelity
**Viewport:** desktop, 1440 × 900 minimum

**Prompt:**
> Design the **Adoption Overview** page of the LYNA manager
> dashboard. Target user: unit manager (Marcus Wells, 4-South).
> Answers the question "are nurses actually using LYNA on my
> unit?" Anchored to H13 (silent abandonment visibility).
>
> [paste LYNA design system block from §1]
>
> **Global chrome (every dashboard page):**
> - Top bar (60pt height, white background, 1pt bottom border):
>   "LYNA" wordmark + "Mt. Sinai · 4-South" left; "Marcus Wells
>   (Mgr)" + role chip + settings ⚙ right.
> - Left nav (240pt wide, #F9FAFB background, 1pt right border):
>   nav items 48pt each — Overview (active, #EFF6FF background +
>   4pt #2563EB left border + #2563EB semibold text), AI tool
>   routing, Top queries, Response times, Abandonment alerts,
>   Broadcast coverage, Critical alerts audit, Interpreter
>   sessions, Per-tool detail, Buyer ROI, divider, Settings.
>
> **Main content (right of left nav, 32pt padding):**
> 1. Page header (88pt): "ADOPTION OVERVIEW" 28pt semibold
>    primary + KPI strip below (4 cards).
> 2. KPI strip — 4 equal cards, 80pt height each, white
>    background, 1pt #E5E7EB border, 12pt corner, 16pt padding,
>    16pt gap:
>    - "ACTIVE TODAY" (13pt uppercase semibold secondary) over
>      "34" (32pt bold primary) over "▲ 4" (14pt semibold
>      #10B981)
>    - "QUERIES TODAY" / "287" / "▲ 23"
>    - "QUERIES / NURSE / SHIFT" / "8.4" / "▲ 1.2"
>    - "TIME SAVED VS BASELINE" / "~24 min/RN" / "(median)"
> 3. Filter row: 4 filter pills (36pt height, 18pt corner,
>    #F3F4F6 background, 1pt #E5E7EB border, 14pt medium
>    secondary text with ▼ chevron):
>    "Unit ▼" "Shift ▼" "7d ▼" "Role: All ▼"
> 4. Trend chart card (section card pattern, full-width):
>    "Trend (queries per day, last 90d)" + sparkline-style bar
>    chart with 90 daily bars using NORMAL-blue (#2563EB).
>    Below: 3 chart-mode toggles "[Stacked by unit] [By role]
>    [By shift]"
> 5. Per-unit heatmap card: rows = units (4-South, 4-East,
>    5-North, 6-South, Tower-3), columns = hour-of-day (00–23
>    in 2-hour steps). Cells 24×24pt. Color scale 5 buckets
>    using blue family: #F9FAFB → #DBEAFE → #93C5FD → #3B82F6
>    → #1E40AF. Legend below.
> 6. Per-nurse table card (collapsible "Show all" affordance):
>    columns: Nurse, Role, Last 7d, Trend, Status. ~10 rows
>    visible. Sample rows:
>    - "Sarah M. | RN | 84 | ▲▲▲ green | Power green pill"
>    - "Linh T. | RN | 62 | ▲▲ green | Active gray pill"
>    - "Tanya R. | RN | 41 | ─ gray | Active gray pill"
>    - "Robert K. | RN | 38 | ▲ green | Active"
>    - "Devon P. | PCA | 12 | ▼ amber | Watching amber pill"
>    - "Yvonne L. | Sec | 3 | ▼▼▼ red | Inactive red pill"
>    Each row clickable for per-nurse drill-down (separate
>    modal not in this brief).

---

### Brief D2 — AI Tool Routing

**Project name:** "LYNA Dashboard · D2 AI Tool Routing"
**Mode:** High fidelity

**Prompt:**
> Design the **AI Tool Routing** page. Target user: CCIO. The
> single most strategically important view for renewal
> conversations. Answers "which hospital AI tools are LYNA's
> nurses routing through, and how much?" Anchored to H6, H13,
> H17, H18.
>
> [paste LYNA design system block from §1]
>
> Global chrome same as D1 (top bar + left nav with this view
> active).
>
> **Main content:**
> 1. Page header: "AI TOOL ROUTING" 28pt semibold primary.
> 2. Filter row: "Unit ▼" "30d ▼" "Tool category ▼"
> 3. **Tool cards** — vertical stack, 1 per row, full width
>    (each ~280pt tall). Use the AI-tool card pattern:
>
>    **Card 1 — Healthy tool with traffic:**
>    - Header row: "Nursing Reference AI" (24pt semibold primary)
>      + status chip right-aligned "⚠ 2 issues this week"
>      (amber pill #FEF3C7 background, #92400E text)
>    - Sub-row: "(registry ID: NU-AI-014)" + "Vendor: [vendor
>      name]" + "Integration: Epic + phone app" (13pt regular
>      secondary, separated by · )
>    - Metric strip (top-border 1pt #E5E7EB, 5 cells, each cell
>      label 13pt uppercase secondary + value 20pt bold
>      primary):
>      "Routed today: 24" | "7d: 142" | "30d: 587" | "Coverage:
>      84% ✓" | "First-time exposures: 12 nurses"
>    - Sparkline (48pt height, full-width, NORMAL-blue
>      #2563EB stroke + 12% fill, 30 daily data points)
>    - Bottom link: "Drill into detail →" (14pt #2563EB)
>
>    **Card 2 — Healthy tool:**
>    - "Clinical Imaging AI" + chip "✓ Healthy" (green
>      #D1FAE5 / #047857)
>    - Subline: "(registry ID: NU-AI-008) · Integration: Haiku"
>    - Metric strip: "Today: 8 · 7d: 47 · 30d: 198 · Coverage:
>      92% · First-time: 4 nurses"
>    - Sparkline
>    - "Drill into detail →"
>
>    **Card 3 — No traffic warning:**
>    - "Sepsis Predict AI" + chip "🟡 No traffic 14d" (amber)
>    - Subline: "(registry ID: NU-AI-022) · Integration: Epic
>      CDS Hooks"
>    - Metric strip with all zeros and "Coverage: 0%"
>    - Warning callout (background #FEF3C7 amber tint, 12pt
>      padding, 12pt corner): "⚠ No queries routed through this
>      tool in 14 days. Possible causes: tool not surfaced for
>      any intent the router matches; or hospital just deployed
>      it."
>    - Two links: "Investigate →" and "Drill into detail →"
>
>    **Card 4 — Coverage low warning:**
>    - "Cardiac Decision Support" + chip "🔴 Coverage 41% (low)"
>      (red #FEE2E2 / #991B1B)
>    - Subline: "(registry ID: NU-AI-031)"
>    - Metric strip with "Coverage: 41% ⚠" highlighted
>    - Warning callout: "⚠ Only 41% of queries this tool should
>      answer were routed through it. Falling back to LYNA
>      native. Possible causes: registry entry too narrow;
>      intent classifier missing edge cases; API errors."
>    - "Investigate →"
> 4. Bottom sort row: "Sort: [Volume ▼] [Coverage] [First-time
>    exposures] [Issues]"

---

### Brief D3 — Top Queries

**Project name:** "LYNA Dashboard · D3 Top Queries"
**Mode:** High fidelity

**Prompt:**
> Design the **Top Queries** page. Target users: NI team + unit
> manager. Answers "what are nurses asking, and where are the
> knowledge gaps?" The unanswered-queries side is the most
> actionable surface — each row has an "Add to KB" affordance.
>
> [paste LYNA design system block from §1]
>
> Global chrome same as D1.
>
> **Main content:**
> 1. Page header: "TOP QUERIES" 28pt semibold primary.
> 2. Filter row: "Unit ▼" "Shift ▼" "7d ▼" "Role ▼" "Answered:
>    All ▼"
> 3. **Two-column layout** (50/50 split, 24pt gap):
>
>    **Left column — "✓ MOST-ASKED (answered)"** (section card):
>    - Numbered list of 10 most-asked queries
>    - Each row 56pt: number + query text 16pt regular + count
>      (14pt regular secondary) + "↗ {top units or nurses}"
>      + "[View samples]" link 12pt #2563EB
>    - Sample rows:
>      "1. 'Last pain med for bed N' · 142× · ↗ 4-South,
>       4-East · [View samples]"
>      "2. 'Door code med room' · 98× · ↗ all units · [View
>       samples]"
>      "3. 'Policy for med refusal' · 67× · ↗ Tanya, Linh, +5"
>      "4. 'Charge nurse tonight' · 52×"
>      "5. 'Drug interaction check' · 48×"
>      "6. 'Sign-on summary' · 41× · (charge nurses)"
>    - Bottom link: "Show all 50 →"
>
>    **Right column — "⚠ UNANSWERED (gaps)"** (section card with
>    amber-tinted header bar #FEF3C7 / #92400E):
>    - Numbered list, same row pattern
>    - Each row has an "[Add to KB]" affordance (NORMAL-blue
>      link) + optional "[Flag urgent]" amber link
>    - Sample rows:
>      "1. 'Where's the suction cart on 4-South?' · 14× ·
>       4-South night · [Add to KB]"
>      "2. 'Pyxis override code' · 9× · 4-South, 5-North ·
>       [Add to KB] [Flag?]"
>      "3. 'Sterile dressing supply on 6-East' · 7× · 6-East
>       floats · [Add to KB]"
>      "4. 'Vincristine extrav protocol' · 5× · 5-North
>       oncology · [Add to KB] [Flag urgent]"
>    - Bottom action: "Export gaps to NI →" (44pt primary
>      button)

---

### Brief D4 — Response Times

**Project name:** "LYNA Dashboard · D4 Response Times"
**Mode:** High fidelity

**Prompt:**
> Design the **Response Times** page. Target user: CCIO
> (efficiency frame, H2). Answers "is LYNA actually faster than
> the workstation?" Sub-2s is the bar.
>
> [paste LYNA design system block from §1]
>
> Global chrome same as D1.
>
> **Main content:**
> 1. Page header: "RESPONSE TIMES" 28pt semibold primary.
> 2. Filter row: "Unit ▼" "Hour-of-day ▼" "7d ▼" "Query type ▼"
> 3. **Distribution chart card** (section card pattern):
>    - Title "Round-trip latency distribution (all queries, 30d)"
>    - Histogram: bars on x-axis 0s to 7s+ in 0.5s buckets,
>      bar color NORMAL-blue 80% opacity, with a vertical 2pt
>      red #DC2626 line at the 2s mark (the target threshold)
>    - Below the chart: percentile summary row "p50: 1.4s ·
>      p75: 2.1s · p95: 4.8s · 89% under 2s ✓" (14pt medium
>      primary, ✓ in green)
> 4. **Latency by query type table** (section card):
>    - 6 rows, each with query-type name + p50 + p95
>    - Sample:
>      "FHIR (live data)     | p50: 0.9s | p95: 2.4s"
>      "OpKB (door codes...) | p50: 0.6s | p95: 1.2s"
>      "Policy lookup        | p50: 1.1s | p95: 2.8s"
>      "AI routing           | p50: 2.1s | p95: 4.8s ⚠"
>      "Drug Info            | p50: 1.4s | p95: 3.1s"
>      "Emergency intent     | p50: 0.8s | p95: 1.6s"
>    - The AI routing row gets an amber warning chip
> 5. **Per-unit comparison card** (section card):
>    - 5 rows, each unit + horizontal bar visualization +
>      p95 value + ✓ or ⚠ icon
>    - Sample (bar uses ████░░ ASCII-style or actual
>      progress-bar component):
>      "4-South     | bar p95 1.8s ✓"
>      "4-East      | bar p95 1.9s ✓"
>      "5-North     | bar p95 4.2s ⚠ (wifi?)"
>      "6-South     | bar p95 2.0s ✓"
>      "Tower-3     | bar p95 1.7s ✓"
> 6. **Slow query log card** (section card with table):
>    - 5-column table: Query | Total time | STT | Router |
>      Source
>    - Sample rows:
>      "'verify safety for bed 22' | 6.8s | 0.4 | 0.2 | 6.1"
>      "'rapid response trace ...' | 5.2s | 0.6 | 0.3 | 4.1"
>    - Header "Slow query log (top 50 slowest, 7d)"

---

### Brief D5 — Silent Abandonment Alerts

**Project name:** "LYNA Dashboard · D5 Abandonment"
**Mode:** High fidelity

**Prompt:**
> Design the **Silent Abandonment Alerts** page. Target user:
> unit manager. Answers "which nurses started using LYNA and
> stopped?" Anchored directly to H13. The "Reach out" affordance
> is the action.
>
> [paste LYNA design system block from §1]
>
> Global chrome same as D1.
>
> **Main content:**
> 1. Page header: "SILENT ABANDONMENT ALERTS" 28pt semibold.
> 2. Filter row: "Severity ▼" "Days since last query ▼"
> 3. **Aggregate card** (section card, summary):
>    - Title "Unit: 4-South"
>    - 4 stat lines (16pt regular primary):
>      "Currently active (7d): 31/38 nurses (82%)"
>      "90d baseline: 89% (–7% from baseline)"
>      "At-risk (severity ≥): 4 nurses"
> 4. **At-risk list card** (section card with red-tinted header
>    #FEE2E2 / #991B1B):
>    - Header "🔴 At-risk"
>    - Table columns: Nurse | Last 7d | Trend | Last query |
>      Severity (+ "Reach out →" affordance)
>    - Sample rows (each row 96pt to fit usage explanation):
>      "Devon P. | 12 | ▼▼ amber | 3d ago | Warning amber pill"
>      "Yvonne L. | 3 | ▼▼▼ red | 9d ago | Critical red pill"
>      "Carlos R. | 8 | ▼ amber | 1d ago | Watching amber"
>      "Maya T. | 5 | ▼▼ amber | 4d ago | Warning amber"
>    - Below each row's stats: a smaller explainer line
>      "Used 41/wk average for prior 4w"
>    - "Reach out →" link 14pt #2563EB right-aligned on each
>      row
> 5. **Reach-out template card** (section card):
>    - Header "Reach-out template:"
>    - Editable text area (4 lines) pre-filled with:
>      "Subject: Quick LYNA check-in
>       Hi {nurse} —
>       Noticed your LYNA usage has dropped this week.
>       Anything we can fix? Bug, friction, missing answer?
>       — {manager}"
>    - Bottom: 3 channel buttons (44pt each, 16pt gap):
>      "Send via Teams" "Send via Mattermost" "Send via email"
>      (each border-only NORMAL-blue)

---

### Brief D6 — Broadcast / Help Coverage

**Project name:** "LYNA Dashboard · D6 Broadcast Coverage"
**Mode:** High fidelity

**Prompt:**
> Design the **Broadcast / Help Coverage** page. Target user:
> unit manager + quality. Answers "is my unit responsive when
> someone asks for help?" Privacy: aggregate-only, no per-nurse
> responsiveness shown.
>
> [paste LYNA design system block from §1]
>
> Global chrome same as D1. Use BROADCAST orange (#F97316) as
> accent on this view where appropriate.
>
> **Main content:**
> 1. Page header: "BROADCAST / HELP COVERAGE" 28pt semibold.
> 2. Filter row: "Unit ▼" "Shift ▼" "7d ▼" "Category ▼"
> 3. KPI strip — 4 cards:
>    - "TOTAL BROADCASTS" / "142"
>    - "ACK WITHIN 30s" / "87% ✓" / "Target ≥85"
>    - "ACK WITHIN 60s" / "95% ✓" / "Target ≥95"
>    - "ESCALATIONS" / "3 (2%)" / "Target <5%"
> 4. **Response-time distribution chart** (section card):
>    - Histogram bars 0s to 2m+, orange #F97316 80% opacity
>    - Vertical reference line at 60s (red #DC2626)
>    - Title "Response-time distribution (4-South, 7d)"
> 5. **Per-shift comparison table** (section card):
>    - 5-column table: Unit | Day | Night | Weekday | Weekend
>    - Each cell shows percentage with ⚠ icon if below threshold
>    - Sample:
>      "4-South | 94% | 78% ⚠ | 92% | 82% ⚠"
>      "4-East  | 96% | 88%   | 95% | 89%"
>      "5-North | 91% | 74% ⚠ | 89% | 78% ⚠"
> 6. **Escalations table** (section card):
>    - Title "Escalations (when no one acked within timeout)"
>    - Columns: Time | Sender | Category | Notes
>    - Sample rows:
>      "03:14 | Priya | Supply | Devon was on break"
>      "04:38 | Maya  | Help   | No PCA on shift"
>      "07:22 | Sarah | Isolation | Iso-cart not stocked"

---

### Brief D7 — Critical Alerts Audit

**Project name:** "LYNA Dashboard · D7 Critical Alerts Audit"
**Mode:** High fidelity

**Prompt:**
> Design the **Critical Alerts Audit** page. Target user:
> quality / safety officer. Read-only audit of every rapid
> response / code blue / fall activation. PDF export per event
> for the hospital's standard post-event review packet.
>
> [paste LYNA design system block from §1]
>
> Global chrome same as D1.
>
> **Main content:**
> 1. Page header: "CRITICAL ALERTS AUDIT" 28pt semibold.
> 2. Filter row: "Unit ▼" "Alert type ▼" "30d ▼"
> 3. **Event log card** (section card with chronological list of
>    activations):
>    - Each event row ~120pt height, separated by 1pt
>      #E5E7EB divider:
>      - Top line (13pt medium secondary):
>        "Date · Time | Unit / Bed | Type | Activator"
>      - Type chip right-aligned: Rapid Resp (red), Code Blue
>        (deeper red), Fall (amber)
>      - Description line (16pt regular primary): scenario
>        summary
>      - Paged line (14pt regular #374151): "Paged: RRT ✓ ·
>        cardiology ✓ · charge ✓"
>      - Protocol line: "Protocol: NU-CARD-014 (ACS) —
>        surfaced ✓"
>      - Timing line: "ACKed in 6s · ended 04:52"
>      - Action links: "[Open full event →]  [Export PDF →]"
>        (12pt #2563EB)
>    - Sample 3 events:
>      "05-20 | 04:35 | 4-East / 6 | Rapid Resp | Sofia C.
>       ST changes, post-CABG day 2 [...]"
>      "05-19 | 14:22 | 5-North / 18 | Code Blue | Maria L.
>       Cardiac arrest, witnessed [...]"
>      "05-17 | 23:14 | 4-South / 22 | Fall | Linh T.
>       Witnessed fall from bed [...]"
> 4. **Aggregate summary card** at bottom:
>    - Title "Aggregate"
>    - 4 stat lines:
>      "This month: 14 activations (12 RR · 1 Code Blue · 1
>       Fall)"
>      "Median time-to-ACK: 5.2s ✓ (target ≤10s)"
>      "Median time-to-RRT-arrive: 87s ✓ (target ≤120s)"
>      "All events have protocol surfaced: ✓"
>      "All events have post-event PDF available: ✓"

---

### Brief D8 — Interpreter Sessions

**Project name:** "LYNA Dashboard · D8 Interpreter Sessions"
**Mode:** High fidelity

**Prompt:**
> Design the **Interpreter Sessions** page. Target user: clinical
> informatics + language services. Title VI compliance focus.
> Answers "how often is ad-hoc machine translation being used,
> and where should we add certified coverage?"
>
> [paste LYNA design system block from §1]
>
> Global chrome same as D1. Use INTERPRETER purple (#9333EA) as
> accent on this view.
>
> **Main content:**
> 1. Page header: "INTERPRETER SESSIONS" 28pt semibold.
> 2. Filter row: "Unit ▼" "Language ▼" "Certified hand-off ▼"
>    "30d ▼"
> 3. **Sessions-by-language card** (section card):
>    - Title "Sessions by language (30d)"
>    - Horizontal bar chart, one bar per language:
>      Spanish, Mandarin, Russian, Bengali, Korean,
>      then a divider line "── coverage line ──",
>      then Polish, Haitian Cr., Vietnamese
>    - Bars above the line are purple #9333EA; below are amber
>      #F59E0B with "🟡 Not in certified coverage" tag
>    - Bottom callout link: "Suggest expanding certified
>      coverage for: Polish, Haitian Cr., Vietnamese →"
> 4. **Certified hand-off rate card** (section card):
>    - 5 stat lines:
>      "Total sessions: 198"
>      "Sessions invoking 'queue cert': 31 (16%)"
>      "Median session length: 4.2 turns"
>      "Sessions ≥10 turns (long): 12 (6%) ⚠"
>      "Of those long sessions, how many invoked 'queue cert':
>       8 (67%)"
> 5. **Per-session detail table** (section card):
>    - Columns: Date | Time | Lang | Unit | Turns | Cert? |
>      Duration
>    - Sample rows:
>      "05-20 | 03:00 | Spanish  | 4-South | 5  | No    | 2:18"
>      "05-19 | 22:14 | Mandarin | 5-North | 12 | Yes ✓ | 18:42"
>      "05-19 | 19:47 | Spanish  | 6-South | 4  | No    | 1:53"
>    - Bottom: "Export compliance PDF for language services
>      audit →" (44pt button border-only purple)

---

### Brief D9 — Per-AI-Tool Detail

**Project name:** "LYNA Dashboard · D9 Per-Tool Detail"
**Mode:** High fidelity

**Prompt:**
> Design the **Per-AI-Tool Detail** drill-down page. Reached
> from a D2 "Drill into detail →" link. Target user: CCIO,
> walking into a vendor renewal conversation. The ROI estimate
> at the bottom is the artifact that ends up in the renewal
> meeting.
>
> [paste LYNA design system block from §1]
>
> Global chrome same as D1.
>
> **Main content:**
> 1. Back link: "◀ Back to AI tool routing" (12pt #2563EB).
> 2. Tool identity header:
>    - "NURSING REFERENCE AI" 28pt semibold primary
>    - "(registry ID: NU-AI-014 · added: 2025-09 · vendor: ___)"
>      14pt regular secondary
> 3. KPI strip — 5 cards:
>    - "ROUTED" / "587"
>    - "FIRST-TIME" / "37"
>    - "COVERAGE" / "84% ✓"
>    - "ISSUES" / "2 ⚠"
>    - "ESTIMATED VALUE/QRY" / "$4.20"
> 4. **Routing volume trend card** (section card, 90 days):
>    - Title "Routing volume (daily, 90d)"
>    - Sparkline bar chart NORMAL-blue, 90 daily bars
> 5. **Top intents card** (section card):
>    - Title "Top intents routed"
>    - 4-row table:
>      "Drug-drug interaction | 387×"
>      "Renal dose check | 112×"
>      "Pregnancy/lactation safety | 54×"
>      "Geriatric dosing | 34×"
> 6. **First-time exposures card** (section card):
>    - Title "First-time exposures (cumulative, 90d)"
>    - Cumulative line chart, NORMAL-blue stroke + fill
> 7. **Issues card** (section card):
>    - Title "Issues (last 14d)"
>    - 2-row table:
>      "05-18 | 14:22 | API 500 (vendor side) | Fallback to
>       LYNA"
>      "05-15 | 09:11 | Timeout 8s            | Fallback to
>       LYNA"
> 8. **ROI estimate card** (section card with NORMAL-blue tinted
>    background #EFF6FF):
>    - Title "ROI estimate"
>    - 7 stat lines (the key numbers in 18pt bold):
>      "Annual contract: **$48,000**"
>      "Routings (annualized): **~7,000**"
>      "Cost per routing: **$6.86**"
>      "Estimated value/qry: **$4.20** (LYNA-derived)"
>      "  (avoided pharmacy page / time saved / safety value)"
>      "ROI before LYNA: n/a (no usage data)"
>      "ROI with LYNA: **~ -0.39 currently** ⚠"
>      "  Vendor relationship: request usage data from vendor
>       to recalculate, or adjust contract structure"

---

### Brief D10 — Buyer-Facing ROI

**Project name:** "LYNA Dashboard · D10 Buyer ROI"
**Mode:** High fidelity

**Prompt:**
> Design the **Buyer-Facing ROI** page. Target user: CCIO + CNO
> + CFO. The PDF export from this page is what ends up in the
> CCIO's budget packet. The page renders identically to the PDF
> output to avoid surprises during the meeting.
>
> [paste LYNA design system block from §1]
>
> Global chrome same as D1.
>
> **Main content:**
> 1. Page header: "BUYER-FACING ROI" 28pt semibold.
> 2. Filter row: "Unit ▼" "Hourly rate ▼" "30d ▼"
> 3. **Headline card** — distinct visual treatment (gradient
>    #EFF6FF → #DBEAFE top → bottom, 1.5pt border #2563EB,
>    32pt padding, 16pt corner):
>    - Label "ESTIMATED TIME SAVED" 14pt bold uppercase
>      letter-spacing 1pt #1E40AF
>    - Headline value 56pt SF Pro Display Bold #1E40AF:
>      "~24 minutes per RN per shift (median)"
>    - 3 bullets 16pt regular primary:
>      "~46,800 RN-hours saved annually (across 4-South
>       deployment of 38 RNs over 365 days)"
>      "~$2,808,000 estimated annual value (at $60/hr fully
>       loaded RN rate)"
>    - Inverted-emphasis trio at bottom (large bold numbers):
>      "LYNA annual cost (this unit): $84,000"
>      "Net annual benefit: $2,724,000"
>      "ROI: ~3,243%"
> 4. **Sensitivity bounds table** (section card):
>    - Title "Sensitivity bounds"
>    - 4-row, 4-column table: row labels "Time saved", "Annual
>      value", "ROI"; columns "Conservative", "Base",
>      "Aggressive"
> 5. **Calculation breakdown card** (section card):
>    - Title "Calculation breakdown"
>    - Long body block with subsection "Avg query saves:" + 7
>      indented bullets:
>      "Workstation bypass: 2.5 min (vs walk + log in)"
>      "Senior-nurse bypass: 5.0 min (Interview #1 ref)"
>      "Policy-Tech bypass: 5.0 min (Interview #2 ref)"
>      "Pharmacist page: 40 min (Robert §4.6)"
>      "Charge handoff: 15 min (Marcus §4.3)"
>      "Sign-on: 20 min (Jamal §4.4)"
>      "Interpreter wait: 9 min (Maya §4.10 baseline)"
>    - Below: "Weighted by query mix: ~3.1 min average per
>      query" + "Queries per RN per shift: ~8.4 (D1 metric)"
>      + "→ Time saved per shift: ~24 min"
> 6. **Per-unit breakdown card** (section card):
>    - 3-row table: Unit | Queries/wk | Time saved/wk | Annual
>      value
> 7. Sticky footer (full-width, 60pt, white background, 1pt top
>    border):
>    - "Export to PDF for CCIO budget packet" button (240×48pt,
>      NORMAL-blue filled, ↗ icon right-aligned, 16pt semibold
>      white)
> 8. Bottom-of-content footnote (12pt italic secondary):
>    "Estimates anchored to I-Corps research (`hypothesis-map.md`
>     H1-H18; `interviews-index.md` BMC V2; `bots/shared/
>     reports/lyna-strategic-analysis.md`)."

---

## Part C — Composite per-journey flows (optional)

These are click-through prototypes that compose multiple v1
iPhone surfaces into a runnable user flow. Use them when you
want to demo a journey end-to-end, not just inspect individual
screens.

### Brief Journey 4.7 — Sofia rapid response (composite)

**Project name:** "LYNA v1 · Journey 4.7 Sofia"
**Mode:** High fidelity
**Composes:** S1.A → S1.B → S1.C → S5.A → S5.B → S5.C

**Prompt:**
> Build a clickable flow showing Sofia, a cardiac step-down
> nurse on 4-East, activating a rapid response for bed 6
> (ST changes, post-CABG day 2 patient). Use the
> already-prototyped screens for S1 and S5 if available;
> otherwise build them according to S1.A/B/C and S5.A/B/C
> briefs.
>
> [paste LYNA design system block from §1]
>
> **Flow sequence:**
> 1. **Screen 1 — S2 Home (Sofia's view).** Normal mode pill.
>    Wake-word prompt "Hey LYNA" visible.
> 2. **Screen 2 — S1.B Listening.** Waveform animating. Live
>    transcription preview: "rapid response bed six S T
>    changes".
> 3. **Screen 3 — S1.C Processing.** Latency badge "~3s".
>    Activity caption "Querying: emergency-intent path · paging
>    + FHIR + protocol pull (parallel)".
> 4. **Screen 4 — S5.A Critical Alert (full screen).** All the
>    detail from the S5.A brief; this is the moment of the
>    journey. ACK button prominent.
> 5. **Screen 5 — Status bar after ACK.** S5.B sticky banner at
>    top of S2 Home, showing "🔴 RR active · 4-East bed 6".
> 6. **Screen 6 — S5.C Protocol view.** Reached by tapping the
>    "View Protocol" affordance in S5.A. Shows the ACS
>    protocol from hospital policy NU-CARD-014 with checkboxes
>    next to each step.
> 7. **Screen 7 — End response.** "End response" action on S5.A
>    after the situation has resolved. Returns to S2 Home with
>    no sticky banner.

---

### Brief Journey 4.8 — Priya broadcast (composite)

**Project name:** "LYNA v1 · Journey 4.8 Priya"
**Mode:** High fidelity
**Composes:** S1.A → S1.B → S6a (sender) → S6b (receiver,
parallel)

**Prompt:**
> Build a clickable flow showing both sides of a broadcast:
> Priya in an isolation room asking for a saline flush, plus
> the receiving side (Devon, the PCA two rooms down).
>
> [paste LYNA design system block from §1]
>
> **Flow sequence (parallel views for sender + receiver):**
> 1. **Sender Screen 1 — S2 Home.** Priya's phone. Normal mode.
> 2. **Sender Screen 2 — S1.B Listening.** Transcription: "broad
>    cast four south I need a ten m L saline flush in three oh
>    five isolation".
> 3. **Sender Screen 3 — S6a Sender ack tracker.** Waiting for
>    ack, roster visible with 7 recipients all ○.
> 4. **Receiver Screen 1 — S2 Home with S6b banner overlay.**
>    Devon's phone (whatever he was on, but show S2). Banner at
>    top: "📢 Priya · 305 (iso) · Needs 10mL saline flush",
>    Acknowledge / Pass buttons.
> 5. **Receiver Screen 2 — After Devon taps Acknowledge.** Banner
>    momentarily shows "✓ Covering — heading to clean utility"
>    then auto-dismisses.
> 6. **Sender Screen 4 — S6a updates to "Broadcast covered".**
>    Green success state, "Devon picking it up, ETA 90 seconds,
>    Iso-room: gowning". Voice readback indicator (small icon)
>    showing the audio is playing in Priya's earpiece.

---

### Brief Journey 4.10 — Maya interpreter (composite)

**Project name:** "LYNA v1 · Journey 4.10 Maya"
**Mode:** High fidelity
**Composes:** S2 → S1.C → S7.A → S7.B

**Prompt:**
> Build a clickable flow showing Maya entering interpreter mode
> at 03:00 with Mr. Reyes (Spanish-only patient) at bedside.
>
> [paste LYNA design system block from §1]
>
> **Flow sequence:**
> 1. **Screen 1 — S2 Home.** Maya's phone. Normal mode.
> 2. **Screen 2 — Voice trigger.** "Interpreter mode, Spanish"
>    flowing through S1.B → S1.C.
> 3. **Screen 3 — S7.A Compliance modal.** Maya taps "Got it".
> 4. **Screen 4 — S7.B Active session.** Initial state, mode
>    pill in S2 background now INTERPRETER purple. Transcript
>    card showing the first turn (Maya's question + the Spanish
>    translation rendered).
> 5. **Screen 5 — S7.B mid-session.** Show after 4 turns, with
>    the active-speaker dot moved to the patient side (○ → ● on
>    Spanish line).
> 6. **Screen 6 — End interpreter.** Confirmation: "Interpreter
>    session ended at 03:03. Logged." Return to S2 Home normal
>    mode.

---

## 5. Cross-references

- [`opal-ui-wireframes-v1.md`](opal-ui-wireframes-v1.md) — ASCII
  wireframes for every surface (full detail for layout)
- [`opal-screen-designs-v1.md`](opal-screen-designs-v1.md) —
  pixel-perfect specs (full detail for dimensions / typography)
- [`opal-interaction-flows.md`](opal-interaction-flows.md) —
  canonical UX spec (what each surface does and why)
- [`manager-dashboard.md`](manager-dashboard.md) — canonical
  dashboard spec
- [`manager-dashboard-wireframes.md`](manager-dashboard-wireframes.md)
  — dashboard ASCII wireframes
- [`manager-dashboard-screen-designs.md`](manager-dashboard-screen-designs.md)
  — dashboard pixel specs
- [`opal-design-system.md`](opal-design-system.md) — full design
  system spec
- [`design-tokens.json`](design-tokens.json) — design tokens

---

**Last updated:** 2026-05-20
