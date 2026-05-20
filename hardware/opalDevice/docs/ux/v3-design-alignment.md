# LYNA v3 Design Alignment — Mapping the Old Device Concept to the 10 Journeys

**Date:** 2026-05-20
**Form factor:** v3 — dedicated LYNA badge (ESP32-C6 + small touch
screen + ES8311 audio codec + RFID + bone-conduction audio +
magnetic charging)
**Scope:** Map the existing v3 design assets in this directory to
the 10 LYNA clinical-staff journeys in
[`INTELLIGENCE_LAYER.md`](../../../../INTELLIGENCE_LAYER.md) §4,
identify what's reusable, what's stale, and what new v3 screens
are required.
**Status:** Pre-design pass. Does NOT redesign v3; documents the
alignment so the eventual v3 design pass (post-v1-pilot) starts
from a clean inventory.

**v3 is deferred:** the canonical active form factor is v1
iPhone. See [`opal-interaction-flows.md`](opal-interaction-flows.md)
and [`opal-ui-wireframes-v1.md`](opal-ui-wireframes-v1.md) for
the v1 spec. The v3 hardware pass happens after v1 pilot data
lands.

---

## 1. The existing v3 assets in this directory

| File | Status | Notes |
|---|---|---|
| [`opal-ui-wireframes.md`](opal-ui-wireframes.md) | **v3 reference, partly stale** | Device UI wireframes for the small touch screen; dashboard wireframes have been superseded by [`manager-dashboard-wireframes.md`](manager-dashboard-wireframes.md) |
| [`opal-design-system.md`](opal-design-system.md) | **Reusable as-is** for v1 + v3 | Colors, typography, spacing, components. The mode-color scheme (blue/orange/purple) is the canonical design language across all form factors. |
| [`opal-screen-designs.md`](opal-screen-designs.md) | **v3 reference** | Pixel-perfect specs for the 240 × 320 px device screen. Needs re-anchoring against the 10 journeys; see §3 below. |
| [`design-tokens.json`](design-tokens.json) | **Reusable as-is** | Cross-platform tokens |
| [`implementation/lvgl-theme/`](implementation/lvgl-theme/) | **v3-specific** | LVGL theme for the embedded device. Not used by v1 iPhone. |
| [`implementation/html-mockups/`](implementation/html-mockups/) | **v3 reference** | HTML mockups against the v3 screens. Patterns reusable for v1 web pages and manager dashboard. |
| [`implementation/react-dashboard/`](implementation/react-dashboard/) | **Active for manager dashboard** | Implementation starting point for `manager-dashboard.md`. |

---

## 2. Old 8-flow → new 10-journey mapping (v3-specific re-anchoring)

The `opal-ui-wireframes.md` device wireframes were drawn against
the 8 flows in the original (now-superseded) interaction-flows
draft. Here's how those wireframed screens map to the 10
canonical journeys.

| Old screen (v3 wireframe) | New v3 mapping | Status |
|---|---|---|
| Screen 1: Idle/Home | Used by every journey — analog of v1 S2 Home | **Keep**; minor copy update ("OPAL" → "LYNA") |
| Screen 2: Mode Selection | §4.8 + §4.10 entry; reusable mode-switcher | **Keep**; add INTERPRETER (purple) as a third mode |
| Screen 3: Voice Command (Listening) | Used by every journey — analog of v1 S1.B | **Keep**; identical pattern |
| Screen 4: Active Call | Used by §4.7 cardiology paging | **Keep as variant**; not its own journey but used as a sub-pattern |
| Screen 5: Call Connecting | Same as Screen 4 | **Keep** |
| Screen 6: Broadcast | §4.8 Priya | **Keep**; add first-acknowledge-wins UX (was missing in old draft) |
| Screen 7: Critical Alert | §4.7 Sofia | **Keep**; protocol-surface affordance needs to escalate to phone (v3 screen too small for full protocol) |
| Screen 8: Interpreter Mode | §4.10 Maya | **Keep**; add compliance-modal entry + queue-interpreter hand-off |
| Screen 9: Settings | S10 on v1, equivalent on v3 | **Keep**; minor revisions |

---

## 3. Per-journey v3 coverage gaps

For each of the 10 journeys, what v3 screens exist, what's
missing, and what hardware affordance is the right answer.

### Journey 4.1 — Sarah, bedside med lookup

**Existing v3 coverage:** Home + Voice Command screens already
exist.

