# OPAL Persona Roster — Tiers & Departments

This is the canonical organizational chart for OPAL's persona-driven
team. Every persona belongs to exactly one **tier** and exactly one
**department**. The persona router enforces this — see
`bots/gtm/scripts/validate-personas.js`.

The structure is modeled on the RTRevenue agent topology pattern
(rich personas + Board / Core split + named workflows + memory-first
protocol) but adapted to OPAL's clinical-wearable + ambient-voice +
EPIC-integrated hardware context.

---

## Tier 1: Board of Advisors

External-perspective, gravitas-providing personas. They challenge,
counsel, and stress-test — they don't own delivery. Used when the team
needs an outside voice (clinician, CMO, IP attorney, market analyst).

| Persona | Role | Status |
|---|---|---|
| **Dr. Claire** | Clinical Advisor — practising clinician perspective on workflow + safety | existing |
| **CMO Advisor** | Hospital CMO peer — gravitas for sales credibility + executive sponsorship paths | **new (PR 3)** |
| **Vera** | Healthcare Industry Analyst — payer dynamics, reimbursement, market trends | existing |
| **IP Counsel** | External patent / IP attorney — prosecution strategy, freedom-to-operate, claim defense | **new (PR 3)** |

---

## Tier 2: Core Team — Departments

Internal operators who own delivery. Six departments, each with a
clear charter.

### 1. Strategy & Leadership
> Connects every product/GTM/financial decision to a coherent strategic narrative. Owns the "what should we do differently?" question.

| Persona | Role | Status |
|---|---|---|
| **Athena** | Strategist — frameworks, scenarios, competitive positioning | existing |
| **Priya** | Product Owner — backlog, requirements, acceptance criteria | existing |

### 2. Engineering & Platform
> Cloud, server-side software, security, ML/AI pipelines. Everything that runs *off* the wearable.

| Persona | Role | Status |
|---|---|---|
| **Marcus** | Software Architect — system design, service boundaries | existing |
| **Cyrus** | Security & Privacy Architect — HIPAA, threat modeling, key management | existing |
| **Nimbus** | Cloud Architect — infrastructure, deployment, scaling | existing |
| **Tensor** | ML/AI Engineer — model selection, fine-tuning, retrieval pipelines | existing |

### 3. Hardware & Design
> The physical wearable + every digital surface a clinician touches. Both physical industrial design and digital UI/UX live here so the device-app handoff stays coherent.

| Persona | Role | Status |
|---|---|---|
| **Hardware Lead** | Firmware, ESP32-C6, audio codec, I2C, PCB | **new (PR 3)** |
| **Industrial Designer** | Wearable form factor, ergonomics, human-factors for clinicians | **new (PR 3)** |
| **UI/UX Expert** | Dashboards, mobile apps, EPIC-integration screens, admin consoles | **new (PR 3)** |
| **Reliability Engineer** | Patient-safety failure modes, FMEA, incident analysis | **new (PR 3)** |

### 4. Healthcare & Clinical
> Hospital-system context, regulatory pathway, on-site deployment. Translates between OPAL's tech and the clinical environment it lands in.

| Persona | Role | Status |
|---|---|---|
| **Helena** | Healthcare Enterprise Architect — EPIC/Cerner integration patterns, FHIR | existing |
| **Regina** | Regulatory Affairs Specialist — FDA pathway, software as a medical device | existing |
| **Clinical Ops / Pilot Manager** | Site selection, workflow integration, pilot ROI tracking | **new (PR 3)** |

### 5. Go-to-Market & Partnerships
> Pipeline, narrative, ecosystem. Owns who-we-talk-to and what-we-say.

| Persona | Role | Status |
|---|---|---|
| **Maya** | Growth Lead — campaigns, top-of-funnel, content | existing |
| **Rex** | Sales & BD — deal motion, objection handling, account plans | existing |
| **Suki** | Compliance & Ops — sales-side compliance, BAA workflow | existing |
| **Partnership Lead** | Hospital systems, EPIC App Orchard, payer partnerships | **new (PR 3)** |

### 6. Finance & Operations
> Capital, runway, suppliers. Keeps the company solvent and the prototype line moving.

| Persona | Role | Status |
|---|---|---|
| **Kai** | Finance Analyst — unit economics, model maintenance | existing |
| **CFO** | Term sheets, runway management, investor narrative | **new (PR 3)** |
| **Manufacturing Ops** | Prototype firms, supplier contracts, BOM cost engineering | **new (PR 3)** |

---

## Cross-Functional Bots (no department)

These are platform bots, not personas in a department. They serve
*all* departments and don't take strategic positions.

| Bot | Role |
|---|---|
| **Scout** | Research & PM assistant — file ingestion, deep research, Jira/GitHub integration |
| **Spark** | Team engagement & PM — ceremonies, retros, blocker tracking |

---

## Tier discipline (when to invoke whom)

- **Need an outside voice on a strategic call?** Pull from Board of Advisors.
- **Need someone to *do* the work?** Pull from Core Team.
- **Need cross-functional plumbing (research, file handling, PM)?** Use Scout / Spark.

The persona router (`bots/gtm/persona-router.js`) selects by command
(`!strategist`), channel mapping, mention pattern, or topic detection.
Department + tier fields on each persona enable future routing rules
like "for any strategic question in #leadership, default to Board of
Advisors first, Core Team second."

---

## Roadmap

| Stage | What lands | Status |
|---|---|---|
| **PR 1** (this PR) | DEPARTMENTS.md + TENSIONS.md + department/tier fields on persona-router + validation script | in flight |
| **PR 2** | `bots/shared/workflows/` (named multi-agent workflows) + Memory-First Protocol integration in `memory_system/` | next |
| **PR 3** | The 10 new personas above + their persona files + router wiring | after PR 2 |

---

## Counts

| Tier / Group | Count |
|---|---|
| Board of Advisors | 4 (2 existing + 2 new in PR 3) |
| Strategy & Leadership | 2 |
| Engineering & Platform | 4 |
| Hardware & Design | 4 (0 existing + 4 new in PR 3) |
| Healthcare & Clinical | 3 (2 existing + 1 new in PR 3) |
| Go-to-Market & Partnerships | 4 (3 existing + 1 new in PR 3) |
| Finance & Operations | 3 (1 existing + 2 new in PR 3) |
| Cross-functional bots | 2 |
| **Total personas (Tiers 1+2)** | **24** (14 existing + 10 new) |
| **Total bots** | **2** (cross-functional) |

---

## Source-of-truth contract

`bots/gtm/persona-router.js` carries the `department` and `tier`
metadata fields per persona. `DEPARTMENTS.md` is the human-readable
view of that data. The two MUST agree — `validate-personas.js`
enforces it.

If you change a persona's department or tier, update both. If you add
a new persona, it must appear in:
1. `bots/shared/personas/<dept>/<persona>.md` — the persona file
2. `bots/gtm/persona-router.js` — the router metadata (with `department` + `tier`)
3. `bots/shared/personas/DEPARTMENTS.md` — this file
4. `bots/shared/personas/TENSIONS.md` — productive tensions, if any
