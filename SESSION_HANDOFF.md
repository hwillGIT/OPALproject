# Session Handoff — OPAL Intelligence Layer Documentation

**Last updated:** 2026-05-20
**Branch we're on:** `docs/intelligence-layer-readme` (PR [#20](https://github.com/collabPGC/OPALproject/pull/20))
**Repo:** `collabPGC/OPALproject` (org repo)

Use this file to bring a fresh session up to speed without re-reading
the whole transcript. Update it at the end of each working session.

---

## 1. Where we are right now

**Nine** LYNA clinical-staff user stories live in
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

**Changes vs. the prior 7-story shape:**
- §4.6 rewritten from cipro-warfarin safety check → **AI-awareness gap** (H6) — hospital has bought a nursing clinical-reference AI nobody opens; LYNA routes through it and names it. New "hospital AI registry" concept introduced as a per-site Operational KB extension.
- §4.7 moved from **ICU → cardiac step-down (4-East)** — interview #2 was explicit that ICU layout / proximity / experience reduces the gap; BMC V2 names med-surg/cardiac as beachhead and ICU as weaker first market.
- §4.3 setup reframed against **H12** (resource-nurse-offline window as the deployment-window hypothesis).
- §4.8 NEW — isolation-room broadcast. Direct unprompted feature request from Interview #2.
- §4.9 NEW — phone coexistence / camera handoff. H14, the most CNIO-sensitive boundary.
- Citation footers ("Interview anchor") added to all nine stories.
- Cross-cutting themes expanded from 3 to 5; added "LYNA as router across the hospital's existing AI investments" and "phone coexistence, not replacement."
- §4 preamble rewritten: "seven stories" → "nine stories" with the new descriptors.

Cross-referenced from `epic_intelligence/README.md` and `AI-CONTEXT.md`.

PR [#20](https://github.com/collabPGC/OPALproject/pull/20) is draft,
stacked on `feat/baa-irb-templates` (PR #19), open and ready for
review/merge — now carrying the alignment pass on top of the
original 7-story draft.

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
- Build a side-by-side table: each interview theme → which of
  our 7 journeys covers it / which doesn't.
- Surface 3–5 candidate adjustments (rewrites, additions,
  removals) and discuss with the user BEFORE editing.
- The user has been firm about not just charging ahead on doc
  changes — they want to talk through findings first.

---

## 3. The next-next ask (after journey alignment)

Once the journeys are validated against interviews, the user wants
to move into **UI design**:

> "Let's discuss user flows on the UI what are needed. What are the
> use cases so we can design these screens and modules?"

### What this likely needs

- A list of UI surfaces (LYNA v1 is iPhone-app; v2 is Vocera /
  Apple Watch; v3+ is the dedicated LYNA badge). Each surface has
  different affordances.
- Per-journey screen flow: what does Sarah see/hear at each step?
  What about Linh? What about Sofia in an emergency?
- A modules list: voice-input, voice-output, on-device display,
  charge-nurse dashboard, etc.

Best done AFTER the journey-vs-interview alignment, because the
journey shape determines the screen shape.

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
| [#20](https://github.com/collabPGC/OPALproject/pull/20) | `docs/intelligence-layer-readme` | **current** | INTELLIGENCE_LAYER.md + 9 LYNA user stories (alignment pass over original 7) + cross-refs |

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
4. If continuing the journey/interview alignment: open
   `i-corps/data-room/problem-validation-research.md` and
   `i-corps/interviews/interviews-index.md` BEFORE making changes.
5. If pivoting to UI design: only after the alignment review is
   done; check this file's §3 for the UI-design framing.

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
