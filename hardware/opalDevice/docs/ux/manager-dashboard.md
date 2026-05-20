# LYNA Manager Dashboard

**Date:** 2026-05-20
**Surface:** Web app (responsive desktop / large tablet). No nurse
ever touches this — it is the **unit manager / CNO / clinical
informatics / CCIO** view.
**Companion to:**
[`opal-interaction-flows.md`](opal-interaction-flows.md) (the
nurse-facing v1 iPhone app)
**Anchored to:** `i-corps/hypothesis-map.md` H1–H18 and the BMC V2
update in `i-corps/interviews/interviews-index.md`.

---

## 0. Why this dashboard exists

Three things the I-Corps interviews said the hospital cannot
currently see, and that LYNA is uniquely positioned to surface:

### 0.1 Silent tool abandonment (H13)

> "Managers have no visibility into silent tool abandonment.
> No current system tracks it."
> — `i-corps/hypothesis-map.md` H13

Every hospital has a graveyard of clinical software that was
purchased, "deployed," reported to the board as successful, and
quietly never used. The unit manager finds out months later when
the renewal invoice comes through. There is no current operational
view that says "as of this month, 0% of your nurses opened
{tool}."

LYNA sees the usage. Specifically: when a nurse asks LYNA a
question that LYNA routes through a hospital-integrated AI (Flow
4.6), LYNA logs the routing. The dashboard surfaces those logs as
**adoption signal** — for LYNA itself and for the AI tools LYNA
routes through.

### 0.2 AI-awareness gap (H6)

> "Hospitals are deploying clinical AI but nurses do not know it
> exists at the point of care. NI team confirmed no usage data
> for clinical reference tools on the phone."
> — H6

The dashboard makes the gap visible. Per-tool, per-unit, per-shift:
how many queries did this AI handle, how many were routed by LYNA,
how many were "first time this nurse saw this tool." H6 stops
being a hypothesis nobody can prove and becomes a chart anyone can
read.

### 0.3 Efficiency as the decision frame for the buyer (H2, H10)

> "CCIO is the beachhead buyer. Efficiency is the decision
> framework, not safety. Safety events from information gaps are
> real (~5%) but explicitly not a top priority."
> — H2
>
> "CCIO is the single door, not a dual CNO/CIO path. His project
> ingestion process requires estimated ROI."
> — H10

The CCIO's renewal conversation is driven by an ROI estimate.
LYNA pilots have to produce that estimate, defensibly. The
dashboard's **buyer-facing metrics view** is the artifact the
CCIO walks into the budget meeting with.

---

## 1. Users

| Role | Primary use of dashboard | Hypothesis link |
|---|---|---|
| Unit manager (med-surg / cardiac) | Adoption + abandonment + broadcast coverage on their unit | H13, H6 |
| CNO / VP Nursing | Adoption across units, top queries, time-saved estimate | H2 |
| CCIO / CMO (informatics) | AI-routing detail, integrated-tool utilization, ROI for renewal conversations | H2, H6, H10, H17, H18 |
| Clinical informatics team (NI) | Top queries / unmet questions for KB curation; per-site Operational KB gaps | H3, H6 |
| Quality / safety officer | Critical-alert audit, broadcast response times, interpreter compliance audit | (cross-cutting) |
| CFO (read-only) | ROI summary | H10, H18 |

**The dashboard is not a buying-funnel marketing surface.** Sales
demos use a separate demo-mode (deferred — see §6).

---

## 2. View inventory

Ten views. Each one answers one question a specific user has.

| View | Primary question it answers | Primary user |
|---|---|---|
| D1 — Adoption overview | "Are nurses actually using LYNA on my unit?" | Unit manager |
| D2 — AI tool routing | "Which hospital AI tools are LYNA's nurses using, and how much?" | CCIO |
| D3 — Top queries | "What are nurses asking LYNA, and where are the knowledge gaps?" | NI / unit manager |
| D4 — Response times | "Is LYNA actually faster than the workstation?" | CCIO (efficiency frame) |
| D5 — Silent abandonment alerts | "Who started using LYNA and stopped?" | Unit manager |
| D6 — Broadcast / help coverage | "Is my unit responsive when someone asks for help?" | Unit manager, quality |
| D7 — Critical alerts audit | "Every rapid response activation — what fired, what was paged, what protocol surfaced?" | Quality / safety |
| D8 — Interpreter sessions | "How often is ad-hoc machine translation being used, and where should we add certified coverage?" | Clinical informatics, language services |
| D9 — Per-AI-tool detail | "Walk me through what {hospital AI tool} did last month." | CCIO (renewal conversations) |
| D10 — Buyer-facing ROI | "What is LYNA saving us in nurse-time per shift?" | CCIO, CNO, CFO |

