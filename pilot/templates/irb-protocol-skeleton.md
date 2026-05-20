# IRB Protocol Skeleton

A starting structure for the IRB protocol document submitted alongside
the `irb-submission` workflow. Every site's IRB has its own forms — this
skeleton populates the **content** they expect; the operator wraps it
in the site's specific cover sheets.

Companion to:

- `bots/shared/workflows/business/irb-submission.yaml` — the
  workflow this skeleton drives
- `pilot/templates/baa-checklist.md` — runs in parallel; BAA + IRB
  often share the same compliance window

The headings below are the ones most US academic medical center IRBs
expect. Sections in *italics* are commonly required by federal
regulation (45 CFR 46) and should not be omitted regardless of which
site you're submitting to.

---

## 1. Protocol Identification

- **Title:** {{specific, not "AI in healthcare"}}
- **Principal Investigator:** {{name, title, affiliation, CITI on file}}
- **Co-investigators:** {{names + roles}}
- **Sponsor:** OPAL, Inc.
- **Funding source:** {{seed / NIH / internal}}
- **Conflict of interest disclosures:** {{per investigator}}

## 2. *Background and Rationale*

Two paragraphs:

1. The clinical problem (nursing communication crisis: 45 min/shift
   lost to outdated comms; 70% of serious safety events tied to
   communication failures).
2. The proposed intervention (LYNA) and the specific outcome we
   expect this pilot to measure.

Cite the prior work this protocol builds on.

## 3. *Specific Aims / Objectives*

Numbered list of falsifiable aims. Each aim must specify the
metric, the comparator, and the success threshold.

Example aim:
> 1. Determine whether LYNA reduces time-to-patient-information
>    retrieval by ≥ 30% on a 5-bed sample unit, measured by RFID +
>    self-report timing logs over 4 weeks.

## 4. *Methods*

### 4.1 Study design

- Type: {{prospective observational / single-arm pilot / etc.}}
- Duration: {{weeks}}
- Site(s): {{name}}
- Sample size + rationale (do NOT skip this — even pilots need it)

### 4.2 Inclusion / Exclusion criteria

- **Inclusion:** {{e.g. RNs on the participating unit during their
  scheduled shifts}}
- **Exclusion:** {{e.g. agency / float staff, traveling staff, patients
  under 18}}

### 4.3 Procedures

Step-by-step: enrollment → consent → device handoff → daily use →
data capture → debrief.

### 4.4 Data collection

(This MUST match the BAA's PHI scope. Cross-reference
`pilot/templates/baa-checklist.md` §1.)

| Variable | Source | Format | Identifier status |
|---|---|---|---|
| {{e.g. communication latency}} | RFID timestamps | seconds | de-identified |
| {{e.g. user satisfaction}} | Survey | 1-5 Likert | de-identified |
| {{e.g. floor patient count}} | EHR (Census) | integer | aggregate |

### 4.5 Data analysis

- **Primary endpoint analysis:** {{statistical test, alpha}}
- **Secondary endpoints:** {{briefly}}
- **Stopping rules:** {{conditions that halt the pilot early}}

## 5. *Human Subjects Protections*

### 5.1 Risk assessment

- **Anticipated risks:** {{e.g. workflow disruption, additional
  cognitive load during initial 2 days}}
- **Mitigation:** {{e.g. clinical champion on-floor for first week, opt-out
  at any time, sub-second device latency target}}
- **Risk classification:** minimal-risk per 45 CFR 46.102(j)
  (or justify otherwise)

### 5.2 Consent strategy

(Mirror the decision recorded in the `consent-strategy` phase of the
`irb-submission` workflow.)

- ☐ Informed consent (attach consent form)
- ☐ Waiver of informed consent under 45 CFR 46.116(f) — rationale:
- ☐ QI determination only — rationale + reference to institution's QI
  policy

### 5.3 Privacy + confidentiality

- HIPAA Safe Harbor de-identification applied to {{which datasets}}
- BAA in place with {{site}} as of {{date}} — see
  `pilot/templates/baa-checklist.md`
- Data retention: {{N days post-pilot}} then secure destruction per
  {{NIST 800-88 / institutional standard}}
- Breach notification: {{tied to BAA terms — keep aligned}}

### 5.4 Vulnerable populations

(Most pilots don't enroll vulnerable populations directly, but
patients on the participating unit may be — address even if minimal.)

## 6. *Investigator Qualifications + Training*

- CITI Good Clinical Practice (current)
- HIPAA training (institution-specific)
- Site-specific orientation completed

## 7. References

(Cite 5-10 papers that ground the rationale + methodology. Light is
better than heavy here — IRB reviewers skim.)

## 8. Appendices

- A. Consent form (if applicable)
- B. Survey instruments
- C. Data dictionary (mirrors BAA scope table)
- D. Device specifications + clinical-grade certification
- E. Prior IRB approvals at other sites (if any)

---

## After approval

Emit one ARTIFACT memory event recording the approved protocol +
approval date + amendment-triggering change list. The
`irb-submission` workflow's `review-timeline-and-amendments` phase
produces this; the orchestrator emits the events automatically.

```memory-emit
- type: ARTIFACT
  title: IRB-approved protocol — {{site name}}
  content: |
    Approval date, IRB classification (exempt/expedited/full),
    expiration / continuing-review date, amendment-triggering changes.
  related: [evt-... (the IRB-submission DECISION)]
  tags: [irb, {{site-slug}}, compliance, regulatory]
```
