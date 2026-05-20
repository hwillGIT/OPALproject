# Session Handoff — OPAL Intelligence Layer Documentation

**Last updated:** 2026-05-20
**Branch we're on:** `docs/intelligence-layer-readme` (PR [#20](https://github.com/collabPGC/OPALproject/pull/20))
**Repo:** `collabPGC/OPALproject` (org repo)

Use this file to bring a fresh session up to speed without re-reading
the whole transcript. Update it at the end of each working session.

---

## 1. Where we are right now

**Ten** LYNA clinical-staff user stories live in
[`INTELLIGENCE_LAYER.md`](INTELLIGENCE_LAYER.md) §4 — all nurses,
all anchored to the I-Corps customer-discovery research (H1–H18 +
BMC V2 themes + Interview #1 David Hernandez and Interview #2
anonymous ICU travel nurse). Each story ends with an **Interview
anchor** block citing what specifically grounds the scenario.

| § | Nurse | Setting | Trigger | Interview anchor |
|---|---|---|---|---|
| 4.1 | Sarah | Med-surg, 2 AM bedside | "What's the last pain med for bed 14?" | H5, H7, H9 — bypass-the-screen |
| 4.2 | Linh | Float pool, first shift on 4-South | "Where are the sterile dressings?" | Interview #1 (David); BMC V2 three-layer baseline |
| 4.3 | Marcus | Charge, late in no-resource window (00:00–05:00) | "Give me a unit status for 4-South" | H12 (resource offline → charge as sole router) |
| 4.4 | Jamal | Day-shift, taking over 4 patients | "Sign-on summary for my four patients" | H5, H9; direct transcript open follow-up |
| 4.5 | Tanya | 2 weeks off orientation, refused med | "Policy for a patient refusing a cardiac med?" | Interview #2 (Policy Tech complaint); H4, H5 |
| 4.6 | Robert | Med-surg admit, AI-awareness gap | "Is the new cipro okay with what he's on?" | H6 (AI awareness), H13 (silent abandonment), H17, H18 |
| 4.7 | Sofia | Cardiac step-down (4-East), deteriorating | "Rapid response, bed 6, ST changes" | H1, H7; BMC V2 ICU explicitly *not* day-one beachhead |
| 4.8 | Priya | Med-surg, mid-procedure in isolation | "Broadcast 4-South: I need a saline flush in 305" | Interview #2 (group-chat-from-iso unprompted feature request); H7, H14 |
| 4.9 | Aisha | Med-surg wound documentation | "LYNA, document a pressure injury on bed 18" | H14 (phone owns camera) |
| 4.10 | Maya | Med-surg night, Spanish-only patient | "Interpreter mode, Spanish" | H5, H8; Mt. Sinai catchment + Title VI; UX-doc Flow 3 precedent |

**UI/UX specs (v1 iPhone app + manager dashboard + v3 alignment)
shipped on the same PR:**

- [`hardware/opalDevice/docs/ux/opal-interaction-flows.md`](hardware/opalDevice/docs/ux/opal-interaction-flows.md)
  — 10-surface inventory (S1–S10) + per-journey flows for §4.1–§4.10.
- [`hardware/opalDevice/docs/ux/opal-ui-wireframes-v1.md`](hardware/opalDevice/docs/ux/opal-ui-wireframes-v1.md)
  — ASCII wireframes for S1–S10 + per-journey screen sequences.
- [`hardware/opalDevice/docs/ux/opal-screen-designs-v1.md`](hardware/opalDevice/docs/ux/opal-screen-designs-v1.md)
  — pixel-perfect specs for v1 iPhone screens (390×844pt).
- [`hardware/opalDevice/docs/ux/manager-dashboard.md`](hardware/opalDevice/docs/ux/manager-dashboard.md)
  — 10-view dashboard spec (D1–D10) anchored to H6, H10, H13, H17, H18.
- [`hardware/opalDevice/docs/ux/manager-dashboard-wireframes.md`](hardware/opalDevice/docs/ux/manager-dashboard-wireframes.md)
  — ASCII wireframes for global chrome + all 10 views.
- [`hardware/opalDevice/docs/ux/manager-dashboard-screen-designs.md`](hardware/opalDevice/docs/ux/manager-dashboard-screen-designs.md)
  — pixel-perfect specs for reusable patterns + D2/D7/D10 detail.
