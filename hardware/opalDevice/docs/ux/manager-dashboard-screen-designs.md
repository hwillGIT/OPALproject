# LYNA Manager Dashboard — Pixel-Perfect Specs

**Date:** 2026-05-20
**Surface:** Web app (desktop primary)
**Companion to:** [`manager-dashboard-wireframes.md`](manager-dashboard-wireframes.md)
**Design system:** [`opal-design-system.md`](opal-design-system.md)
+ [`design-tokens.json`](design-tokens.json) — colors, typography
reusable as-is

This doc specs the **reusable patterns** that compose the 10
dashboard views (D1–D10), plus pixel-level detail for views with
novel layout (the AI-tool card, the heatmap, the broadcast
response distribution, the buyer-ROI breakdown).

Standard table rows, filter bars, modal sheets, and section
headers follow the design system + the wireframes — not re-spec'd
here.

---

## 0. Layout grid

```
Breakpoints:
  Desktop (≥1280):   8-col grid, 24 pt gutters, 32 pt margin
  Tablet (1024-1279): 6-col grid, 20 pt gutters, 24 pt margin
  Below 1024:        Single-col stack, no grid
```

**Vertical rhythm:** 8 pt baseline.

**Card spacing:** 24 pt between cards on desktop; 16 pt on tablet.

**Page padding:** 32 pt top/bottom, 32 pt sides on desktop (24 pt
on tablet).

---

## 1. Global chrome

### 1.1 Top bar

```
Height:           60 pt
Background:       #FFFFFF
Border-bottom:    1 pt #E5E7EB
Padding:          12 pt 32 pt
```

**Left cluster:** logo (24 pt SF Pro Display Semibold `#111827`)
+ org/scope label (16 pt Regular `#374151`, separated by " · ").

**Right cluster:** user identity (16 pt Medium `#111827`) + role
chip (12 pt Bold uppercase, 4 pt × 8 pt padding, background
`#F3F4F6`, color `#6B7280`, corner radius 4 pt) + settings icon
(24 × 24 pt, `#6B7280`) + sign-out chevron.

### 1.2 Left nav

```
Width:            240 pt
Background:       #F9FAFB
Border-right:     1 pt #E5E7EB
Padding:          24 pt 0
```

Per nav item:
```
Height:           48 pt
Padding:          12 pt 24 pt
Text:             16 pt SF Pro Text Regular #374151
Active state:     Background #EFF6FF
                  Border-left 4 pt #2563EB
                  Text #2563EB Semibold
Hover state:      Background #F3F4F6
```

Divider between nav groups: 1 pt `#E5E7EB`, 16 pt margin top/bottom.

### 1.3 Page header

```
Height:           Variable (88 pt min, expands with filter row)
Background:       #FFFFFF
Padding:          24 pt 32 pt
Border-bottom:    1 pt #E5E7EB
```

- Title: 28 pt SF Pro Display Semibold `#111827`
- Subtitle (optional): 16 pt Regular `#6B7280`
- KPI strip (when present): full-width, 80 pt height, 16 pt gap
  between cards
- Filter row: 56 pt height, horizontal scroll if needed

---

## 2. Reusable patterns

### 2.1 KPI card

The 4-cell strip at the top of D1, D6, etc.

```
Container:        Flex row, 16 pt gap
Each card:        Equal width, 80 pt height
Card background:  #FFFFFF
Card border:      1 pt #E5E7EB
Card padding:     16 pt
Card corner:      12 pt
```

**Content layout:**
- Label (top): 13 pt SF Pro Text Medium, uppercase, `#6B7280`,
  letter-spacing 0.5 pt
- Value (middle): 32 pt SF Pro Display Bold, `#111827`
- Delta (bottom right): 14 pt Semibold; color = `#10B981` (up,
  positive) / `#EF4444` (down, negative); icon ▲ or ▼

### 2.2 Section card

Used throughout (top queries column, broadcast distribution,
AI-tool card, etc.).

```
Background:       #FFFFFF
Border:           1 pt #E5E7EB
Corner radius:    12 pt
Padding:          24 pt
Shadow:           0 1 pt 2 pt rgba(0,0,0,0.04)
```

**Header bar (optional, for sectioned cards like D4 brain-sheet
inheritance):**
- Height: 40 pt
- Background: color-coded per section type (red/amber/blue/purple
  tints matching the brain-sheet pattern in v1)
