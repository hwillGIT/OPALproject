# OPAL Persona Productive Tensions

Pairs of personas that, by design, will reach different conclusions
about the same question. Calling both into a discussion produces
better thinking than either alone. Modeled on the RTRevenue
"Productive Tensions" pattern, adapted to OPAL's hardware + clinical +
regulated context.

This is a *map*, not a rulebook. The discussion orchestrator (PR 2,
under `bots/shared/workflows/`) consults this file when assembling
multi-persona panels for a workflow phase.

---

## How a tension is read

> **A ↔ B** — Tension type → What productive disagreement produces

`A` and `B` will disagree along the named axis. The "produces" column
names what the synthesis is good for. *Neither side is wrong.* The
goal is to surface the trade-off explicitly, not to resolve it
prematurely.

---

## Tier crosses (Advisor ↔ Core Team)

| Tension | Type | Produces |
|---|---|---|
| **Dr. Claire ↔ Helena** | Bedside reality vs. EPIC integration plumbing | Workflow that survives contact with real clinicians |
| **Dr. Devon ↔ Rex** | Executive-buyer skepticism vs. sales conviction | Pitch that withstands a CMO grilling |
| **Vera ↔ Maya** | Industry trends vs. tactical campaigns | Growth strategy aligned with where the market is moving |
| **Adriana ↔ Marcus** | Defensible-claim language vs. shipping architecture | Architecture descriptions that hold up at the USPTO |

## Strategy crosses (within Core Team)

| Tension | Type | Produces |
|---|---|---|
| **Athena ↔ Priya** | Strategic narrative vs. backlog reality | Roadmap that ladders to strategy without fantasy |
| **Athena ↔ Kai** | Long-term positioning vs. quarterly burn | Strategy honest about runway |
| **Athena ↔ Rex** | Where-we-should-go vs. where-the-pipeline-is | Real ICP, not aspirational ICP |

## Engineering ↔ Hardware crosses

| Tension | Type | Produces |
|---|---|---|
| **Marcus ↔ Diego** | Cloud/server architecture vs. firmware constraints | Boundary contracts that respect both worlds |
| **Tensor ↔ Diego** | Model size/latency targets vs. on-device compute budget | ML approach that actually fits the device |
| **Cyrus ↔ Diego** | Security ideal vs. firmware/OTA constraints | Threat model achievable on the actual device |
| **Nimbus ↔ Cyrus** | Operational simplicity vs. security posture | Cloud architecture defensible at audit |
| **Helena ↔ Cyrus** | EPIC integration shape vs. PHI surface minimization | Integration scope that asks for the minimum PHI necessary |
| **Suki ↔ Cyrus** | Compliance/BAA contract language vs. security architecture | BAA redlines that match what the architecture actually does, not what marketing wishes |

## Hardware & Design internal

| Tension | Type | Produces |
|---|---|---|
| **Yuki ↔ Diego** | Form factor wishes vs. physics & BOM | Wearable that's both wearable AND buildable |
| **Sasha ↔ Marcus** | Interaction ideal vs. API/data model reality | Screens that the backend can actually serve |
| **Sasha ↔ Yuki** | Digital surface vs. physical context-of-use | Coherent experience across glasses + companion app |
| **Bjorn ↔ Diego** | Failure-mode coverage vs. ship-the-prototype urgency | Prototype safe enough to put on a real clinician |

## Clinical & Regulatory crosses

| Tension | Type | Produces |
|---|---|---|
| **Regina ↔ Marcus** | FDA documentation burden vs. agile iteration | Engineering process that produces audit-ready evidence as a side effect |
| **Regina ↔ Yuki** | Design-controls discipline vs. design exploration | Controlled design history without killing creativity |
| **Helena ↔ Tensor** | EPIC FHIR contract vs. ML pipeline realities | Models that consume what EPIC actually exposes |
| **Imani ↔ Suki** | Pilot-site reality vs. compliance paperwork | Pilots that get signed AND start on time |
| **Bjorn ↔ Imani** | Lab-bench failure modes vs. real-ward failure modes | FMEA grounded in observed clinical events, not just theory |
| **Dr. Claire ↔ Regina** | Clinician's "we'll figure it out at the bedside" vs. regulatory protocol discipline | Consent + data-use strategy that holds up at IRB without alienating the floor |
| **Regina ↔ Cyrus** | Regulatory data-use language vs. security architecture reality | Data-use statement that the IRB accepts AND the threat model supports |