---

## 3. Per-view specs

### D1 — Adoption Overview

**Question:** Are nurses actually using LYNA on my unit?

**Layout:**
- Top KPI row: active users (today, this week, this month);
  total queries (today, this week, this month); average queries
  per nurse per shift
- Trend graph (90 days): queries per day, split by unit
- Per-unit heatmap: row per unit, columns showing
  activity-per-shift across the day-night cycle
- Per-nurse list (drill-down from the heatmap): who's a power
  user, who has plateaued, who never engaged

**Filters:** unit, shift (day/night), date range, role (RN /
PCA / charge / float).

**Data sources:** memory event log (`memory_system/events/log/`);
specifically the per-query event written by the voice router.

**v1 specific behaviors:**
- "Power user" definition is empirical, not pre-set: any nurse
  in the top quartile of queries-per-shift for their unit
- "Never engaged" definition: logged into the app at least once
  in the last 14 days, but made 0 voice queries

**Hypothesis link:** H13 (visibility into who's using vs not).

### D2 — AI Tool Routing

**Question:** Which hospital AI tools are LYNA's nurses routing
through, and how much?

**Layout:**
- Per-tool card (one card per entry in the per-site hospital AI
  registry — see Flow 4.6 in the interaction-flows doc):
  - Tool name
  - Queries routed via LYNA (today / week / month)
  - "First-time exposures" — count of unique nurses who heard
    this tool named by LYNA for the first time in the period
  - Coverage — what percentage of queries the registry says this
    tool should authoritatively answer actually went through it
    vs LYNA's native fallback
  - Trend sparkline
- Sortable by tool, by routing volume, by coverage gap, by
  first-time exposures

**Data sources:** memory event log (the query routing emits a
typed event with the routed-to tool's registry ID).

**v1 specific behaviors:**
- If a tool has zero routings in 14 days, the card carries a
  yellow "no traffic" flag — H13 in action
- If a tool's "coverage" drops below 70%, a red flag — indicates
  the integration is broken, the registry entry is stale, or
  LYNA's intent classification is misrouting

**Hypothesis link:** H6, H13, H17, H18 (LYNA's most important
strategic surface for the buyer conversation).

### D3 — Top Queries

**Question:** What are nurses asking LYNA, and where are the
knowledge gaps?

**Layout:**
- Two parallel columns:
  - **Most-asked queries** (anonymized, normalized) — top 50
    queries by frequency in the period
  - **Most-unanswered queries** — queries LYNA could not answer
    (no data in any registered source, fell back to "I don't
    have that documented")
- Per-row drill: which unit / shift / role asked, how many
  distinct nurses asked, sample queries (paraphrased for
  privacy)
- **"Add to KB" affordance** on every unanswered query — files
  a ticket to the per-site Operational KB curation queue

**Filters:** unit, shift, role, answered vs unanswered.

**Data sources:** memory event log (every voice query
emits an event with normalized intent + answered/unanswered
flag).

**v1 specific behaviors:**
- Unanswered queries are the most actionable view in the
  dashboard. Each one represents either (a) a missing
  Operational KB entry (door codes, supplies, on-call rosters
  that haven't been ingested) or (b) a hospital AI tool that
  exists but isn't yet in the AI registry. Both are quick fixes.
- The "Add to KB" affordance writes a task to the per-site
  curation queue, NI team picks up, registry/KB gets updated,
  next query resolves cleanly.

**Hypothesis link:** H3 (NI team is the evaluator/configurer);
H6 (AI awareness gap surfaced as queries the hospital could
answer if the tools were registered).

### D4 — Response Times

**Question:** Is LYNA actually faster than the workstation?

**Layout:**
- Distribution chart of voice round-trip latency, segmented by
  query type (FHIR / OpKB / Policy / AI registry / Drug Info /
  emergency-intent)
- The sub-2-second target line drawn on the chart
- Per-unit comparison: which units' nurses see worse latency
  (network / wifi coverage signal)
- "Slow query" log: top 50 slowest queries in the period with
  a per-query breakdown of where the time was spent (STT,
  router, source query, synthesis, TTS)

**Filters:** unit, time of day, query type.

**Data sources:** voice router emits a structured timing event
per query; the briefing engine aggregates.

**v1 specific behaviors:**
- The sub-2s bar is non-negotiable for the bypass-the-screen
  pattern (see INTELLIGENCE_LAYER.md cross-cutting themes:
  "faster than asking a person"). When >10% of queries exceed
  2s the dashboard turns yellow; >25% turns red.
- "Where time was spent" drill-down is the operator's debugging
  view — STT slowness → wifi; source-query slowness → integrated
  AI's API; synthesis slowness → LLM provider.

**Hypothesis link:** H2 (efficiency is the buyer's frame).

### D5 — Silent Abandonment Alerts

**Question:** Which nurses started using LYNA and stopped?

**Layout:**
- Alert list: nurses whose query rate has dropped >50% from their
  trailing-4-week average
- Per-row: nurse identity (within the manager's unit scope only),
  trailing usage curve, last query, last query type
- "Reach out" affordance: messages the nurse via the hospital's
  preferred channel (Teams, Mattermost, email — per-site
  configurable) with a templated "we noticed, anything we can
  fix?" message
- Aggregate: percentage of the unit currently active vs trailing
  90-day baseline

**Filters:** unit, severity (warning / critical), days since last
query.

**Data sources:** memory event log + anomaly detection
(LYNA-side); reach-out goes through the hospital's existing
messaging integration.

**v1 specific behaviors:**
- The first wave of pilot deployments at any new site WILL show
  abandonment of LYNA itself — that is healthy data. The
  dashboard's job is to surface it early so the unit manager can
  intervene (training, retraining, removing blockers) before it
  becomes a pilot-killing pattern.
- Privacy: the manager only sees nurses on their unit. CNO sees
  unit-level aggregates, not nurse-level.

**Hypothesis link:** H13.

### D6 — Broadcast / Help Coverage

**Question:** Is my unit responsive when someone asks for help?

**Layout:**
- Per-unit response-time histogram for broadcasts (Flow 4.8)
- Coverage rate: percentage of broadcasts that got an ack within
  30s, 60s, 120s
- "Escalation rate" — broadcasts that timed out and escalated to
  the charge nurse
- Per-shift comparison: day vs night, weekday vs weekend
- Aggregate broadcast volume per shift (calibration against staffing
  ratios)

**Filters:** unit, shift, broadcast category (supply, help,
isolation).

**Data sources:** broadcast event log (sender, recipients,
acks, delivery confirmation, escalations).

**v1 specific behaviors:**
- Per-nurse responsiveness is NOT shown (privacy + culture risk).
  Aggregate-unit only.
- An escalation rate above 15% on a unit signals a structural
  problem (under-staffing, role confusion, broken acknowledgment
  workflow) — flagged but not auto-acted on.

**Hypothesis link:** H12 (resource-nurse-offline window
deployment); H8 (chronic-normalized — quantifying the chronic
load).

### D7 — Critical Alerts Audit

**Question:** Every rapid response activation — what fired, what
was paged, what protocol surfaced?

**Layout:**
- Chronological list of every critical-alert activation in the
  period (Flow 4.7)
- Per-event: timestamp, activator, unit, bed, alert type,
  pages sent (who got paged, who acknowledged, ETAs), protocol
  surfaced, patient FHIR data at activation, alert end time
- Drill-down into the structured event log for the activation
- Export-to-PDF for the hospital's standard post-event review
  packet

**Filters:** unit, alert type (rapid response / code blue / fall /
bleed), date range.

**Data sources:** critical-alert events (Flow 4.7 §"Logged
event").

**v1 specific behaviors:**
- Every hospital does post-event reviews on rapid responses;
  LYNA's audit log replaces the manual paperwork those reviews
  currently rely on. The PDF export matches the per-site review
  packet template (Operational KB).
- The audit log is read-only — nothing can be edited or removed
  after the fact. This is a compliance feature.

**Hypothesis link:** safety-side validation (the ~5% of cases
where info gaps cause adverse events; not the top buyer concern
per H2 but real, and a compliance-required audit trail).

### D8 — Interpreter Sessions

**Question:** How often is ad-hoc machine translation being used,
and where should we add certified coverage?

**Layout:**
- Aggregate session count per language, per unit, per shift
- "Queue interpreter" invocation rate — when ad-hoc bumped up to
  a certified-interpreter request
- Languages requested but not in the per-site coverage set
  (signal for adding coverage)
- Average session duration; turn count per session
- Per-session detail (with PHI handled per the standard
  event-log policy): patient encounter ID, language, duration,
  whether certified hand-off occurred

**Filters:** unit, shift, language, certified-hand-off occurred.

**Data sources:** interpreter session events (Flow 4.10 §"Logged
event").

**v1 specific behaviors:**
- Compliance audit framing: the dashboard's PDF export matches
  the per-site language-services audit packet, demonstrating
  ad-hoc-vs-certified usage discipline.
- "Add this language to certified coverage" affordance: surfaces
  the case for expanding the hospital's interpreter contract,
  with usage data to back it.

**Hypothesis link:** H5 (formal-system bypass — interpreter line
queue is the formal system); H8 (chronic-normalized — quantifies
the chronic delay); Title VI compliance framing.

### D9 — Per-AI-Tool Detail

**Question:** Walk me through what {hospital AI tool} did last
month.

**Layout (one tool at a time):**
- Tool identity card: name, vendor, contract term, integration
  surface (Epic / phone / intranet / etc.)
- Routing volume trend (daily, 90 days)
- Top intents routed through this tool
- First-time exposure trend (new nurses who heard this tool
  named by LYNA for the first time)
- Coverage: what fraction of queries-this-tool-should-answer
  actually went through it
- "Issues" log: integration failures, API errors, fallback
  events
- ROI estimate (utilization × estimated value-per-query) for the
  renewal conversation

**Filters:** date range, intent.

**Data sources:** memory event log + hospital AI registry +
per-tool integration health checks.

**v1 specific behaviors:**
- This is the **CCIO renewal-conversation surface**. When the
  CCIO sits down with the vendor of a hospital-integrated AI
  to discuss renewal, the conversation is "we paid you $X last
  year; here is the routing volume LYNA drove to your tool;
  here is the trend." Without LYNA, that data does not exist.
- A tool with zero routings in 90 days is a renewal-cancellation
  candidate — surfaced as a top-of-page banner.

**Hypothesis link:** H17 (clinical AI vendors are complementary
to LYNA); H18 (renewal economics — hospitals pay for utilization
of existing investments).

### D10 — Buyer-Facing ROI

**Question:** What is LYNA saving us in nurse-time per shift?

**Layout:**
- Top-of-page summary card:
  - Estimated minutes saved per nurse per shift (median)
  - Estimated FTE-equivalent across the deployment
  - Estimated annualized value (configurable hourly rate)
- ROI calculation breakdown:
  - Time-loss benchmarks from I-Corps research (the ~5 min "ask
    a senior nurse" loop from Interview #1, the 5+ min "Policy
    Tech then hunt for a person" from Interview #2, etc.)
  - Query volume × time saved per query × labor cost
- Comparison: LYNA annual cost vs estimated annual labor savings
- Sensitivity: low / base / high estimates (matching the
  `bots/shared/reports/lyna-strategic-analysis.md` ROI model)
- Per-unit breakdown
- PDF export for the CCIO's budget packet

**Filters:** unit, hourly-rate assumption, date range.

**Data sources:** memory event log + configurable rate parameters
+ I-Corps research benchmarks (hard-coded references to the H1–H18
hypotheses).

**v1 specific behaviors:**
- The ROI estimate is honestly framed as an estimate, with
  sensitivity bounds shown explicitly. Overclaiming on the
  dashboard would burn the CCIO conversation the first time the
  hospital does its own time study.
- The PDF export references the I-Corps research and
  `bots/shared/reports/lyna-strategic-analysis.md` for the
  underlying assumptions — defensible under questioning.

**Hypothesis link:** H10 (CCIO's project ingestion requires ROI
estimate); H2 (efficiency framing).

---

## 4. Cross-view patterns

### 4.1 Privacy and PHI handling

- **Manager scope:** unit manager sees data only for their unit's
  staff and patients. Cross-unit views require CNO-level or
  informatics-level access.
- **PHI in dashboard:** patient identifiers are shown only where
  necessary (D7 critical-alert audit, D8 interpreter session
  per-event detail). Aggregate views never show patient
  identifiers.
- **Per-nurse views:** D5 abandonment alerts show nurse-level
  data only to that nurse's unit manager. D6 broadcast coverage
  is aggregate-only.
- **Audit:** every dashboard access is logged (who looked at
  what, when). Same compliance discipline as nurse-side queries.

### 4.2 Data sources

The dashboard is a read-only view over:

- `memory_system/events/log/` — typed memory events, the source
  of truth for every voice query LYNA handled (anonymized
  identifiers).
- `memory_system/events/briefing.py` — briefing engine
  aggregations.
- Per-site Operational KB — hospital AI registry, on-call rosters,
  Policy system inventory.
- Hospital integration health endpoints — Epic FHIR, Policy
  system, Drug Info, integrated AI APIs.

The dashboard never writes back to clinical systems. It is a
read view + a curation queue ("add to KB" tasks for NI).

### 4.3 Filters and time ranges

Standard filter set across all views where applicable:
- Date range (today / yesterday / 7d / 30d / 90d / custom)
- Unit (manager-scoped) / cross-unit (CNO+ scope)
- Shift (day / night)
- Role (RN / charge / PCA / float / educator)
- Custom: per-view specific filters

### 4.4 Export

Every view supports:
- CSV export (raw data)
- PDF export (formatted, with the hospital's logo + the LYNA
  attribution footer for compliance audit trail)

PDF exports include the I-Corps hypothesis references where
applicable so the buyer-facing conversations stay anchored to the
research foundation.

---

## 5. Cross-references to existing assets

The earlier `opal-ui-wireframes.md` includes dashboard
wireframes drawn against the v3 device-targeted concept. Some of
those wireframes still apply:

- **Color palette / typography / spacing:** `opal-design-system.md`
  is authoritative; reusable for the dashboard.
- **System status / device map views:** in the earlier doc, these
  showed the dedicated-device fleet. For v1 (iPhone app), the
  device map is not applicable; D1 Adoption Overview replaces it.
- **Message flow / AI intelligence views:** the old doc's
  "AI Intelligence" view is the precursor to D2 + D9; some of the
  visualization patterns (sparklines, per-tool cards) carry over.
- **React dashboard skeleton:** `implementation/react-dashboard/`
  is the implementation starting point. Repurpose for v1.

A separate visual design pass will produce wireframes /
high-fidelity screens against this spec. Not in scope here.

---

## 6. Deferred / out of scope

- **Demo mode / sales-presentation surface** — separate UI for
  sales demos (synthetic data, scenario walkthroughs). Deferred
  until the dashboard is in pilot use.
- **Predictive staffing module** — the
  `bots/shared/reports/lyna-strategic-analysis.md` strategic-plan
  doc references a predictive-staffing capability. Not part of
  v1 dashboard.
- **Workforce intelligence premium tier** — per the BMC V1
  draft, a higher-tier workforce-intelligence offering was
  planned. Same module bones as predictive staffing; deferred to
  post-pilot.
- **Per-nurse review pages** — manager-led 1:1 review surfaces
  with nurse usage data. Privacy-and-culture risk evaluation
  required before designing.
- **Integration with hospital's existing analytics platform**
  (Tableau, Power BI, Epic Caboodle). The dashboard is a
  standalone v1; integration is a v1.1 conversation per pilot
  site.

---

## 7. Update protocol for this file

This doc is the canonical manager-dashboard spec. Update when:
- A new view is added or substantially changed
- A new data source comes online (e.g., the Neo4j projection
  becomes available for relationship queries)
- A new hypothesis lands in `hypothesis-map.md` that the
  dashboard should surface
- Pilot feedback identifies a missing view or a misframed
  question

Cross-check against:
- [`opal-interaction-flows.md`](opal-interaction-flows.md) — every
  logged-event the dashboard reads has a source in a nurse-side
  flow
- [`../../../../INTELLIGENCE_LAYER.md`](../../../../INTELLIGENCE_LAYER.md)
  §4.6 (Robert, AI-routing) and §4.7 / §4.8 / §4.10 (the
  high-logging journeys)
- [`../../../../i-corps/hypothesis-map.md`](../../../../i-corps/hypothesis-map.md)
  H1–H18 (the dashboard's reason for being)
- [`opal-design-system.md`](opal-design-system.md) — design system
  is authoritative for color / typography / spacing

---

**Last updated:** 2026-05-20
**Next pass:** wireframe + high-fidelity screens against this spec
(separate visual-design pass).