**Gaps:** None. v3 plays this voice-only with response readback
through bone-conduction audio. Mini display can render a
glanceable response card (dose + time + due-time) but optional.

**New v3 screens needed:** None.

### Journey 4.2 — Linh, float onboarding

**Existing v3 coverage:** Voice command + voice readback.

**Gaps:** None. Voice-only flow.

**New v3 screens needed:** None.

### Journey 4.3 — Marcus, charge handoff (28-patient brain sheet)

**Existing v3 coverage:** Voice command exists; brain-sheet
display does NOT.

**Gaps:** The 28-patient brain sheet is too dense for the v3
mini-display. The v3 device cannot reasonably render this.

**New v3 screens needed:** None. **Decision:** Marcus holds the
v1 phone for this flow even if he has a v3 badge. The v3 badge
handles voice trigger + voice readback only; the brain sheet
casts to the unit tablet or the workstation via SMART app launch.

### Journey 4.4 — Jamal, sign-on summary (4-patient brain sheet)

**Existing v3 coverage:** Voice command exists; assignment brain
sheet does NOT.

**Gaps:** Same as 4.3 — too dense for v3 mini-display.

**New v3 screens needed:** None. **Decision:** Jamal uses phone
for the brain sheet; v3 badge is voice-only on this flow.

### Journey 4.5 — Tanya, policy lookup

**Existing v3 coverage:** Voice command + voice readback.

**Gaps:** None. Voice-only flow; v3 mini-display optionally shows
the policy number for citation.

**New v3 screens needed:** None.

### Journey 4.6 — Robert, AI-tool routing

**Existing v3 coverage:** Voice command + voice readback.