## Go-to-Market crosses

| Tension | Type | Produces |
|---|---|---|
| **Maya ↔ Rex** | Demand generation vs. enterprise sales motion | Funnel that produces qualified, closeable pipeline |
| **Rex ↔ Suki** | Deal velocity vs. compliance / BAA workflow | Sales motion that doesn't stall at security review |
| **Wei ↔ Rex** | Long-cycle alliance vs. transactional deal | Coverage map that exploits both motions |
| **Wei ↔ Helena** | Strategic integration ambition vs. EPIC-app-orchard reality | Partnership scope that EPIC's process actually permits |
| **Suki ↔ Wei** | Compliance / BAA close timeline vs. partnership relationship building | Pilot-site sign that doesn't burn the relationship for follow-on deals |
| **Regina ↔ Wei** | IRB submission cadence vs. partnership-driven start-date pressure | Realistic pilot start date that doesn't promise IRB review faster than it can deliver |

## Finance & Operations crosses

| Tension | Type | Produces |
|---|---|---|
| **Naomi ↔ Athena** | Capital efficiency vs. strategic ambition | Funded version of the strategy |
| **Naomi ↔ Kai** | Story-quality numbers vs. ground-truth numbers | Numbers that hold up to investor diligence |
| **Ramon ↔ Diego** | Supplier reality vs. design wish-list | BOM that quotes within the funded budget |
| **Ramon ↔ Yuki** | DFM constraints vs. form-factor ideals | Design that survives moulding/assembly |

## Special: the "two clinicians" check

| Tension | Type | Produces |
|---|---|---|
| **Dr. Claire ↔ Dr. Devon** | Floor-level clinician vs. executive medical leader | Position that resonates with both nurses-at-bedside AND C-suite |

A claim about clinical value should pass *both* views. If only one
agrees, the message is mis-aimed.

---

## When to invoke a tension

The PR-2 workflows (under `bots/shared/workflows/`) reference these
tensions explicitly. Default invocation rules:

| Workflow | Required tensions to surface |
|---|---|
| Clinical Decision Loop | Dr. Claire ↔ Helena, Bjorn ↔ Imani |
| Hardware Build Review | Yuki ↔ Diego, Marcus ↔ Diego, Bjorn ↔ Diego |
| Pilot Site Assessment | Imani ↔ Suki, Dr. Claire ↔ Dr. Devon |
| Investor Pitch Review | Naomi ↔ Athena, Athena ↔ Rex, Vera ↔ Maya |
| Regulatory Risk Assessment | Regina ↔ Marcus, Regina ↔ Yuki, Adriana ↔ Marcus |
| Partnership Qualification | Wei ↔ Helena, Wei ↔ Rex |
| BAA Negotiation | Helena ↔ Cyrus, Suki ↔ Cyrus, Suki ↔ Wei |
| IRB Submission | Regina ↔ Cyrus, Dr. Claire ↔ Regina, Regina ↔ Wei |

Workflows are responsible for *making the tension visible* in the
conversation transcript, not for resolving it. Resolution is the
human operator's call.

---

## Anti-pattern

A "productive tension" pair that *always agrees* is broken — either
the personas need redefinition or the tension entry should be
removed. Real tensions trade something material; if both sides give
the same answer, no choice is being made.

---

## Maintenance

Adding or moving a persona requires re-checking this file. The
validation script (`bots/gtm/scripts/validate-personas.js`) only
checks router/DEPARTMENTS consistency — it does not validate
tensions, since the right set of tensions is a judgment call, not a
mechanical property.
