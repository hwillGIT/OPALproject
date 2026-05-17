# pilot — pilot-site scoring rubric + champion ID framework (D-1)

A deterministic, transparent rubric for evaluating candidate pilot
hospitals against the criteria the pilot-site-assessment workflow
(bots/shared/workflows/business/pilot-site-assessment.yaml) already
cares about. The rubric is the operator's **fast-triage tool**; the
workflow is the **deep-dive review**. They share the same vocabulary.

Six weighted dimensions sum to 100. The rubric is opinionated about
weights — see `models.py:DIMENSION_WEIGHTS` — but every contribution
is surfaced with a rationale so the operator can argue with the
score, not just live with it.

| Dimension | Weight | What it scores |
|---|---:|---|
| `clinical_fit` | 25% | pain felt, week-1 plausible, named champion (scored separately) |
| `integration_feasibility` | 20% | EPIC build supported, FHIR exposed, device path |
| `compliance_burden` | 15% | BAA timeline, IRB status, security review path |
| `executive_resonance` | 15% | CMO alignment, C-suite metric mapped |
| `deal_economics` | 15% | pricing fit, reference-design value |
| `operator_ground_truth` | 10% | site bandwidth, signer accessibility |

Verdicts:

- **GO** — total ≥ 75 — proceed to contract once gaps closed
- **HOLD** — 55–74 — worth pursuing, fix gaps first
- **NO_GO** — < 55 — not now; revisit when gaps move

## CLI

```bash
# Score a site
python -m pilot.cli score pilot/examples/strong-fit.yaml

# Same, as JSON for piping into a brief / memory event
python -m pilot.cli score pilot/examples/mt-sinai.yaml --json

# Rank the champion candidates at a site
python -m pilot.cli champions pilot/examples/mt-sinai.yaml

# List bundled examples
python -m pilot.cli example
```

## Authoring a site YAML

Field-for-field mirror of `models.py:Site`. Most fields are booleans
defaulting to `false` (unknown is treated as "no" — surfaces the gap
as a score). The example files are designed as starting templates:

- `examples/strong-fit.yaml` — all gates pass (anchors the upper end)
- `examples/weak-fit.yaml` — classic IT-led + unsupported-EPIC failure
- `examples/mt-sinai.yaml` — Mt Sinai template, populated to where
  Ruth's actual knowledge already covers; the rest defaults to false
  by design so the discovery gaps surface as score deductions

## Champion framework

Champion scoring (see `champion.py`) is intentionally weighted
**motivation > authority** because:

- A high-authority bored executive ghosts.
- A passionate floor manager unblocks weekly and creates escalation
  paths the operator can pull on.

Weights:

| Dimension | Weight | Notes |
|---|---:|---|
| `motivation` (0–10) | 40% | does this person care about THIS problem? |
| `authority_level` (0–3) | 35% | 0=floor, 1=manager, 2=director, 3=VP/C-suite |
| `bandwidth` (0–10) | 15% | will they have time? |
| `evidence` (list) | 10% | concrete trace — meeting, quote, action. Capped at 2 entries; stuffing the list doesn't help. |

Risks flag low-motivation / no-evidence / low-bandwidth candidates
explicitly so the operator doesn't bank on someone aspirational.

## Programmatic use

```python
from pilot import load_site, score_site, rank_champions

site = load_site("pilot/examples/mt-sinai.yaml")
result = score_site(site)
print(result.verdict, result.total)
for d in result.dimensions:
    print(d.dimension.value, d.score, d.gaps)

for ranking in rank_champions(site.champion_candidates):
    print(ranking.candidate.name, ranking.score, ranking.risks)
```

## How this pairs with the orchestrator

The pilot-site-assessment workflow asks personas to *judge* a site;
this rubric *scores* one. Two natural integrations (not in scope for
D-1, but obvious follow-ups):

1. **Workflow phase consumes the rubric.** A new phase could call
   `score_site(site)` and pass the dimension breakdown into the
   persona prompt as ground-truth context — the persona then argues
   with or extends the score rather than re-deriving it.
2. **Operator emits the assessment as an INSIGHT.** The CLI's
   `--json` output is shaped to feed straight into
   `python -m memory_system.events.cli write --type INSIGHT
   --title "..." --content "$(cat assessment.json)"` so the briefing
   layer surfaces the score next time.

## Layout

```
pilot/
├── __init__.py
├── models.py         # Site, ChampionCandidate, Dimension, Verdict, weights
├── scoring.py        # score_site — per-dimension + weighted total + verdict
├── champion.py       # score_champion + rank_champions
├── loader.py         # YAML -> Site
├── cli.py            # score / champions / example subcommands
├── examples/
│   ├── strong-fit.yaml
│   ├── weak-fit.yaml
│   └── mt-sinai.yaml
└── tests/
    ├── test_scoring.py
    ├── test_champion.py
    └── test_loader.py
```