- Header text: 13 pt SF Pro Text Bold uppercase, color matches
  border-darker variant

### 2.3 AI-tool card (D2's main pattern)

The most-novel pattern. Each tool gets a card.

```
Container:        Section card pattern
Min height:       180 pt
```

```
┌────────────────────────────────────────────────────────────┐
│ [Tool name]                            [Status chip]       │
│ (24 pt Semibold #111827)               (right-aligned)     │
│                                                            │
│ Registry: ID · Vendor · Integration                        │
│ (13 pt Regular #6B7280, all on one row, separated by ·)    │
│                                                            │
│ ──── 16 pt spacer ────                                     │
│                                                            │
│ ┌────────┬────────┬────────┬─────────┬─────────────┐      │
│ │ Today  │ 7d     │ 30d    │Coverage │ First-time  │      │
│ │ 24     │ 142    │ 587    │ 84% ✓   │ 12 nurses   │      │
│ └────────┴────────┴────────┴─────────┴─────────────┘      │
│                                                            │
│ ──── 16 pt spacer ────                                     │
│                                                            │
│ (Sparkline, full-width, 48 pt height)                      │
│  ▆▆▆▇▇▆▆█████▇▇█████▇▆▇▇█████▇                            │
│                                                            │
│ ──── 16 pt spacer ────                                     │
│                                                            │
│ [Drill into detail →]    (text link, 14 pt #2563EB)        │
└────────────────────────────────────────────────────────────┘
```

**Status chip:**
- 24 pt height, 12 pt padding sides, 12 pt corner radius
- States:
  - ✓ Healthy → background `#D1FAE5`, text `#047857`
  - ⚠ Issues → background `#FEF3C7`, text `#92400E`
  - 🟡 No traffic → background `#FEF3C7`, text `#92400E`
  - 🔴 Coverage low → background `#FEE2E2`, text `#991B1B`

**Inline metric row:**
- 5 cells, 16 pt gap, top-border 1 pt `#E5E7EB`
- Each cell: label (13 pt Medium uppercase `#6B7280`) + value
  (20 pt Bold `#111827`)

**Sparkline:**
- Width: full card width
- Height: 48 pt
- Color: `#2563EB` (or status-color tint)
- Block characters in wireframes are placeholders; real
  implementation uses SVG path with 1.5 pt stroke + filled area
  at 12% opacity

### 2.4 Heatmap (D1)

```
Cell size:        24 × 24 pt
Row label width:  120 pt
Column count:     24 (hour-of-day)
Total width:      120 + (24 × 24) + (23 × 4) = 788 pt
Row gap:          8 pt
Column gap:       4 pt
```

**Color scale (5 buckets):**
- None (0 queries): `#F9FAFB`
- Low (1–3): `#DBEAFE`
- Medium (4–10): `#93C5FD`
- High (11–25): `#3B82F6`
- Peak (>25): `#1E40AF`

**Row label:** 14 pt SF Pro Text Medium `#374151`, right-aligned.

**Hover:** tooltip with exact count + comparison to baseline.

**Tap (mobile):** sticky tooltip below the cell.

### 2.5 Sparkline (used in D1, D2, D9)

```
Default:
  Height:         32 pt (compact) or 48 pt (standard)
  Stroke:         1.5 pt #2563EB
  Fill:           #2563EB at 12% opacity
  Axis:           Hidden by default; visible on hover
```

**With baseline reference:**
- Add dashed horizontal line at the baseline value (1 pt
  `#9CA3AF`, dash 4-2)
- Annotation on right: baseline value (12 pt `#6B7280`)

### 2.6 Distribution histogram (D4 latency, D6 response time)

```
Container:        Section card pattern
Height:           240 pt total (200 pt for bars + 40 pt for axis)
Bar width:        Adaptive, 4 pt min, 32 pt max, 4 pt gap
Bar color:        #2563EB at 80% opacity
Threshold line:   2 pt solid #DC2626 (the 2s target)
                  + dashed extension to top
Axis labels:      12 pt #6B7280 Regular
```

**Below the histogram:** percentile summary row (p50, p75, p95)
in 14 pt SF Pro Text Medium with the green check ✓ if all are
under threshold; orange ⚠ otherwise.

### 2.7 Per-nurse / per-tool table (D1, D5)