- [`hardware/opalDevice/docs/ux/v3-design-alignment.md`](hardware/opalDevice/docs/ux/v3-design-alignment.md)
  — maps existing v3 assets to the 10 journeys, identifies gaps
  and required new v3 screens (post-v1-pilot work plan).
- [`hardware/opalDevice/docs/ux/claude-design-briefs.md`](hardware/opalDevice/docs/ux/claude-design-briefs.md)
  — paste-ready prompts for Claude Design (claude.ai/design),
  one per surface and dashboard view + composite journey flows.
- [`hardware/opalDevice/docs/ux/implementation/html-mockups/`](hardware/opalDevice/docs/ux/implementation/html-mockups/)
  — first-pass interactive HTML prototype. Open `index.html`
  in a browser. Covers 6 v1 iPhone surfaces (S1.A, S3.B, S4.A,
  S5.A, S6a, S7.B) + 3 dashboard views (D1, D2, D10) against
  the LYNA design tokens.
- [`hardware/opalDevice/docs/ux/README.md`](hardware/opalDevice/docs/ux/README.md)
  — updated index distinguishing canonical v1 specs from v3 reference material.

**Cumulative changes vs. the prior 7-story shape:**
- §4.6 rewritten from cipro-warfarin safety check → **AI-awareness gap** (H6) — hospital has bought a nursing clinical-reference AI nobody opens; LYNA routes through it and names it. New "hospital AI registry" concept introduced as a per-site Operational KB extension.
- §4.7 moved from **ICU → cardiac step-down (4-East)** — interview #2 was explicit that ICU layout / proximity / experience reduces the gap; BMC V2 names med-surg/cardiac as beachhead and ICU as weaker first market.
- §4.3 setup reframed against **H12** (resource-nurse-offline window as the deployment-window hypothesis).
- §4.8 NEW — isolation-room broadcast. Direct unprompted feature request from Interview #2.
- §4.9 NEW — phone coexistence / camera handoff. H14, the most CNIO-sensitive boundary.
- §4.10 NEW — ad-hoc bedside interpreter session. Title VI compliance + Mt. Sinai catchment; weakest direct-interview anchor of the ten.
- Citation footers ("Interview anchor") added to all ten stories.
- Cross-cutting themes expanded from 3 to 6; added "LYNA as router across the hospital's existing AI investments," "phone coexistence, not replacement," and "session modes for capabilities voice-Q&A alone can't carry."
- §4 preamble rewritten: "seven stories" → "ten stories" with the new descriptors.
- v1 iPhone interaction-flows spec + manager-dashboard spec added (see §3 above).

Cross-referenced from `epic_intelligence/README.md`, `AI-CONTEXT.md`,
`README.md`, and `hardware/opalDevice/docs/ux/README.md`.

