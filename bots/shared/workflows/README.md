# Workflows

Two distinct categories live in this directory:

## 1. Orchestration patterns (`./*.yaml`)

Reusable *how* — how the team debates, reviews, deliberates, or
synthesizes. Domain-agnostic. Each pattern is a DAG of steps that an
orchestrator (skill+role+I/O) can execute.

| Pattern | What it does |
|---|---|
| `dialectic-debate.yaml` | Thesis → antithesis → synthesis, 2 rounds + validator |
| `team-deliberation.yaml` | Full crew roundtable, all perspectives respond |
| `internal-review.yaml` | Self-critique + improvement loop before delivery |
| `deep-research.yaml` | Multi-step research with dialectic refinement |
| `creative-brainstorm.yaml` | Multi-perspective ideation |
| `comprehensive-report.yaml` | 100K+ word reports with memory-tracked continuity |

These are the existing files. **Not changed by PR 2.**

## 2. Business workflows (`./business/*.yaml`) — added in PR 2

Domain-specific *what* — the OPAL-specific multi-persona conversations
the team needs to repeatedly run (clinical, hardware, pilot, investor,
regulatory, partnership). Each business workflow:

- names the **phases** the conversation moves through
- names the **lead persona** and **supporting personas** at each phase
- references the **productive tensions** from
  [`../personas/TENSIONS.md`](../personas/TENSIONS.md) that must be
  surfaced
- declares which **memory event types** it emits (per the Memory-First
  Protocol in [`../../../memory_system/PROTOCOL.md`](../../../memory_system/PROTOCOL.md))
- declares its **backpressure** — the criteria that must be met for
  the workflow to be considered "done"
- optionally points each phase at an orchestration pattern from
  category 1 (e.g., a "stress test" phase uses `dialectic-debate`)

| Workflow | Purpose | Tied to ADR/spec |
|---|---|---|
| `business/clinical-decision-loop.yaml` | Validate any clinician-facing change against bedside reality + EPIC plumbing + reliability | Phase 3 Epic 4 (AI-Enhanced Comms) |
| `business/hardware-build-review.yaml` | Greenlight a build/firmware change without breaking ID, physics, or compliance | Phase 1 hardware (ESP32-C6 + I2C + audio) |
| `business/pilot-site-assessment.yaml` | Qualify a hospital pilot site and define success criteria | Closed-loop pilot task in Jira |
| `business/investor-pitch-review.yaml` | Stress-test a pitch/data-room before external exposure | Funding strategy (OPAL Series A track) |
| `business/regulatory-risk-assessment.yaml` | Score a proposed change against FDA/HIPAA pathway risks | FDA software-as-medical-device pathway |
| `business/partnership-qualification.yaml` | Qualify a hospital-system or App-Orchard partnership opportunity | EPIC App Orchard + payer partnership tracks |

## Validation

`node bots/shared/workflows/validate.js` checks both categories:

- Schema integrity (every required field present)
- Persona references resolve to a real persona key (either in
  `bots/gtm/persona-metadata.js` or marked as `new (PR 3)` in
  [`../personas/DEPARTMENTS.md`](../personas/DEPARTMENTS.md))
- Tension references resolve to a pair in
  [`../personas/TENSIONS.md`](../personas/TENSIONS.md)
- Event types in `emits` are in the Memory-First Protocol vocabulary

Exits 0 on success, 1 on failure. No npm install required.

## When to invoke which

| Situation | Start here |
|---|---|
| "Should we ship this clinical feature?" | `business/clinical-decision-loop.yaml` |
| "Should we approve this hardware spec change?" | `business/hardware-build-review.yaml` |
| "Should we sign this pilot?" | `business/pilot-site-assessment.yaml` |
| "Is this deck ready for [investor]?" | `business/investor-pitch-review.yaml` |
| "Does this change move our FDA risk?" | `business/regulatory-risk-assessment.yaml` |
| "Should we engage with this hospital/payer?" | `business/partnership-qualification.yaml` |
| "We need to debate something abstract" | one of the patterns in this dir |

## Schema for business workflows

```yaml
name: <workflow-id>           # kebab-case, matches filename stem
category: business            # literal
domain: <domain-key>          # clinical | hardware | pilot | investor | regulatory | partnership
version: "1.0"
description: <one-line>
backpressure:                 # workflow is "done" iff ALL true
  - <criterion>
phases:
  - id: <phase-id>            # kebab-case
    lead: <persona-key>       # MUST be a real persona key
    supporting: [<key>, ...]  # optional
    tensions:                 # optional; format: a<>b (must be in TENSIONS.md)
      - persona-a<>persona-b
    pattern: <pattern-name>   # optional; one of the category-1 files
    questions:                # the phase tries to answer these
      - <question>
    output: <artifact-description>
emits:                        # memory event types this workflow appends
  - DECISION                  # one of: DECISION | ACTION | INSIGHT |
  - INSIGHT                   #         PREDICTION | OUTCOME | DEBATE |
  - ARTIFACT                  #         CONTEXT_CHANGE | ARTIFACT
```
