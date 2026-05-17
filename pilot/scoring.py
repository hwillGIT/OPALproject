"""Score a candidate pilot site against the rubric.

Pure functions of the Site dataclass. Each dimension produces a 0-100
score, a list of rationale bullets (why the score), and a list of
gaps (what would need to change to lift the score). The dimension
scores are then weighted (see DIMENSION_WEIGHTS) into a 0-100 total
and bucketed into a Verdict.

No LLM, no I/O. Deterministic. The same Site always produces the
same SiteAssessment.
"""
from __future__ import annotations

from .champion import score_champion
from .models import (
    DIMENSION_WEIGHTS,
    VERDICT_THRESHOLDS,
    Dimension,
    DimensionScore,
    Site,
    SiteAssessment,
    Verdict,
)


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def score_site(site: Site) -> SiteAssessment:
    """Score a site across all six dimensions; return the assessment."""
    dim_scores = [
        _score_clinical_fit(site),
        _score_executive_resonance(site),
        _score_integration_feasibility(site),
        _score_compliance_burden(site),
        _score_deal_economics(site),
        _score_operator_ground_truth(site),
    ]
    total = round(sum(d.weighted for d in dim_scores), 1)
    verdict = _verdict_for(total)
    summary = _summarize(site, total, verdict, dim_scores)
    return SiteAssessment(
        site_name=site.name,
        total=total,
        verdict=verdict,
        dimensions=tuple(dim_scores),
        summary=summary,
    )


# ---------------------------------------------------------------------------
# Per-dimension scoring
# ---------------------------------------------------------------------------


def _score_clinical_fit(site: Site) -> DimensionScore:
    """Clinical fit: champion + felt pain + plausible week-one."""
    score = 0.0
    rationale: list[str] = []
    gaps: list[str] = []

    if site.clinical_pain_addressed:
        score += 40
        rationale.append("Clinicians at this site feel the pain OPAL addresses.")
    else:
        gaps.append("No evidence the floor clinicians feel OPAL-shaped pain.")

    if site.week_one_plausible:
        score += 25
        rationale.append("A week-1 day-in-the-life with OPAL has been described.")
    else:
        gaps.append("No week-1 day-in-the-life has been mapped.")

    # Champion: best candidate's score, scaled to 35 points
    if site.champion_candidates:
        best_score = max(score_champion(c).score for c in site.champion_candidates)
        champ_pts = round(0.35 * best_score, 1)
        score += champ_pts
        rationale.append(
            f"Best champion candidate scores {best_score:.0f}/100 "
            f"({champ_pts:.0f}/35 weighted)."
        )
        if best_score < 60:
            gaps.append(
                "No champion candidate clears the 60/100 bar — the named "
                "champion is the workflow's backpressure gate."
            )
    else:
        gaps.append(
            "No champion candidate identified — backpressure gate of the "
            "pilot-site-assessment workflow is unmet."
        )

    return _build_dim_score(Dimension.CLINICAL_FIT, score, rationale, gaps)


def _score_executive_resonance(site: Site) -> DimensionScore:
    score = 0.0
    rationale: list[str] = []
    gaps: list[str] = []
    if site.cmo_aligned:
        score += 60
        rationale.append("CMO (or equivalent) has echoed the floor's pain.")
    else:
        gaps.append("CMO alignment not confirmed.")
    if site.c_suite_metric_mapped:
        score += 40
        rationale.append("A specific C-suite-tracked metric this moves is named.")
    else:
        gaps.append("No specific C-suite metric mapped — investor-grade evidence missing.")
    return _build_dim_score(Dimension.EXECUTIVE_RESONANCE, score, rationale, gaps)


def _score_integration_feasibility(site: Site) -> DimensionScore:
    """Hard-stop dimension. An unsupported EPIC build is a near-zero."""
    score = 0.0
    rationale: list[str] = []
    gaps: list[str] = []

    if site.epic_version and site.epic_supported:
        score += 50
        rationale.append(
            f"EPIC {site.epic_version} is supported by our integration."
        )
    elif site.epic_version and not site.epic_supported:
        gaps.append(
            f"EPIC {site.epic_version} is in production but our integration "
            "does not yet support it — hard-stop unless we extend support."
        )
    else:
        gaps.append("EPIC build/version at the site is unknown.")

    if site.fhir_endpoints_exposed:
        score += 30
        rationale.append("FHIR resources we need are live + reachable.")
    else:
        gaps.append("FHIR endpoints we need are not confirmed exposed.")

    if site.device_provisioning_path:
        score += 20
        rationale.append("Device provisioning path (wifi/MDM/segmentation) is mapped.")
    else:
        gaps.append("Device provisioning path is undefined.")

    return _build_dim_score(Dimension.INTEGRATION_FEASIBILITY, score, rationale, gaps)