PR [#20](https://github.com/collabPGC/OPALproject/pull/20) is draft,
stacked on `feat/baa-irb-templates` (PR #19), open and ready for
review/merge — now carrying the alignment pass + v1 UI design pass.

---

## 2. The immediate next ask (BEFORE any UI design) — DONE

> **User's original words:** "before we do that, let's make sure that the
> user journeys align with the interviews and specific interactions
> captured from the interviews. Please look at the research paper from
> Ruth and **Kofi** and brainstorm and discuss this with me using
> ultra thinking."

(The phrase "Ruth and coffee" in the original prompt was "Ruth and
Kofi" — Kofi Agyeman is on the OPAL team per AI-CONTEXT.)

### Status — completed 2026-05-20

The journey-vs-interview alignment is **done** and applied to
INTELLIGENCE_LAYER.md §4. PR #20 now carries the alignment pass.
See §1 above for the diff summary.

The brainstorm produced six adjustments (A–F), all approved and
applied:

- **A.** Citation footers on §4.1, §4.2, §4.5 (and on every story).
- **B.** §4.6 rewrite from cipro-safety → AI-awareness gap (H6).
- **C.** §4.7 moved from ICU → cardiac step-down.
- **D.** §4.8 NEW isolation-room broadcast.
- **E.** §4.9 NEW phone-coexistence / camera handoff (originally an
  optional 9th journey on the AI-awareness angle; redirected to the
  H14 phone-coexistence gap because §4.6 already absorbed the
  AI-awareness intent and we did not want duplicate stories).
- **F.** §4.3 reframed against H12 (12:00–17:00 resource-offline
  window — adapted to 00:00–05:00 to fit the existing overnight
  shift framing). §4.4 was originally in scope for F but excluded
  during drafting because start-of-shift sign-on doesn't fit the
  midday H12 window; §4.4 now carries an H5/H9-based footer instead.

### Constraints respected

- Direct interview transcripts beyond Interview #1 (David
  Hernandez) and Interview #2 (anonymous ICU travel) **not
  available** — the alignment leaned on the BMC V2 synthesis
  (`i-corps/interviews/interviews-index.md`) and the
  post-39-participants `hypothesis-map.md` H1–H18 for everything
  beyond those two interviews. Cluster-2 transcripts remain an
  open item; if they surface, §4.3 / §4.4 should be cross-validated
  against the charge-nurse and start-of-shift interviews.

### Research sources consulted

In `i-corps/` (already in this repo):

- [`i-corps/data-room/problem-validation-research.md`](i-corps/data-room/problem-validation-research.md)
  — table of contents only; full prose not yet ingested.
- [`i-corps/interviews/interviews-index.md`](i-corps/interviews/interviews-index.md)
  — index of 18 interviews conducted Mar 3–19, 2026 + V1→V2 BMC
  change log. Individual canvases live in Slack (access-restricted
  to team members; **not available** to this session).
- [`i-corps/interviews/interview-scripts-cluster1.md`](i-corps/interviews/interview-scripts-cluster1.md)
  — question scripts + IYE summaries for Interview #1 (David
  Hernandez, float pool) and Interview #2 (anonymous ICU travel).
- [`i-corps/hypothesis-map.md`](i-corps/hypothesis-map.md) — H1–H18
  validated hypotheses, updated post-39-participants.
- [`i-corps/mount-sinai-hub.md`](i-corps/mount-sinai-hub.md) —
  Mt Sinai Regional I-Corps Spring 2026 program hub.

Recommended approach (the user asked for "ultra thinking" —
brainstorm-first, propose-then-implement):

- Brainstorm-first, propose-then-implement was honored: the
  alignment table + proposed adjustments + sample drafts were
  reviewed before any edit was applied.

---

## 3. UI design pass — DONE for v1, dashboard SPEC SHIPPED, v3 deferred

> **User's original ask:** "Let's discuss user flows on the UI
> what are needed. What are the use cases so we can design these
> screens and modules?"

### Status — completed 2026-05-20

Two new specs landed on PR #20:

- [`hardware/opalDevice/docs/ux/opal-interaction-flows.md`](hardware/opalDevice/docs/ux/opal-interaction-flows.md)
  — v1 iPhone-app spec. 10-surface inventory (S1–S10), per-journey
  flows for §4.1–§4.10 of INTELLIGENCE_LAYER.md, reusable patterns
  (mode indicator, AI-source pill, citation footer, voice-surface
  states, execution-layer affordances, compliance moments),
  cross-cutting error handling, and a mapping table from the prior
  8-flow draft. Supersedes the 2025-11-19 draft (preserved in git
  history).
- [`hardware/opalDevice/docs/ux/manager-dashboard.md`](hardware/opalDevice/docs/ux/manager-dashboard.md)
  — companion spec for the web dashboard. 10 views (D1–D10)
  covering adoption, AI routing, top queries, response times,
  abandonment, broadcast coverage, critical alerts, interpreter
  sessions, per-AI-tool detail, and buyer-facing ROI. Anchored to
  H13 (silent abandonment), H6 (AI awareness gap), H10 (CCIO
  needs ROI), H17/H18 (renewal economics).

A new journey §4.10 — **Maya, interpreter mode** — was added to
INTELLIGENCE_LAYER.md to cover language-access at the bedside
(weakest direct-interview anchor of the ten; kept because of
Mt. Sinai catchment language mix + Title VI compliance + the
prior UX doc's Flow 3). Cross-references (`README.md`,
`AI-CONTEXT.md`, `epic_intelligence/README.md`,
`hardware/opalDevice/docs/ux/README.md`) updated to 10 stories.

### Form-factor decisions locked

| Form factor | Status | Notes |
|---|---|---|
| **v1 — iPhone app + Bluetooth earpiece** | spec'd | nurse-side flows + manager dashboard |
| v2 — Vocera-class / Apple Watch | **skipped** | Interview #2 anti-signal: "hated wearing something heavy" |
| **v3 — Dedicated LYNA badge** | **deferred** | separate design pass after v1 pilot data; existing wireframes / screen-designs / LVGL theme remain v3 reference |

### Decisions that locked during the design pass

- **v1 form factor:** iPhone app, not the earlier dedicated-device
  concept. Driven by H14 (phone coexistence), time-to-pilot, and
  the validated bypass-the-screen pattern.
- **v2 skipped intentionally.** Interview #2 explicitly hated
  Vocera; going iPhone (v1) → dedicated optimized hardware (v3)
  avoids the anti-signal.
- **Manager dashboard before v3.** Per user direction: v1 nurse
  surfaces, then manager dashboard, then v3 — because the
  dashboard is the artifact the CCIO needs to renew the pilot,
  and v3 hardware comes after pilot data.
- **Multilingual = §4.10**, not a deferred feature. Title VI
  compliance + Mt. Sinai catchment mix means it ships in v1.
- **§4.6 introduces the "hospital AI registry"** as a per-site
  Operational KB extension. The registry is the data position
  the dashboard's D2 view reads against — surfacing the H6
  awareness gap.

### What was preserved vs replaced from the prior UX work

The earlier docs in `hardware/opalDevice/docs/ux/` (wireframes,
screen designs, LVGL theme) were drawn against the v3
dedicated-device concept. **The design-system bones
(`opal-design-system.md`, `design-tokens.json`) are reusable
as-is for v1 iPhone.** Wireframes and screen designs remain v3
reference material; a separate v3 design pass will re-anchor
them against the 10 journeys. The previously-prominent "demo
mode" + LVGL implementation are explicitly v3-deferred.

---

## 4. What's shipped (PR stack, oldest first)

All draft PRs stacked on top of each other. Merge in order or
squash-merge sequentially.

| PR | Branch | Status | Summary |
|---|---|---|---|
| [#6](https://github.com/collabPGC/OPALproject/pull/6) | `feat/persona-departments-and-tensions` | draft | Persona tiers + departments + productive-tensions matrix |
| [#7](https://github.com/collabPGC/OPALproject/pull/7) | `feat/workflows-and-memory-protocol` | draft | Named business workflows + Memory-First Protocol |
| [#8](https://github.com/collabPGC/OPALproject/pull/8) | `feat/new-personas` | draft | 10 new personas across Board + 4 departments |
| [#9](https://github.com/collabPGC/OPALproject/pull/9) | `feat/memory-system-full-port` | draft | Port collab-memory architecture into OPAL |
| [#10](https://github.com/collabPGC/OPALproject/pull/10) | `feat/epic-intel-crawl-expansion` | draft | 147 files / 8,556 chunks across 5 Epic doc sites |
| [#11](https://github.com/collabPGC/OPALproject/pull/11) | `feat/epic-intel-synthesis` | draft | LLM provider abstraction (stub/anthropic/openai/gemini) + assistant service |
| [#12](https://github.com/collabPGC/OPALproject/pull/12) | `feat/memory-adversarial-review` | draft | Adversarial review for Tier-2 scope transitions (E-1) |
| [#13](https://github.com/collabPGC/OPALproject/pull/13) | `feat/memory-neo4j-projection` | draft | Neo4j projection of typed memory events (E-2) |
| [#14](https://github.com/collabPGC/OPALproject/pull/14) | `feat/workflow-orchestrator` | draft | Workflow orchestrator runtime (A-1) |
| [#15](https://github.com/collabPGC/OPALproject/pull/15) | `feat/persona-emit-protocol` | draft | Persona-authored memory emit protocol + post-write predicates (A-2) |
| [#16](https://github.com/collabPGC/OPALproject/pull/16) | `feat/mattermost-emit-bridge` | draft | JS Mattermost emit bridge — same YAML contract (A-2b) |
| [#17](https://github.com/collabPGC/OPALproject/pull/17) | `feat/briefing-mattermost-cron` | draft | Briefing → Mattermost webhook + cron docs (A-3) |
| [#18](https://github.com/collabPGC/OPALproject/pull/18) | `feat/pilot-site-scoring` | draft | Pilot-site scoring rubric + champion ID (D-1) |
| [#19](https://github.com/collabPGC/OPALproject/pull/19) | `feat/baa-irb-templates` | draft | BAA + IRB workflow YAMLs + operator templates (D-2) |
| [#20](https://github.com/collabPGC/OPALproject/pull/20) | `docs/intelligence-layer-readme` | **current** | INTELLIGENCE_LAYER.md + 10 LYNA stories + v1 iPhone wireframes + v1 screen specs + dashboard wireframes + dashboard screen specs + v3 alignment doc + cross-refs |

**Cumulative test status (last full run):** 282 Python tests passed +
1 skipped (Neo4j live-integration auto-skip when DB unreachable);
16 JS node:test cases passed in `bots/shared/memory-emit/tests/`.

---

## 5. Established design principles (don't re-debate these)

The user has been explicit on these — re-reading them saves the
next session from re-litigating settled ground.

### Memory emission is persona-deliberate, not classifier-driven

The persona itself decides what's memory-worthy and authors a
fenced `memory-emit` YAML block. **No regex / heuristic / LLM
classifier scanning every reply.** Zero blocks = zero events, and
that's the right answer for routine prose. Predicates over the
sparse log do the inference at read time.

Saved in user memory:
`C:\Users\huber\.claude\projects\G--Downloads\memory\feedback-memory-emission.md`.

### LYNA users are clinical staff at the hospital — not the OPAL team

The user pushed back hard when an earlier draft conflated the two.
INTELLIGENCE_LAYER.md is strictly for end users (nurses); internal-
team tooling (orchestrator, pilot rubric, BAA/IRB workflows, memory
log) is documented in their own module READMEs but NOT documented
as "user journeys" in INTELLIGENCE_LAYER.md.

### Epic is the reference EHR throughout

Use real Epic resource names (Patient, Observation,
MedicationAdministration, MedicationRequest, Encounter, Procedure,
DiagnosticReport) and real Epic specs (FHIR R4, Epic on FHIR,
CDS Hooks, SMART on FHIR, Open Epic).

### Always cite sources

LYNA never makes a claim without a citation back to where it came
from (Epic chart, FHIR endpoint, hospital policy, Drug Info,
Operational KB). This applies to every user-facing answer in every
story.

---

## 6. Open follow-ups (not blocking, but on the list)

- **Backpressure evaluation** in the orchestrator runner — workflows
  declare it; runner doesn't evaluate yet.
- **Multi-persona conversation patterns** (debate, panel) — runner
  only invokes lead persona today.
- **Unified event store** across JS-side
  (`bots/shared/institutional-memory/`) and Python-side
  (`memory_system/events/log/`) — needs shared id scheme.
- **Absence-based predictive predicates** (stale ACTION > 30d,
  unverified PREDICTION > 90d) — needs `older_than_days` semantics
  in the predicate engine.
- **Briefing → predicate enrichment** — surface tripped predicates
  in the briefing.
- **RTRevenue worktree cleanup** — leftover files at
  `G:/Downloads/RTRevenue/.claude/worktrees/funny-poincare-337eb2/`
  (user to run manually; not safe to auto-delete).

---

## 7. How to restart in a new session

1. Read this file end-to-end.
2. `git -C G:/Downloads/OPALproject status` — confirm clean working
   tree on `docs/intelligence-layer-readme`.
3. `gh pr view 20` — confirm PR #20 state.
4. If continuing journey work: open
   [`INTELLIGENCE_LAYER.md`](INTELLIGENCE_LAYER.md) §4 +
   `i-corps/interviews/interviews-index.md` before making changes.
5. If continuing UI work for v1:
   [`hardware/opalDevice/docs/ux/opal-interaction-flows.md`](hardware/opalDevice/docs/ux/opal-interaction-flows.md)
   is the canonical spec; v3 reference material is in the same
   directory and clearly marked.
6. If starting the v3 design pass: read both v1 specs first (they
   describe the journeys and behavior the v3 hardware must
   support), then begin the v3 hardware-affordance pass against
   the existing `opal-ui-wireframes.md` / `opal-screen-designs.md`
   / `implementation/lvgl-theme/` material.
7. If starting the dashboard wireframe pass: the spec is
   `manager-dashboard.md`; the implementation starting point is
   `hardware/opalDevice/docs/ux/implementation/react-dashboard/`.

---

## 8. Update protocol for this file

End every working session by updating:

- §1 ("Where we are right now") — current branch + PR + what's done
- §2 ("The immediate next ask") — the next thing the user wants
- §4 (PR stack table) — any new PRs opened or merged
- §6 (Open follow-ups) — add or remove as work lands or new
  follow-ups surface

Keep it under ~250 lines. If it grows past that, the older history
should move into a separate `SESSION_HANDOFF_ARCHIVE.md`.
