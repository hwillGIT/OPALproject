"""Unit tests for site scoring.

Cover the per-dimension scoring + the verdict thresholds + the
end-to-end on the bundled example sites (the examples ARE the
calibration anchors — strong-fit should land GO, weak-fit NO_GO).
"""
from __future__ import annotations

from pathlib import Path

import pytest

from pilot.loader import load_site
from pilot.models import (
    DIMENSION_WEIGHTS,
    ChampionCandidate,
    Dimension,
    Site,
    Verdict,
)
from pilot.scoring import score_site


EXAMPLES = Path(__file__).resolve().parent.parent / "examples"


# --------------------------------------------------------------------------
# Helpers — minimal site builders
# --------------------------------------------------------------------------


def _empty_site(**kw) -> Site:
    """An absolute-worst-case site so each test can flip exactly one
    dimension on and assert its contribution in isolation."""
    base = dict(
        name="t",
        clinical_pain_addressed=False,
        week_one_plausible=False,
        champion_candidates=(),
        cmo_aligned=False,
        c_suite_metric_mapped=False,
        epic_version="",
        epic_supported=False,
        fhir_endpoints_exposed=False,
        device_provisioning_path=False,
        baa_path_days=None,
        irb_required=None,
        security_review_path=False,
        pricing_fit=False,
        reference_design_value=False,
        site_bandwidth=False,
        decision_maker_accessible=False,
    )
    base.update(kw)
    return Site(**base)


# --------------------------------------------------------------------------
# Verdict bucketing
# --------------------------------------------------------------------------


class TestVerdicts:
    def test_empty_site_lands_no_go(self) -> None:
        result = score_site(_empty_site(name="empty"))
        assert result.verdict == Verdict.NO_GO
        assert result.total < 55

    def test_strong_fit_example_is_go(self) -> None:
        site = load_site(EXAMPLES / "strong-fit.yaml")
        result = score_site(site)
        assert result.verdict == Verdict.GO
        assert result.total >= 75

    def test_weak_fit_example_is_no_go(self) -> None:
        site = load_site(EXAMPLES / "weak-fit.yaml")
        result = score_site(site)
        assert result.verdict == Verdict.NO_GO
        assert result.total < 55

    def test_mt_sinai_template_lands_in_hold_or_no_go(self) -> None:
        # The Mt Sinai template defaults most fields to false/unknown
        # because the discovery work hasn't happened — by design.
        # That should NOT land GO; it should be HOLD or NO_GO so the
        # operator knows the discovery gaps.
        site = load_site(EXAMPLES / "mt-sinai.yaml")
        result = score_site(site)
        assert result.verdict in {Verdict.HOLD, Verdict.NO_GO}


# --------------------------------------------------------------------------
# Per-dimension contribution
# --------------------------------------------------------------------------


class TestClinicalFit:
    def test_pain_addressed_alone_adds_weighted_points(self) -> None:
        s = _empty_site(clinical_pain_addressed=True)
        result = score_site(s)
        cf = next(d for d in result.dimensions if d.dimension == Dimension.CLINICAL_FIT)
        # raw 40 * 0.25 = 10.0
        assert cf.score == 40.0
        assert cf.weighted == 10.0

    def test_champion_contributes_proportional_to_score(self) -> None:
        good = ChampionCandidate(
            name="g", role="r", authority_level=3, bandwidth=10, motivation=10,
            evidence=("a", "b"),
        )
        s = _empty_site(
            name="x", clinical_pain_addressed=True, week_one_plausible=True,
            champion_candidates=(good,),
        )
        result = score_site(s)
        cf = next(d for d in result.dimensions if d.dimension == Dimension.CLINICAL_FIT)
        # 40 (pain) + 25 (week 1) + 35 (champ * 0.35) = 100
        assert cf.score == 100.0

    def test_no_champion_produces_explicit_gap(self) -> None:
        s = _empty_site(clinical_pain_addressed=True, week_one_plausible=True)
        result = score_site(s)
        cf = next(d for d in result.dimensions if d.dimension == Dimension.CLINICAL_FIT)
        assert any("No champion candidate identified" in g for g in cf.gaps)


class TestIntegrationFeasibility:
    def test_unsupported_epic_is_hard_stop_signal(self) -> None:
        s = _empty_site(epic_version="Aug 2019", epic_supported=False)
        result = score_site(s)
        d = next(d for d in result.dimensions if d.dimension == Dimension.INTEGRATION_FEASIBILITY)
        assert d.score == 0.0
        assert any("hard-stop" in g for g in d.gaps)

    def test_supported_epic_plus_endpoints_scores_high(self) -> None:
        s = _empty_site(
            epic_version="May 2023", epic_supported=True,
            fhir_endpoints_exposed=True, device_provisioning_path=True,
        )
        result = score_site(s)
        d = next(d for d in result.dimensions if d.dimension == Dimension.INTEGRATION_FEASIBILITY)
        assert d.score == 100.0


class TestComplianceBurden:
    def test_fast_baa_no_irb_scores_high(self) -> None:
        s = _empty_site(baa_path_days=21, irb_required=False, security_review_path=True)
        result = score_site(s)
        d = next(d for d in result.dimensions if d.dimension == Dimension.COMPLIANCE_BURDEN)
        # 40 (fast BAA) + 35 (no IRB) + 25 (security) = 100
        assert d.score == 100.0

    def test_slow_baa_with_irb_scores_low(self) -> None:
        s = _empty_site(baa_path_days=180, irb_required=True, security_review_path=False)
        result = score_site(s)
        d = next(d for d in result.dimensions if d.dimension == Dimension.COMPLIANCE_BURDEN)
        # 5 (slow) + 15 (IRB) + 0 = 20
        assert d.score == 20.0

    def test_unknown_baa_is_called_out_as_risky(self) -> None:
        s = _empty_site()  # baa_path_days=None
        result = score_site(s)
        d = next(d for d in result.dimensions if d.dimension == Dimension.COMPLIANCE_BURDEN)
        assert any("BAA timeline unknown" in g for g in d.gaps)


# --------------------------------------------------------------------------
# Weighting + summary
# --------------------------------------------------------------------------


class TestWeightingAndSummary:
    def test_weights_sum_to_one(self) -> None:
        assert abs(sum(DIMENSION_WEIGHTS.values()) - 1.0) < 1e-9

    def test_total_is_sum_of_weighted_dimensions(self) -> None:
        site = load_site(EXAMPLES / "strong-fit.yaml")
        result = score_site(site)
        assert abs(result.total - sum(d.weighted for d in result.dimensions)) < 0.2

    def test_summary_names_top_gaps(self) -> None:
        site = load_site(EXAMPLES / "weak-fit.yaml")
        result = score_site(site)
        assert "NO_GO" in result.summary
        assert "Top gaps:" in result.summary
