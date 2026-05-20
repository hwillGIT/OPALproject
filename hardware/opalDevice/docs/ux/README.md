# LYNA UX/UI Documentation

This directory contains the user-experience and interface design
documentation for LYNA — the voice-first clinical-staff assistant
in the OPAL project.

After the I-Corps customer-discovery work landed (March 2026),
the form-factor focus for the first pilot is the **iPhone app
(v1)** plus a Bluetooth earpiece, not the dedicated touchscreen
device the earlier docs in this directory were drawn against.
The earlier docs are preserved as **v3 reference material** for
the eventual dedicated LYNA-badge design pass.

---

## Canonical v1 specs (current)

### **[opal-interaction-flows.md](opal-interaction-flows.md)** — START HERE
Per-journey UI flow specification for the v1 iPhone app:
- Form-factor pivot rationale (iPhone over dedicated device, v2 skipped)
- 10-surface inventory (S1–S10)
- Per-journey flows for §4.1–§4.10 of `INTELLIGENCE_LAYER.md`
- Reusable patterns (mode indicator, AI-source pill, citation footer,
  voice-surface states, execution-layer affordances, compliance moments)
- Cross-cutting error handling
- Mapping from the prior 8-flow draft

### **[opal-ui-wireframes-v1.md](opal-ui-wireframes-v1.md)**
ASCII wireframes for the 10 v1 iPhone surfaces (S1–S10), plus
per-journey screen sequences for §4.1–§4.10. Read alongside
`opal-interaction-flows.md` for layout context.

### **[opal-screen-designs-v1.md](opal-screen-designs-v1.md)**
Pixel-perfect specifications for the v1 iPhone screens (390 × 844 pt
viewport): voice surface states, response card variants, brain
sheet (unit + assignment), critical alert, broadcast composer + ack
tracker, interpreter session, camera handoff banner. Plus animation
specs and accessibility requirements.

### **[manager-dashboard.md](manager-dashboard.md)**
Companion spec for the web manager dashboard:
- 10 views (D1–D10) covering adoption, AI routing, top queries,
  response times, abandonment, broadcast coverage, critical alerts,
  interpreter sessions, per-tool detail, and buyer-facing ROI
- Anchored to H13 (silent abandonment), H6 (AI awareness gap), H10
  (CCIO needs ROI), H17/H18 (renewal economics)
- Privacy + PHI handling, data-source map, deferred work

### **[manager-dashboard-wireframes.md](manager-dashboard-wireframes.md)**
ASCII wireframes for the dashboard global chrome (top bar, left nav,
page header) + every view D1–D10.

### **[manager-dashboard-screen-designs.md](manager-dashboard-screen-designs.md)**
Pixel-perfect specs for the reusable dashboard patterns (KPI strip,
AI-tool card, heatmap, sparkline, distribution histogram, per-nurse
table, trend chips, filter bar, reach-out modal) plus
view-specific detail for D2 (AI-tool grid), D7 (audit log), and D10
(buyer-facing ROI). Includes PDF export specs.

### **[v3-design-alignment.md](v3-design-alignment.md)**
Mapping of the existing v3 device assets in this directory to the
10 journeys. Documents what's reusable, what's stale, what new v3
screens are required, and what hardware affordances the v1 spec
assumes v3 will eventually provide (ACK button, broadcast button,
RFID, bone-conduction audio, paired patient earpiece). The eventual
v3 design pass (post-v1 pilot) starts from this inventory.

---

## v3 reference material (dedicated LYNA badge — deferred design pass)

These docs were drawn against the dedicated touchscreen-device
concept (LVGL theme, large hardware buttons, small panel). They
remain valid reference for the eventual v3 design pass, and
several elements (design system, color palette, response-card
pattern, dashboard wireframe bones) are reusable for v1.

### **[opal-ui-wireframes.md](opal-ui-wireframes.md)** — v3 reference
Device UI wireframes (small touch screen) + dashboard wireframes.
The device wireframes carry forward to v3 (re-anchoring documented
in `v3-design-alignment.md`); the dashboard wireframes are
superseded by `manager-dashboard-wireframes.md`.

### **[opal-design-system.md](opal-design-system.md)** — **reusable as-is**
Color palette, typography, spacing, components. Used by v1 iPhone
specs and v3 device specs equally.

### **[opal-screen-designs.md](opal-screen-designs.md)** — v3 reference
v3 high-fidelity screens at 240 × 320 px. Useful as visual reference
for the eventual v3 design pass.

### **[design-tokens.json](design-tokens.json)** — **reusable as-is**
Design tokens in JSON for multi-platform use.

### **[IMPLEMENTATION_ROADMAP.md](IMPLEMENTATION_ROADMAP.md)** — v3 reference

---

## v1 design principles (current)

### **iPhone app (v1):**
- **Voice-first.** The screen exists to carry what voice can't —
  long structured output (brain sheet), persistent state
  (critical alert, interpreter session), bidirectional ack
  tracking (broadcast), and handoffs to apps LYNA doesn't own
  (Epic Haiku camera).
- **Mode-switching UX.** Three modes — NORMAL / BROADCAST /
  INTERPRETER. Always visible. Color-coded (blue / orange /
  purple).
- **Phone coexistence (H14).** LYNA never positions as a phone
  replacement. Camera-dependent workflows hand off to the phone
  cleanly.
- **Sub-2s round-trip.** The bypass-the-screen value disappears
  if LYNA is slower than asking a senior nurse. Latency is a
  first-class UX concern, tracked in the manager dashboard.
- **Every answer carries a citation.** Never silent. Never fake.

### **Manager dashboard:**
- **Reading view, not authoring view.** The dashboard is
  read-only over the memory event log, plus a curation queue
  ("add to KB" tasks for NI).
- **Privacy by scope.** Unit manager sees their unit; CNO+ sees
  cross-unit aggregates; per-nurse data stays unit-internal.
- **Anchored to H13 / H6 / H10 / H17 / H18.** Every view answers
  a question one of those hypotheses says is currently
  unanswerable.

---

## Form-factor scope

| Form factor | Status | Reference |
|---|---|---|
| **v1 — iPhone app + Bluetooth earpiece** | **Active design** | `opal-interaction-flows.md`, `manager-dashboard.md` |
| v2 — Vocera-class wearable / Apple Watch | **Skipped** intentionally (Interview #2 anti-signal) | n/a |
| **v3 — Dedicated LYNA badge** | Deferred design pass after v1 pilot data | wireframes / screen-designs / LVGL theme |

---

## Related Epics

- **SCRUM-33**: User Experience & Interface
- **SCRUM-34**: Demo & Pilot Programs (dashboard visualization)

---

## Implementation Files

### **[implementation/](implementation/)**
Ready-to-use implementation files:
- `html-mockups/` — HTML/CSS visual mockups (v3 reference;
  patterns reusable for v1 web pages and the manager dashboard)
- `html-prototype/` — Interactive HTML prototype (v3 reference)
- `lvgl-theme/` — LVGL theme for the v3 device UI
- `react-dashboard/` — React dashboard skeleton, **v1 starting
  point for `manager-dashboard.md`**

---

**Last Updated:** 2026-05-20