**Gaps:**
- **AI-source pill** moment — v1 has it as a prominent S3 card
  affordance; v3 needs a minimal equivalent (the "I'm routing
  through {tool}" voice readback carries most of the weight)
- **First-time exposure card** — too long for v3 mini-display;
  defer to v1 phone view when first-time. v3 plays the voice
  readback and pings the phone in the nurse's pocket to surface
  the card.

**New v3 screens needed:** None new; pattern is "voice carries
the moment, phone gets the detail card."

### Journey 4.7 — Sofia, rapid response

**Existing v3 coverage:** Critical Alert wireframe exists (old
Screen 7).

**Gaps:**
- Old Critical Alert was designed for a touchscreen; v3 hardware
  also has a **dedicated hardware ACK button** (firm tactile
  click). Need to spec the hardware button + visual on the
  mini-display.
- Protocol view escalates to the phone (mini-display too small
  for full protocol). v3 spec needs to wire the "protocol view"
  affordance to a phone hand-off, mirroring §4.9's pattern.
- Vitals view also escalates to phone.

**New v3 screens needed:**
- v3-S5.A — Critical alert minimal view (rapid-response title,
  unit/bed, big visual ACK indicator + hardware button confirm)
- v3-S5.B — Status-pill banner (post-ACK) on the mini-display

### Journey 4.8 — Priya, broadcast

**Existing v3 coverage:** Broadcast wireframe exists (old Screen
6).

**Gaps:**
- First-acknowledge-wins tracker — old draft didn't have this
- **Hardware broadcast button** — v3 has a dedicated firm-click
  hardware button for broadcasts (faster than wake word + voice
  in noisy unit)
- Receiver banner — needs a v3 equivalent that doesn't take over
  the mini-display

**New v3 screens needed:**
- v3-S6a — Sender ack-tracker view (compact roster + first-ack
  indicator)
- v3-S6b — Receiver minimal notification (LED + haptic + voice;
  visual confirmation on mini-display)

### Journey 4.9 — Aisha, camera handoff

**Existing v3 coverage:** None. v3 has no camera.

**Gaps:** The whole journey is about handing off TO the phone for
camera-dependent work. v3 needs a minimal "go to your phone"
indication.

**New v3 screens needed:**
- v3-S8 — Phone-handoff banner (mini-display shows "Open Haiku
  on your phone" + LED indicator pointing nurse to phone)

### Journey 4.10 — Maya, interpreter session

**Existing v3 coverage:** Interpreter mode wireframe exists (old
Screen 8).

**Gaps:**
- Compliance modal — old draft didn't have it
- **Paired bedside earpiece for the patient** — v3-specific
  capability; v1 routes patient audio through the phone speaker,
  v3 routes through a paired patient earpiece for privacy in
  shared rooms. Need to spec the pairing flow + the active-session
  indicator that includes "Patient earpiece: paired" status.
- Per-turn transcript on the mini-display — needs to be tight (3
  lines max, scrollable via touch)

**New v3 screens needed:**
- v3-S7.A — Compliance entry modal (3-line text + "Got it" big
  button + hardware button confirm)
- v3-S7.B — Active session compact view (active-speaker indicator
  + last-1-turn transcript + "End session" affordance)
- v3-S7.C — Patient earpiece pairing flow (pre-session; pairs the
  bedside earpiece for the patient)

---

## 4. v3 hardware affordances the v1 spec assumes

The v1 iPhone spec uses only software affordances (touch, voice).
v3 hardware adds:

| Affordance | Used by | v1 substitute |
|---|---|---|
| **Hardware ACK button** (firm click) | §4.7 critical alert | Touch ACK on full-screen S5.A |
| **Hardware broadcast button** (firm click) | §4.8 broadcast | Voice trigger or mode-switch + touch on S2 |
| **Bone-conduction audio** | All voice readback | Bluetooth earpiece + phone speaker fallback |
| **RFID badge tap** (hardware) | §9 login | Phone NFC (if available) or camera-based badge scan |
| **Magnetic charging** | Always-on availability | iPhone charging |
| **Paired patient earpiece** | §4.10 interpreter, shared rooms | Phone speaker on bedside tray |
| **Indicator LEDs** | §4.7, §4.8, §4.9 escalation cues | Phone push notifications + haptic |

---

## 5. v3 mini-display constraints

The v3 device has a small touch screen (per
`opal-ui-wireframes.md`, "likely 1.69" or similar," typical
240 × 320 px). All v3 screen designs must respect:

- **Single primary action per view.** No long lists of options.
- **Glove-friendly touch targets** (≥44 × 44 px).
- **Bone-conduction audio is primary**; the screen is for
  glanceable visual confirmation only.
- **High contrast required**; clinical lighting varies wildly
  from bedside (bright) to night-shift hallway (dim).
- **No dense data**; brain sheets, full protocols, AI-source
  detail cards all escalate to the phone via SMART app launch.

Screens that need real estate (brain sheet, full protocol, full
response card with AI-source detail) deliberately escalate to
the phone. **The v3 device is a hands-free voice surface with
minimal visual confirmation — it is not a small smartphone.**

---

## 6. The eventual v3 design pass — work plan

Out of scope for this doc; documented here as the next-pass
roadmap.

1. **Re-anchor `opal-ui-wireframes.md`** against the 10 journeys.
   Update copy (OPAL → LYNA), remove dashboard wireframes (moved
   to `manager-dashboard-wireframes.md`), add the missing
   v3-S5.A/B, v3-S6a/b, v3-S7.A/B/C, v3-S8 screens identified in
   §3 above.
2. **Re-anchor `opal-screen-designs.md`** with the same set of
   screens at pixel-perfect detail for the actual hardware
   resolution.
3. **Spec the hardware affordances** in §4 — ACK button,
   broadcast button, RFID, bone-conduction audio, indicator LEDs,
   paired patient earpiece. Includes hardware-firmware contract.
4. **Update `implementation/lvgl-theme/`** to match the new
   screen specs.
5. **Update `IMPLEMENTATION_ROADMAP.md`** to reflect v3 as a
   post-v1-pilot work stream.

This is approximately the scope of the prior v3 design work — but
informed by v1 pilot data and the I-Corps research, which the
prior work was not.

---

## 7. Cross-references

- [`INTELLIGENCE_LAYER.md`](../../../../INTELLIGENCE_LAYER.md) §4
  — the 10 canonical journeys all v3 work must support
- [`opal-interaction-flows.md`](opal-interaction-flows.md) —
  v1 UX spec; the v3 design pass will reuse most of the surface
  inventory and reusable patterns
- [`opal-ui-wireframes-v1.md`](opal-ui-wireframes-v1.md) — v1
  ASCII wireframes; the v3 design pass adapts to the smaller
  hardware
- [`opal-ui-wireframes.md`](opal-ui-wireframes.md) — v3
  reference, partially stale (see §1)
- [`opal-screen-designs.md`](opal-screen-designs.md) — v3
  pixel-perfect reference, needs re-anchoring (see §6)
- [`README.md`](README.md) — index distinguishing v1 active from
  v3 reference

---

**Last updated:** 2026-05-20
**Next:** v3 design pass after v1 pilot data lands.