```
Container:        Section card pattern
Row height:       56 pt
Header height:    44 pt
Header background:#F9FAFB
Header text:      13 pt SF Pro Text Bold uppercase #374151
Row text:         16 pt SF Pro Text Regular #111827
Row divider:      1 pt #F3F4F6
Hover state:      Background #F9FAFB
Tap target:       Full row
```

**Status column rendering:**
- Power user (top quartile): green pill `#D1FAE5` / `#047857`
- Active: gray pill `#F3F4F6` / `#374151`
- Watching: amber pill `#FEF3C7` / `#92400E`
- Inactive: red pill `#FEE2E2` / `#991B1B`

### 2.8 Trend chips (▲▼─)

Used in the per-nurse table and per-tool detail.

```
Format:          ▲ for up, ▼ for down, ─ for flat
Repeated chars   for magnitude:
  ▲   slight increase
  ▲▲  notable increase
  ▲▲▲ strong increase
  ─   flat (no notable change)
  ▼   slight decrease
  ▼▼  notable decrease
  ▼▼▼ strong decrease (likely abandonment signal)
Color:           Green #10B981 for ▲, gray #6B7280 for ─,
                 amber #F59E0B for ▼ and ▼▼, red #EF4444 for ▼▼▼
Font:            14 pt SF Mono Bold (monospace for alignment)
```

### 2.9 Reach-out modal (D5)

Standard modal, 480 × 360 pt, centered, dimmed backdrop.

```
┌─────────────────────────────────────────────┐
│ ✕ Cancel                  Reach out to Devon│
├─────────────────────────────────────────────┤
│ Subject: Quick LYNA check-in                │
│ ─────                                       │
│ Hi Devon,                                   │
│                                             │
│ Noticed your LYNA usage has dropped this    │
│ week. Anything we can fix? Bug, friction,   │
│ missing answer?                             │
│                                             │
│ — Marcus                                    │
│                                             │
│ ┌──────────────────────────────────────┐   │
│ │ (edit field, 4 lines, 320 pt wide)   │   │
│ └──────────────────────────────────────┘   │
├─────────────────────────────────────────────┤
│ Send via:                                   │
│ ┌────────┐ ┌────────┐ ┌────────┐            │
│ │ Teams  │ │Matterm-│ │ Email  │            │
│ └────────┘ └────────┘ └────────┘            │
└─────────────────────────────────────────────┘
```

Channel choice depends on hospital config (per-site Operational
KB).

### 2.10 Filter bar

```
Container:        Flex row, 12 pt gap, wraps to second row if needed
Each filter pill: Height 36 pt, padding 8 pt 16 pt, corner 18 pt
                  Background #F3F4F6
                  Border 1 pt #E5E7EB
                  Text 14 pt SF Pro Text Medium #374151
                  Dropdown chevron ▼ 12 pt #6B7280
Active filter:    Background #DBEAFE
                  Border #2563EB
                  Text #1E40AF
```

---

## 3. D2 specifics — AI tool grid

D2 is the most strategically important view (CCIO renewal
conversations). The tool cards stack vertically in a single
column on desktop (not a grid), because each card is dense and
benefits from full width.

**Sort options at top:**
```
Sort by:  [Volume ▼]  [Coverage]  [First-time exposures]  [Issues]
```

Active sort: filled background; inactive: outline only.

---

## 4. D7 specifics — Audit log

The audit log (D7) is a chronological list with per-event detail
on tap. Each row is a section card with a header indicating event
type:

```
Container:        Section card pattern, no inner section header
Padding:          16 pt
Row height:       Adaptive (96 pt typical, more if event has long
                  description)
```

**Event row layout:**
```
Date · Time  Unit / Bed    Type            Activator
(13 pt Medium #6B7280)     (14 pt Bold)    (right-aligned)

Description (16 pt Regular #111827, 2-line max with ellipsis)

Compact metrics row (14 pt Regular #374151):
Paged: X ✓ · Protocol: Y · ACK: Zs

[Open full event →]  [Export PDF →]
(12 pt #2563EB, link styling)
```

**Event-type chip on the right:**
- "Rapid Resp" → `#FEE2E2` / `#991B1B`
- "Code Blue" → `#FECACA` / `#7F1D1D` (deeper red)
- "Fall" → `#FEF3C7` / `#92400E`
- Other → `#F3F4F6` / `#374151`

---

## 5. D10 specifics — ROI calculator

D10 is the buyer-facing PDF export source. The page renders
identically to the PDF output to avoid surprises during the CCIO
meeting.

