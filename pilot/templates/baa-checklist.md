# BAA Checklist

Walks the operator + compliance-ops persona through a candidate site's
Business Associate Agreement from "we got their template" to "signed
both ways" without burning weeks on theatrical legal review.

Companion to:

- `bots/shared/workflows/business/baa-negotiation.yaml` — the
  workflow this checklist drives
- `pilot/` rubric — the `compliance_burden` dimension uses
  `baa_path_days` which this checklist sets

Use a fresh copy of this checklist per candidate site. Fill in as you
go. Anything still blank at sign time is a known risk you're
accepting; record those as `CONTEXT_CHANGE` memory events.

---

## 1. PHI scope (phase: scope-the-phi)

| Item | Done | Notes |
|------|:---:|------|
| FHIR resources OPAL reads at this site | ☐ | e.g. Patient, MedicationRequest, Observation |
| FHIR resources OPAL writes (if any) | ☐ | |
| Fields touched per resource | ☐ | enumerate by element name |
| What stays transient (in-memory only) | ☐ | |
| What's at rest in OPAL's environment | ☐ | duration + storage location |
| What never leaves the site's network | ☐ | local-only data |
| PHI flow diagram attached | ☐ | table form is fine; arrows showing source -> sink |

## 2. Their template (phase: read-their-template)

| Item | Done | Notes |
|------|:---:|------|
| BAA template received (PDF/Word) | ☐ | from whom, date |
| Read end-to-end (not skimmed) | ☐ | |
| Standard HHS-sample clauses identified | ☐ | typically §§1–4 |
| Custom clauses identified | ☐ | line-numbered list |
| Cross-referenced documents identified | ☐ | security addenda, audit rights, subcontractor policy |
| Counsel of record at the site | ☐ | name, email |

## 3. Friction clauses (phase: identify-friction)

For each clause we'll redline, fill one row:

| Clause # | Their text (1-line) | Our concern | Our proposed text | Rationale |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

Common friction patterns to watch for:

- **Breach notification timeline** — they may require 24h; HHS says 60d.
  Negotiate to a reasonable middle (often 48-72h for OPAL to investigate
  + notify).
- **Data-use limits** — model improvement / aggregate analytics may not
  fit their default language. State plainly what we use the data for;
  carve out de-identified aggregates if applicable.
- **Audit rights** — unbounded audit rights are expensive. Counter-propose
  annual scheduled audit + reasonable cost-shifting for ad-hoc.
- **Subcontractor flow-down** — they want every sub to sign mirror
  language. Real but manageable.
- **Termination + data return** — they may want destruction in 30 days.
  If OPAL needs to retain for outcome verification, name that explicitly.

## 4. Counterparty (phase: counterparty-position)

| Item | Done | Notes |
|------|:---:|------|
| BAA signatory (name, title, email) | ☐ | who actually signs |
| Negotiator (name, title, email) | ☐ | often different from signer |
| Documented median signing time at this institution | ☐ | days |
| Prior pilots / BAAs at this institution we can reference | ☐ | shorten the cycle |

## 5. Timeline (phase: timeline-and-blockers)

Build a dated critical-path table:

| Step | Owner | Target date | Predictable stall | Escalation trigger |
|---|---|---|---|---|
| Initial redline sent | | | | |
| Their counsel review | | | legal queue length | >X days no response |
| Our counter-redline | | | | |
| Exec sign (theirs) | | | exec calendar / holiday | |
| Exec sign (ours) | | | | |

**Latest signed-by date that still preserves the pilot start:** ____________

## 6. Sign or walk (phase: sign-or-walk)

Three questions to answer in writing before either path:

1. **Are residual disagreements material to OPAL's product, or
   legal-theater?**
2. **Does the timeline still fit inside the pilot's evaluation window?**
3. **If we sign as-is, what risk are we accepting? If we walk, what's
   the cost?**

Record the DECISION as a memory event (the workflow emits this
automatically via the orchestrator):

```memory-emit
- type: DECISION
  title: BAA signed / BAA walked — {{site name}}
  content: |
    Verdict + 2-3 sentence rationale.
  related: [evt-... (the site's earlier compliance INSIGHT)]
  tags: [baa, {{site-slug}}, compliance]
- type: ARTIFACT
  title: Final BAA — {{site name}}
  content: |
    Pointer to the signed PDF + 1-line summary of negotiated changes.
```

(If walked, replace ARTIFACT with a CONTEXT_CHANGE recording what
would change our mind.)