def _score_compliance_burden(site: Site) -> DimensionScore:
    """BAA timeline, IRB status, security review."""
    score = 0.0
    rationale: list[str] = []
    gaps: list[str] = []

    if site.baa_path_days is None:
        gaps.append("BAA timeline unknown — treat as risky.")
    elif site.baa_path_days <= 30:
        score += 40
        rationale.append(f"BAA path estimated at {site.baa_path_days} days — fast.")
    elif site.baa_path_days <= 90:
        score += 25
        rationale.append(f"BAA path estimated at {site.baa_path_days} days — workable.")
    else:
        score += 5
        rationale.append(f"BAA path estimated at {site.baa_path_days} days — slow.")
        gaps.append("BAA timeline >90 days will compress pilot evaluation window.")

    if site.irb_required is None:
        gaps.append("IRB requirement is unknown.")
    elif site.irb_required is False:
        score += 35
        rationale.append("No IRB required — no separate review timeline.")
    else:
        score += 15
        rationale.append("IRB required — adds a parallel review timeline.")
        gaps.append("IRB protocol + submission timeline must be mapped.")

    if site.security_review_path:
        score += 25
        rationale.append("Security review queue + owner identified.")
    else:
        gaps.append("Security review path (queue + owner) is undefined.")

    return _build_dim_score(Dimension.COMPLIANCE_BURDEN, score, rationale, gaps)


def _score_deal_economics(site: Site) -> DimensionScore:
    score = 0.0
    rationale: list[str] = []
    gaps: list[str] = []
    if site.pricing_fit:
        score += 60
        rationale.append("Pricing band matches what this hospital pays for similar tools.")
    else:
        gaps.append("Pricing fit unconfirmed — quoting may stall.")
    if site.reference_design_value:
        score += 40
        rationale.append(
            "A discounted pilot here generates outsized follow-on value "
            "(reference architecture for the segment)."
        )
    else:
        gaps.append("No clear reference-design upside; the pilot must pay its own way.")
    return _build_dim_score(Dimension.DEAL_ECONOMICS, score, rationale, gaps)


def _score_operator_ground_truth(site: Site) -> DimensionScore:
    score = 0.0
    rationale: list[str] = []
    gaps: list[str] = []
    if site.site_bandwidth:
        score += 50
        rationale.append("Site has a named person who will run the pilot day-to-day.")
    else:
        gaps.append("No on-site operator named — high risk of being ghosted post-signing.")
    if site.decision_maker_accessible:
        score += 50
        rationale.append("We can reach the signer in under 2 weeks.")
    else:
        gaps.append("Decision-maker is hard to reach — contract cycle will slip.")
    return _build_dim_score(Dimension.OPERATOR_GROUND_TRUTH, score, rationale, gaps)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _build_dim_score(
    dim: Dimension,
    raw_score: float,
    rationale: list[str],
    gaps: list[str],
) -> DimensionScore:
    capped = max(0.0, min(100.0, raw_score))
    weighted = round(capped * DIMENSION_WEIGHTS[dim], 1)
    return DimensionScore(
        dimension=dim,
        score=round(capped, 1),
        weighted=weighted,
        rationale=tuple(rationale),
        gaps=tuple(gaps),
    )


def _verdict_for(total: float) -> Verdict:
    if total >= VERDICT_THRESHOLDS[Verdict.GO]:
        return Verdict.GO
    if total >= VERDICT_THRESHOLDS[Verdict.HOLD]:
        return Verdict.HOLD
    return Verdict.NO_GO


def _summarize(
    site: Site,
    total: float,
    verdict: Verdict,
    dims: list[DimensionScore],
) -> str:
    """One-paragraph human-readable verdict + the top 2-3 gaps."""
    all_gaps: list[str] = []
    for d in dims:
        all_gaps.extend(d.gaps)
    top_gaps = all_gaps[:3]
    parts = [
        f"{site.name}: {verdict.value.upper()} ({total:.1f}/100).",
    ]
    if verdict == Verdict.GO:
        parts.append("Proceed to contract once the named gaps are closed.")
    elif verdict == Verdict.HOLD:
        parts.append("Worth pursuing — but fix the named gaps before signing.")
    else:
        parts.append("Not worth pursuing right now; revisit if the gaps move.")
    if top_gaps:
        parts.append("Top gaps: " + "; ".join(top_gaps))
    return " ".join(parts)
