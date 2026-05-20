"""Data models for the pilot-site rubric.

The Site dataclass is what an operator describes about a candidate
hospital — a fixed-shape input the scoring engine consumes. Every
field maps to a question the pilot-site-assessment workflow asks.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


# ---------------------------------------------------------------------------
# Dimensions + weights
# ---------------------------------------------------------------------------


class Dimension(str, Enum):
    """The six scoring dimensions, named to match the workflow phases."""

    CLINICAL_FIT = "clinical_fit"
    EXECUTIVE_RESONANCE = "executive_resonance"
    INTEGRATION_FEASIBILITY = "integration_feasibility"
    COMPLIANCE_BURDEN = "compliance_burden"
    DEAL_ECONOMICS = "deal_economics"
    OPERATOR_GROUND_TRUTH = "operator_ground_truth"


# Weights sum to 1.0. Tuned for OPAL/LYNA's reality: clinical fit
# matters most (no clinical pain ⇒ no pilot), integration second
# (an unsupported EPIC build is a hard stop), compliance third (BAA
# delays kill timelines), then economics + executive + ground-truth.
DIMENSION_WEIGHTS: dict[Dimension, float] = {
    Dimension.CLINICAL_FIT: 0.25,
    Dimension.INTEGRATION_FEASIBILITY: 0.20,
    Dimension.COMPLIANCE_BURDEN: 0.15,
    Dimension.EXECUTIVE_RESONANCE: 0.15,
    Dimension.DEAL_ECONOMICS: 0.15,
    Dimension.OPERATOR_GROUND_TRUTH: 0.10,
}


# ---------------------------------------------------------------------------
# Verdict + scores
# ---------------------------------------------------------------------------


class Verdict(str, Enum):
    """The bucket the weighted total falls into."""

    GO = "go"          # >= 75 — proceed to contract
    HOLD = "hold"      # 55-74 — fix the named gaps first
    NO_GO = "no_go"    # < 55 — site not worth pursuing now


VERDICT_THRESHOLDS = {
    Verdict.GO: 75.0,
    Verdict.HOLD: 55.0,
    # NO_GO is anything below HOLD
}


@dataclass(frozen=True)
class DimensionScore:
    """One dimension's score + explanation."""

    dimension: Dimension
    score: float                 # 0-100, the raw dimension score
    weighted: float              # score * weight; contributes to total
    rationale: tuple[str, ...]   # bullets explaining how we got the score
    gaps: tuple[str, ...]        # what's missing — actionable for the operator


@dataclass(frozen=True)
class SiteAssessment:
    """The output of score_site."""

    site_name: str
    total: float                 # weighted total, 0-100
    verdict: Verdict
    dimensions: tuple[DimensionScore, ...]
    summary: str                 # one-paragraph human-readable summary


# ---------------------------------------------------------------------------
# Site description — operator input
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ChampionCandidate:
    """A person at the site who might be the clinical champion."""

    name: str
    role: str
    # 0=floor staff, 1=manager, 2=director, 3=VP/C-suite. Higher = more
    # ability to greenlight + remove blockers.
    authority_level: int
    # 0-10: 0 = "no time, will dodge calls", 10 = "actively asking how
    # to help right now". Operator's honest read.
    bandwidth: int
    # 0-10: 0 = "doesn't see the problem we solve", 10 = "this is the
    # most important thing in their week".
    motivation: int
    # Free-text evidence the operator can point to (a quote, a meeting,
    # a Slack message, an LOI mention).
    evidence: tuple[str, ...] = ()


@dataclass(frozen=True)
class Site:
    """An operator's description of a candidate pilot hospital."""

    name: str

    # Clinical fit
    clinical_pain_addressed: bool       # do the clinicians at this site
                                          # actually feel the pain OPAL
                                          # addresses?
    week_one_plausible: bool              # can a clinician describe a
                                          # day-in-the-life with OPAL on
                                          # day 7?
    champion_candidates: tuple[ChampionCandidate, ...] = ()

    # Executive resonance
    cmo_aligned: bool = False             # has the CMO (or equivalent)
                                          # said the same thing as the
                                          # floor?
    c_suite_metric_mapped: bool = False   # is there a specific reported
                                          # metric this moves?

    # Integration feasibility (the hard-stop dimension)
    epic_version: str = ""                 # e.g. "May 2023"; empty if
                                          # unknown
    epic_supported: bool = False          # does our EPIC integration
                                          # support this build?
    fhir_endpoints_exposed: bool = False  # are the FHIR resources we
                                          # need actually live + reachable?
    device_provisioning_path: bool = False  # wifi, MDM, segmentation
                                          # answered?

    # Compliance burden
    baa_path_days: int | None = None       # known legal timeline; None
                                          # = unknown (treated as risky)
    irb_required: bool | None = None       # None = unknown
    security_review_path: bool = False    # do we know the queue + owner?

    # Deal economics
    pricing_fit: bool = False             # does our price band match
                                          # what this hospital actually
                                          # pays for similar tools?
    reference_design_value: bool = False  # would a discounted pilot
                                          # generate disproportionate
                                          # follow-on value?

    # Operator ground-truth
    site_bandwidth: bool = False          # does the site have someone
                                          # who will actually run the
                                          # pilot, vs. saying yes and
                                          # ghosting?
    decision_maker_accessible: bool = False  # can we reach the
                                          # signer in <2 weeks?

    # Free-form notes the rubric does NOT consume — kept so the
    # assessment + briefing can quote them.
    notes: tuple[str, ...] = field(default_factory=tuple)
