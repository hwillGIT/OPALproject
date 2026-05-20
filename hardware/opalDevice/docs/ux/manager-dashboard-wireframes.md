# LYNA Manager Dashboard — Wireframes

**Date:** 2026-05-20
**Surface:** Web app (responsive desktop / large tablet)
**Companion to:** [`manager-dashboard.md`](manager-dashboard.md)
(canonical spec — read first for view purposes, hypothesis
anchors, and data sources)
**Pixel-perfect specs:** [`manager-dashboard-screen-designs.md`](manager-dashboard-screen-designs.md)

ASCII wireframes for the 10 views (D1–D10), plus the global
chrome (nav, header, filters).

---

## 0. Layout system

**Target:** desktop (1440 × 900 minimum), responsive down to
tablet (1024 × 768). Below 1024 the dashboard degrades
gracefully to a stacked view but is not optimized for phone
(nurses don't use the dashboard).

**Global structure:**
```
┌──────────────────────────────────────────────────────────────────┐
│  Top bar (60 pt): logo + org + user + sign out                   │
├──────────┬───────────────────────────────────────────────────────┤
│          │  Page header (88 pt): title + KPI strip + filters     │
│   Left   ├───────────────────────────────────────────────────────┤
│   nav    │                                                       │
│  (240    │       Main content area                               │
│   pt)    │                                                       │
│          │                                                       │
└──────────┴───────────────────────────────────────────────────────┘
```

**Left nav items:**
- Overview (D1)
- AI tool routing (D2)
- Top queries (D3)
- Response times (D4)
- Abandonment alerts (D5)
- Broadcast coverage (D6)
- Critical alerts audit (D7)
- Interpreter sessions (D8)
- Per-tool detail (D9, drills from D2)
- Buyer ROI (D10)
- ── divider ──
- Settings

---

## 1. Top bar (global)

```
┌──────────────────────────────────────────────────────────────────┐
│ [LYNA] Mt. Sinai · 4-South        ↳ Marcus Wells (Mgr)  ⚙ ↗     │
└──────────────────────────────────────────────────────────────────┘
```

- LYNA logo: wordmark, 24 pt
- Org + scope: "Mt. Sinai · {unit-or-aggregate}" — the scope the
  current view is rendered against
- User identity (right): name + role (Mgr / CNO / Inf / Quality)
- Sign out / settings cluster

---

## 2. D1 — Adoption overview

**Question:** Are nurses actually using LYNA on my unit?

```
┌──────────┬───────────────────────────────────────────────────────┐
│   nav    │ ADOPTION OVERVIEW                                     │
│          │ ─────────────────────                                 │
│ ● D1     │                                                       │
│ ○ D2     │ ┌───────────┬───────────┬───────────┬───────────────┐ │
│ ○ D3     │ │ Active    │ Queries   │ Queries / │ Time saved    │ │
│ ○ D4     │ │ today     │ today     │ nurse /   │ vs baseline   │ │
│ ○ D5     │ │           │           │ shift     │               │ │
│ ○ D6     │ │   34      │  287      │   8.4     │  ~24 min/RN   │ │
│ ○ D7     │ │  ▲ 4      │  ▲ 23     │  ▲ 1.2    │   (median)    │ │
│ ○ D8     │ └───────────┴───────────┴───────────┴───────────────┘ │
│ ○ D9     │                                                       │
│ ○ D10    │ Filters: [Unit ▼] [Shift ▼] [7d ▼] [Role: All ▼]    │
│          │                                                       │
│ ───      │ Trend (queries per day, last 90d)                     │
│ Settings │ ┌───────────────────────────────────────────────────┐ │
│          │ │  ▆                                                │ │
│          │ │  ▆▆▆▇    ▇█▇▆           ▆▇▇█▇▇▆ ▆▇▇▇▇▇▇▇▆▇       │ │
│          │ │  █████▇▇▇████▇▇▇▆▆▇▇▇▇▇█████████████████████      │ │
│          │ │  ────────────────────────────────────────────     │ │
│          │ │  Feb 20         Mar 20         Apr 20       May  │ │
│          │ └───────────────────────────────────────────────────┘ │
│          │ [Stacked by unit]  [By role]  [By shift]              │
│          │                                                       │
│          │ Per-unit heatmap (activity by hour-of-day)            │
│          │ ┌─────────────────────────────────────────────────┐  │
│          │ │            00 02 04 06 08 10 12 14 16 18 20 22 │  │
│          │ │ 4-South    ░░░░▒▒██▆▆▇▇▆▆██▇▇▒▒░░░░ ──         │  │
│          │ │ 4-East     ░░░░░░▒▒▆▆▇▇█████▇▇▒▒░░░░            │  │
│          │ │ 5-North    ░░░░▒▒▆▆▇▇████████▇▇▒▒░░             │  │
│          │ │ 6-South    ░░░░░░▒▒▆▆▇▇██▇▇▒▒▒▒░░░░             │  │
│          │ │ Tower-3    ░░░░░░░░▒▒▆▆██▇▇▒▒░░░░░░             │  │
│          │ └─────────────────────────────────────────────────┘  │
│          │ Color: ░ none, ▒ low, ▆ med, ▇ high, █ peak          │
│          │                                                       │
│          │ Per-nurse list                                        │
│          │ ┌─────────────────────────────────────────────────┐  │
│          │ │ Nurse       Role  Last 7d  Trend      Status   │  │
│          │ │ ─────       ────  ───────  ─────      ──────   │  │
│          │ │ Sarah M.    RN    84       ▲▲▲        Power    │  │
│          │ │ Linh T.     RN    62       ▲▲         Active   │  │
│          │ │ Tanya R.    RN    41       ─          Active   │  │
│          │ │ Robert K.   RN    38       ▲          Active   │  │
│          │ │ ...                                              │  │
│          │ │ Devon P.    PCA   12       ▼          Watching │  │
│          │ │ Yvonne L.   Sec   3        ▼▼▼        Inactive │  │
│          │ └─────────────────────────────────────────────────┘  │
│          │ Tap any nurse → Per-nurse usage view                  │
└──────────┴───────────────────────────────────────────────────────┘
```

---

## 3. D2 — AI tool routing

**Question:** Which hospital AI tools are LYNA's nurses routing
through, and how much?

```
│ AI TOOL ROUTING                                                  │
│ ───────────────                                                  │
│ Filters: [Unit ▼] [30d ▼] [Tool category ▼]                      │
│                                                                  │
│ ┌────────────────────────────────────────────────────────────┐  │
│ │ Nursing Reference AI            ⚠ 2 issues this week       │  │
│ │ (registry ID: NU-AI-014)                                   │  │
│ │ Vendor: [vendor name]                                      │  │
│ │ Integration: Epic + phone app                              │  │
│ │                                                            │  │
│ │ ┌─────────┬─────────┬─────────┬──────────┬─────────────┐  │  │
│ │ │ Routed  │ 7d      │ 30d     │ Coverage │ First-time  │  │  │
│ │ │ today   │         │         │          │ exposures   │  │  │
│ │ │   24    │  142    │  587    │   84% ✓  │   12 nurses │  │  │
│ │ └─────────┴─────────┴─────────┴──────────┴─────────────┘  │  │
│ │                                                            │  │
│ │  ▆▆▆▇▇▆▆█████▇▇█████▇▆▇▇█████▇                            │  │
│ │  ──────────────────────────────                            │  │
│ │  Apr 20                          May 20                    │  │
│ │                                                            │  │
│ │ [Drill into detail →]                                      │  │
│ └────────────────────────────────────────────────────────────┘  │
│                                                                  │
│ ┌────────────────────────────────────────────────────────────┐  │
│ │ Clinical Imaging AI             ✓ Healthy                  │  │
│ │ (registry ID: NU-AI-008)                                   │  │
│ │ Integration: Haiku                                         │  │
│ │                                                            │  │
│ │ Routed today: 8 · 7d: 47 · 30d: 198 · Coverage: 92%        │  │
│ │ First-time exposures: 4 nurses                             │  │
│ │  ▒▒▒▆▆▆▆▇▇▆▆▆▇▇▆▆                                          │  │
│ │ [Drill into detail →]                                      │  │
│ └────────────────────────────────────────────────────────────┘  │
│                                                                  │
│ ┌────────────────────────────────────────────────────────────┐  │
│ │ Sepsis Predict AI               🟡 No traffic 14d          │  │
│ │ (registry ID: NU-AI-022)                                   │  │
│ │ Integration: Epic CDS Hooks                                │  │
│ │                                                            │  │
│ │ Routed today: 0 · 7d: 0 · 30d: 0 · Coverage: 0%            │  │
│ │ First-time exposures: 0                                    │  │
│ │ ⚠ No queries routed through this tool in 14 days.          │  │
│ │   Possible causes: tool not surfaced for any                │  │
│ │   intent the router matches; or hospital just deployed it. │  │
│ │ [Investigate →]  [Drill into detail →]                     │  │
│ └────────────────────────────────────────────────────────────┘  │
│                                                                  │
│ ┌────────────────────────────────────────────────────────────┐  │
│ │ Cardiac Decision Support       🔴 Coverage 41% (low)        │  │
│ │ (registry ID: NU-AI-031)                                   │  │
│ │                                                            │  │
│ │ Routed today: 3 · 7d: 19 · 30d: 78 · Coverage: 41% ⚠       │  │
│ │ ⚠ Only 41% of queries this tool should answer were         │  │
│ │   routed through it. Falling back to LYNA native.          │  │
│ │   Possible causes: registry entry too narrow; intent       │  │
│ │   classifier missing edge cases; API errors.               │  │
│ │ [Investigate →]                                            │  │
│ └────────────────────────────────────────────────────────────┘  │
│                                                                  │
│ Sort: [Volume ▼]  [Coverage]  [First-time exposures]             │
```

---

## 4. D3 — Top queries

**Question:** What are nurses asking LYNA, and where are the
knowledge gaps?

```
│ TOP QUERIES                                                      │
│ ───────────                                                      │
│ Filters: [Unit ▼] [Shift ▼] [7d ▼] [Role ▼] [Answered: All ▼]  │
│                                                                  │
│ ┌─────────────────────────────────┬──────────────────────────┐  │
│ │ ✓ MOST-ASKED (answered)         │ ⚠ UNANSWERED (gaps)      │  │
│ │ ─────────────────────────────── │ ──────────────────────── │  │
│ │                                 │                          │  │
│ │ 1. "Last pain med for bed N"    │ 1. "Where's the suction  │  │
│ │    142×  ↗ 4-South, 4-East      │     cart on 4-South?"    │  │
│ │    [View samples]                │    14×  4-South night    │  │
│ │                                 │    [Add to KB]            │  │
│ │ 2. "Door code med room"         │                          │  │
│ │    98×  ↗ all units              │ 2. "Pyxis override code" │  │
│ │    [View samples]                │    9×  4-South, 5-North  │  │
│ │                                 │    [Add to KB] [Flag?]   │  │
│ │ 3. "Policy for med refusal"     │                          │  │
│ │    67×  ↗ Tanya, Linh, +5       │ 3. "Sterile dressing     │  │
│ │    [View samples]                │     supply on 6-East"    │  │
│ │                                 │    7×  6-East floats     │  │
│ │ 4. "Charge nurse tonight"       │    [Add to KB]            │  │
│ │    52×                           │                          │  │
│ │ 5. "Drug interaction check"     │ 4. "Vincristine extrav    │  │
│ │    48×                           │     protocol"            │  │
│ │ 6. "Sign-on summary"            │    5×  5-North oncology  │  │
│ │    41×  (charge nurses)         │    [Add to KB] [Urgent]  │  │
│ │ ...                              │                          │  │
│ │                                 │ Bottom action:           │  │
│ │ [Show all 50 →]                  │ [Export gaps to NI →]    │  │
│ └─────────────────────────────────┴──────────────────────────┘  │
```

---

## 5. D4 — Response times

**Question:** Is LYNA actually faster than the workstation?

```
│ RESPONSE TIMES                                                   │
│ ──────────────                                                   │
│ Filters: [Unit ▼] [Hour-of-day ▼] [7d ▼] [Query type ▼]         │
│                                                                  │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Round-trip latency distribution (all queries, 30d)       │    │
│ │                                                          │    │
│ │   ████                                                   │    │
│ │   ████████                                               │    │
│ │   ████████████                ◄ 2s bar                   │    │
│ │   ████████████████                                       │    │
│ │   ████████████████████                                   │    │
│ │   █████████████████████████████                          │    │
│ │   ███████████████████████████████████                    │    │
│ │   ██████████████████████████████████████████             │    │
│ │   0s    1s    2s    3s    4s    5s    6s   7s+          │    │
│ │                                                          │    │
│ │ p50: 1.4s · p75: 2.1s · p95: 4.8s · 89% under 2s ✓       │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Latency by query type                                    │    │
│ │ ──────────────────                                       │    │
│ │ FHIR (live data)         p50: 0.9s  p95: 2.4s            │    │
│ │ OpKB (door codes, etc)   p50: 0.6s  p95: 1.2s            │    │
│ │ Policy lookup            p50: 1.1s  p95: 2.8s            │    │
│ │ AI routing               p50: 2.1s  p95: 4.8s   ⚠        │    │
│ │ Drug Info                p50: 1.4s  p95: 3.1s            │    │
│ │ Emergency intent         p50: 0.8s  p95: 1.6s            │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Per-unit comparison                                      │    │
│ │ ─────────────────                                        │    │
│ │ 4-South     ███████████░░ p95 1.8s ✓                     │    │
│ │ 4-East      ███████████░░ p95 1.9s ✓                     │    │
│ │ 5-North     ██████████████ p95 4.2s ⚠ (wifi?)            │    │
│ │ 6-South     ███████████░░ p95 2.0s ✓                     │    │
│ │ Tower-3     ██████████░░░ p95 1.7s ✓                     │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Slow query log (top 50 slowest, 7d)                      │    │
│ │ ────────────────────────────────                         │    │
│ │ Query                          Time   STT  Router  Source │   │
│ │ ──────────────────────────────                            │   │
│ │ "verify safety for bed 22"     6.8s   0.4  0.2     6.1   │   │
│ │ "rapid response trace for ..."  5.2s   0.6  0.3     4.1   │   │
│ │ ...                                                       │   │
│ └──────────────────────────────────────────────────────────┘    │
```

---

## 6. D5 — Silent abandonment alerts

**Question:** Which nurses started using LYNA and stopped?

```
│ SILENT ABANDONMENT ALERTS                                        │
│ ─────────────────────────                                        │
│ Filters: [Severity ▼] [Days since last query ▼]                  │
│                                                                  │
│ Aggregate                                                        │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │  Unit: 4-South                                           │    │
│ │  Currently active (7d): 31/38 nurses (82%)              │    │
│ │  90d baseline:           89% (–7% from baseline)         │    │
│ │  At-risk (severity ≥):   4 nurses                       │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ 🔴 At-risk                                                │    │
│ │ ─────                                                    │    │
│ │ Nurse        Last 7d    Trend    Last query   Severity   │    │
│ │ Devon P.     12         ▼▼       3d ago       Warning    │    │
│ │              Used 41/wk average for prior 4w             │    │
│ │              [Reach out →]                               │    │
│ │                                                          │    │
│ │ Yvonne L.    3          ▼▼▼      9d ago       Critical   │    │
│ │              Used 22/wk average for prior 4w             │    │
│ │              [Reach out →]                               │    │
│ │                                                          │    │
│ │ Carlos R.    8          ▼        1d ago       Watching   │    │
│ │              Used 18/wk average for prior 4w             │    │
│ │              [Reach out →]                               │    │
│ │                                                          │    │
│ │ Maya T.      5          ▼▼       4d ago       Warning    │    │
│ │              Used 32/wk average for prior 4w             │    │
│ │              [Reach out →]                               │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ Reach-out template:                                              │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Subject: Quick LYNA check-in                             │    │
│ │ Hi {nurse} —                                             │    │
│ │ Noticed your LYNA usage has dropped this week.           │    │
│ │ Anything we can fix? Bug, friction, missing answer?      │    │
│ │ — {manager}                                              │    │
│ │                                                          │    │
│ │ [Send via Teams] [Send via Mattermost] [Send via email]  │    │
│ └──────────────────────────────────────────────────────────┘    │
```

---

## 7. D6 — Broadcast / help coverage

**Question:** Is my unit responsive when someone asks for help?

```
│ BROADCAST / HELP COVERAGE                                        │
│ ─────────────────────────                                        │
│ Filters: [Unit ▼] [Shift ▼] [7d ▼] [Category ▼]                  │
│                                                                  │
│ ┌─────────────┬─────────────┬─────────────┬─────────────────┐   │
│ │ Total       │ Ack within  │ Ack within  │ Escalations     │   │
│ │ broadcasts  │ 30s         │ 60s         │ (timed out)     │   │
│ │             │             │             │                 │   │
│ │   142       │  87%  ✓     │  95%  ✓     │   3  (2%)       │   │
│ │             │  Target ≥85 │  Target ≥95 │  Target <5%     │   │
│ └─────────────┴─────────────┴─────────────┴─────────────────┘   │
│                                                                  │
│ Response-time distribution (4-South, 7d)                         │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │      ████                                                │    │
│ │      ████████                                            │    │
│ │      ████████████████                                    │    │
│ │      █████████████████████████              ◄ 60s        │    │
│ │      ████████████████████████████████                    │    │
│ │      ██████████████████████████████████████              │    │
│ │      0s    15s   30s   45s   60s   75s   90s   2m+      │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ Per-shift comparison                                             │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │             Day     Night    Weekday  Weekend            │    │
│ │ 4-South     94%     78% ⚠    92%      82% ⚠               │    │
│ │ 4-East      96%     88%      95%      89%                │    │
│ │ 5-North     91%     74% ⚠    89%      78% ⚠               │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ Escalations (when no one acked within timeout)                   │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Time    Sender   Category    Notes                       │    │
│ │ ────    ──────   ────────    ─────                       │    │
│ │ 03:14   Priya    Supply       Devon was on break          │   │
│ │ 04:38   Maya     Help         No PCA on shift             │   │
│ │ 07:22   Sarah    Isolation    Iso-cart not stocked        │   │
│ └──────────────────────────────────────────────────────────┘    │
```

---

## 8. D7 — Critical alerts audit

**Question:** Every rapid response activation — what fired, what
was paged, what protocol surfaced?

```
│ CRITICAL ALERTS AUDIT                                            │
│ ─────────────────────                                            │
│ Filters: [Unit ▼] [Alert type ▼] [30d ▼]                         │
│                                                                  │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Date     Time    Unit / bed    Type        Activator     │    │
│ │ ────     ────    ──────────    ────        ─────────     │    │
│ │ 05-20    04:35   4-East / 6    Rapid Resp  Sofia C.      │    │
│ │   ST changes, post-CABG day 2                            │    │
│ │   Paged: RRT ✓ · cardiology ✓ · charge ✓                 │    │
│ │   Protocol: NU-CARD-014 (ACS) — surfaced ✓               │    │
│ │   ACKed in 6s · ended 04:52                              │    │
│ │   [Open full event →]  [Export PDF →]                    │    │
│ │ ─                                                        │    │
│ │ 05-19    14:22   5-North / 18  Code Blue   Maria L.      │    │
│ │   Cardiac arrest, witnessed                              │    │
│ │   Paged: code team ✓ · attending ✓                       │    │
│ │   Protocol: NU-CARD-002 (ACLS) — surfaced ✓              │    │
│ │   ACKed in 4s · ended 14:38                              │    │
│ │   [Open full event →]  [Export PDF →]                    │    │
│ │ ─                                                        │    │
│ │ 05-17    23:14   4-South / 22  Fall        Linh T.       │    │
│ │   Witnessed fall from bed                                │    │
│ │   Paged: charge nurse ✓                                  │    │
│ │   Protocol: NU-FALL-001 — surfaced ✓                     │    │
│ │   IR filed within 30 min ✓                               │    │
│ │   [Open full event →]  [Export PDF →]                    │    │
│ │ ...                                                      │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ Aggregate                                                        │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ This month: 14 activations (12 RR · 1 Code Blue · 1 Fall)│    │
│ │ Median time-to-ACK:        5.2s  ✓ (target ≤10s)         │    │
│ │ Median time-to-RRT-arrive: 87s   ✓ (target ≤120s)        │    │
│ │ All events have protocol surfaced:  ✓                    │    │
│ │ All events have post-event PDF available: ✓              │    │
│ └──────────────────────────────────────────────────────────┘    │
```

---

## 9. D8 — Interpreter sessions

**Question:** How often is ad-hoc machine translation being used,
and where should we add certified coverage?

```
│ INTERPRETER SESSIONS                                             │
│ ─────────────────────                                            │
│ Filters: [Unit ▼] [Language ▼] [Certified hand-off ▼] [30d ▼]    │
│                                                                  │
│ Sessions by language (30d)                                       │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Spanish     ████████████████████████████  88             │    │
│ │ Mandarin    ████████████████  47                          │    │
│ │ Russian     ████████  22                                  │    │
│ │ Bengali     ██████  17                                    │    │
│ │ Korean      ████  11                                      │    │
│ │ ── coverage line ──                                       │    │
│ │ Polish      ██  6   🟡 Not in certified coverage          │    │
│ │ Haitian Cr. █  4    🟡 Not in certified coverage          │    │
│ │ Vietnamese  █  3    🟡 Not in certified coverage          │    │
│ │                                                          │    │
│ │ [Suggest expanding certified coverage for: Polish,       │    │
│ │  Haitian Cr., Vietnamese →]                              │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ Certified hand-off rate (should we be queuing more?)             │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Total sessions:                  198                     │    │
│ │ Sessions invoking 'queue cert':  31 (16%)                │    │
│ │ Median session length:           4.2 turns               │    │
│ │ Sessions ≥10 turns (long):       12 (6%)  ⚠              │    │
│ │ Of those long sessions,                                  │    │
│ │   how many invoked 'queue cert': 8 (67%)                 │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ Per-session detail                                               │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Date    Time   Lang     Unit    Turns  Cert?  Duration   │    │
│ │ ────    ────   ────     ────    ─────  ─────  ────────   │    │
│ │ 05-20   03:00  Spanish  4-South 5      No     2:18       │    │
│ │ 05-19   22:14  Mandarin 5-North 12     Yes ✓  18:42      │    │
│ │ 05-19   19:47  Spanish  6-South 4      No     1:53       │    │
│ │ ...                                                      │    │
│ │ [Export compliance PDF for language services audit →]    │    │
│ └──────────────────────────────────────────────────────────┘    │
```

---

## 10. D9 — Per-AI-tool detail

**Question:** Walk me through what {tool} did last month.

Drill-down from D2. Single-tool detail page.

```
│ ◀ Back to AI tool routing                                        │
│                                                                  │
│ NURSING REFERENCE AI                                             │
│ (registry ID: NU-AI-014 · added: 2025-09 · vendor: ___)          │
│ ──────────────────────────────────────────                       │
│                                                                  │
│ Top KPIs (30d)                                                   │
│ ┌──────────┬──────────┬──────────┬──────────┬──────────────┐   │
│ │ Routed   │ First-   │ Coverage │ Issues   │ Estimated    │   │
│ │          │ time     │          │          │ value/qry    │   │
│ │  587     │  37      │  84% ✓   │  2 ⚠     │  $4.20       │   │
│ └──────────┴──────────┴──────────┴──────────┴──────────────┘   │
│                                                                  │
│ Routing volume (daily, 90d)                                      │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │  ▆▇▆▇▆▆▇█▇▆▇▆▇▆▆▇█▇▇▇▇▇████▇▇▇█████▇▇█████              │    │
│ │  ──────────────────────────────────────                  │    │
│ │  Feb 20         Mar 20         Apr 20         May 20     │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ Top intents routed                                               │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Drug-drug interaction         387×                       │    │
│ │ Renal dose check              112×                       │    │
│ │ Pregnancy/lactation safety     54×                       │    │
│ │ Geriatric dosing               34×                       │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ First-time exposures (cumulative, 90d)                           │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │                                       ▆▇▆▇                │   │
│ │                              ▆▇▆▇▆▆▇████                  │   │
│ │                     ▆▇▆▇▆▆▇█████████████                  │   │
│ │      ▆▆▇▇▆▇▆▆▇█████████████████████████                   │   │
│ │  ────────────────────────────────────────                 │   │
│ │  Feb 20         Mar 20         Apr 20         May 20      │   │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ Issues (last 14d)                                                │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ 05-18  14:22  API 500 (vendor side)    Fallback to LYNA  │   │
│ │ 05-15  09:11  Timeout 8s              Fallback to LYNA   │   │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ ROI estimate                                                     │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Annual contract:        $48,000                          │    │
│ │ Routings (annualized):  ~7,000                           │    │
│ │ Cost per routing:       $6.86                            │    │
│ │ Estimated value/qry:    $4.20 (LYNA-derived)             │    │
│ │   (avoided pharmacy page / time saved / safety value)    │    │
│ │ ROI before LYNA:        n/a (no usage data)              │    │
│ │ ROI with LYNA:          ~ -0.39 currently   ⚠            │    │
│ │   Vendor relationship   :  request usage data from vendor │    │
│ │   to recalculate, or adjust contract structure           │    │
│ └──────────────────────────────────────────────────────────┘    │
```

---

## 11. D10 — Buyer-facing ROI

**Question:** What is LYNA saving us in nurse-time per shift?

```
│ BUYER-FACING ROI                                                 │
│ ────────────────                                                 │
│ Filters: [Unit ▼] [Hourly rate ▼] [30d ▼]                        │
│                                                                  │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │  ESTIMATED TIME SAVED                                    │    │
│ │  ──────────────────                                      │    │
│ │                                                          │    │
│ │     ~24 minutes per RN per shift (median)                │    │
│ │     ~46,800 RN-hours saved annually (across 4-South      │    │
│ │              deployment of 38 RNs over 365 days)         │    │
│ │     ~$2,808,000 estimated annual value                   │    │
│ │              (at $60/hr fully loaded RN rate)            │    │
│ │                                                          │    │
│ │     LYNA annual cost (this unit):  $84,000               │    │
│ │     Net annual benefit:            $2,724,000            │    │
│ │     ROI:                           ~3,243%               │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ Sensitivity bounds                                               │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │              Conservative   Base       Aggressive        │    │
│ │ Time saved   12 min/shift   24 min     36 min            │    │
│ │ Annual value $1,404K        $2,808K    $4,212K           │    │
│ │ ROI          1,571%         3,243%     4,914%            │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ Calculation breakdown                                            │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │ Source: I-Corps benchmarks anchored to H1–H18 +          │    │
│ │   measured LYNA query volume.                            │    │
│ │                                                          │    │
│ │ Avg query saves:                                         │    │
│ │   - Workstation bypass:    2.5 min  (vs walk + log in)   │    │
│ │   - Senior-nurse bypass:   5.0 min  (Interview #1 ref)   │    │
│ │   - Policy-Tech bypass:    5.0 min  (Interview #2 ref)   │    │
│ │   - Pharmacist page:       40 min   (Robert §4.6)        │    │
│ │   - Charge handoff:        15 min   (Marcus §4.3)        │    │
│ │   - Sign-on:               20 min   (Jamal §4.4)         │    │
│ │   - Interpreter wait:      9 min    (Maya §4.10 baseline)│    │
│ │                                                          │    │
│ │ Weighted by query mix:     ~3.1 min average per query    │    │
│ │ Queries per RN per shift:  ~8.4 (D1 metric)              │    │
│ │ → Time saved per shift:    ~24 min                       │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ Per-unit breakdown                                               │
│ ┌──────────────────────────────────────────────────────────┐    │
│ │              Queries/wk   Time saved/wk   Annual value   │    │
│ │ 4-South      1,994        ~103 RN-hours   $2,808K        │    │
│ │ 4-East       1,712        ~88 RN-hours    $2,413K        │    │
│ │ 5-North      1,387        ~71 RN-hours    $1,952K        │    │
│ └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│ [Export to PDF for CCIO budget packet →]                         │
│ ─                                                                │
│ Footer: Estimates anchored to I-Corps research                   │
│ (`hypothesis-map.md` H1-H18; `interviews-index.md` BMC V2;        │
│ `bots/shared/reports/lyna-strategic-analysis.md`)                 │
```

---

## 12. Per-nurse usage drill-down (modal from D1)

Tap any nurse on the D1 per-nurse list:

```
│ ┌────────────────────────────────────────────────────────┐      │
│ │ ✕ Close                                                │      │
│ │                                                        │      │
│ │ Devon P. · PCA · 4-South                               │      │
│ │ ────────────────────────                               │      │
│ │                                                        │      │
│ │ Last query: 3d ago ("Where is the Pyxis override?")    │      │
│ │ 7d queries: 12 (vs 41/wk baseline — ▼ 70%)             │      │
│ │                                                        │      │
│ │ Trend (90d)                                            │      │
│ │ ▇▇▇▆▇▇████████▇▆▆▆▒▒▒▒▒▒░░                            │      │
│ │ ──────────────────────────                              │      │
│ │ Feb 20             May 20                              │      │
│ │                                                        │      │
│ │ Top query types (lifetime)                             │      │
│ │ - Door codes / supply locations                        │      │
│ │ - Charge nurse on duty                                 │      │
│ │ - Broadcast acknowledgments                            │      │
│ │                                                        │      │
│ │ Recent broadcasts handled: 23 (top responder on 4-S)   │      │
│ │                                                        │      │
│ │ [Reach out →]                                          │      │
│ └────────────────────────────────────────────────────────┘      │
```

---

## 13. Cross-references

- [`manager-dashboard.md`](manager-dashboard.md) — canonical spec
- [`manager-dashboard-screen-designs.md`](manager-dashboard-screen-designs.md) — pixel specs
- [`opal-design-system.md`](opal-design-system.md) — colors,
  typography, components
- [`opal-ui-wireframes.md`](opal-ui-wireframes.md) — earlier v3
  doc had dashboard wireframes; some patterns (sparklines,
  per-tool cards) carry forward
- [`implementation/react-dashboard/`](implementation/react-dashboard/) — implementation skeleton

---

**Last updated:** 2026-05-20