**Top "headline" card** uses a distinct visual treatment:
```
Background:       Gradient #EFF6FF → #DBEAFE (top → bottom)
Border:           1.5 pt #2563EB
Padding:          32 pt
Corner radius:    16 pt
```

**Inside:**
- Label "ESTIMATED TIME SAVED": 14 pt Bold uppercase
  letter-spacing 1 pt `#1E40AF`
- Headline value (largest text on the page): 56 pt SF Pro Display
  Bold `#1E40AF` — "~24 minutes per RN per shift (median)"
- Supporting bullet list: 16 pt Regular `#111827`, 4 lines
- LYNA annual cost / Net annual benefit / ROI rendered as a
  inverted-emphasis trio at the bottom of the card

**Sensitivity table:** standard 4-column table, headers and rows
follow §2.7 pattern.

**Calculation breakdown:** standard section card, list of bullets,
with the I-Corps research source footnote at the bottom in
12 pt Italic `#6B7280`.

**Export-to-PDF button:** sticky footer, full-width on tablet,
right-aligned (240 × 48 pt) on desktop. Background `#2563EB`,
text "Export to PDF for CCIO budget packet" 16 pt Semibold
`#FFFFFF`, icon ↗ on the right.

---

## 6. Animation specifications

| Element | Duration | Easing | Notes |
|---|---|---|---|
| Sparkline draw-in | 600 ms | ease-out | On view mount; staggered 100 ms per card |
| Trend chip color fade | 200 ms | linear | When data refreshes |
| Heatmap cell hover | 100 ms | linear | Tooltip fade-in |
| KPI card mount | 300 ms | ease-out | Stagger 80 ms across the row |
| Modal slide-in | 250 ms | spring | Standard iOS/web modal |
| Status-chip pulse | 1200 ms | ease-in-out | For "issues this week" warning |

---

## 7. Responsive behavior

### Desktop (≥1280)
- Full layout as specified
- AI-tool cards: 1 per row, full width

### Tablet (1024–1279)
- Left nav collapses to icon-only (60 pt wide), labels show on
  hover
- KPI cards: 2 × 2 grid instead of 1 × 4
- AI-tool cards: 1 per row, full width
- Filter pills: wrap to second row if needed

### Below 1024
- Left nav collapses to hamburger menu
- All cards stack vertically, full-width
- Per-nurse table becomes a list of cards (16 pt padding each)
- Heatmap scrolls horizontally with sticky row labels

Note: the dashboard is not optimized for phone viewing. The
target user is at a workstation or large tablet.

---

## 8. Accessibility

Same as `opal-screen-designs-v1.md` §10 plus:

- **Charts:** every chart has a sibling `<table>` with the
  underlying data, hidden visually but accessible to screen
  readers
- **Color-only info:** every color-coded element (status chips,
  trend chips, heatmap) also carries text or icon
- **Keyboard navigation:** every interactive element reachable via
  tab; visible focus ring (2 pt `#2563EB`)
- **High contrast mode:** all card backgrounds darken to preserve
  text contrast; status chips become solid colored backgrounds
  instead of tinted

---

## 9. PDF export specs (D7 audit, D10 ROI)

**Page size:** US Letter (8.5 × 11 in) portrait.

**Margins:** 0.75 in all sides.

**Header (every page):**
- Hospital logo (top-left, 1 × 1 in max)
- LYNA wordmark (top-right, 16 pt)
- Title (centered, 20 pt Bold)

**Footer (every page):**
- Generated date + time (left, 9 pt)
- Page X of Y (center, 9 pt)
- "Data current as of HH:MM" (right, 9 pt)
- 1 pt `#E5E7EB` rule above footer

**Compliance attribution footer (last page only):**
- "Generated by LYNA Manager Dashboard · Source: hospital-side
  memory event log · Anchored to I-Corps customer-discovery
  research (H1–H18)"
- 8 pt SF Pro Text Regular `#6B7280`
- Plus the per-document file references where applicable

---

## 10. Cross-references

- [`manager-dashboard.md`](manager-dashboard.md) — canonical spec
- [`manager-dashboard-wireframes.md`](manager-dashboard-wireframes.md) — ASCII wireframes
- [`opal-design-system.md`](opal-design-system.md) — design system
  (reusable as-is)
- [`design-tokens.json`](design-tokens.json) — tokens
- [`implementation/react-dashboard/`](implementation/react-dashboard/) — implementation skeleton

---

**Last updated:** 2026-05-20
