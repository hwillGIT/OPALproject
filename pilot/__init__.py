"""Pilot-site scoring + champion identification (D-1).

A deterministic, transparent rubric for evaluating candidate pilot
hospitals against the criteria the pilot-site-assessment workflow
already cares about (bots/shared/workflows/business/pilot-site-
assessment.yaml). The rubric is the operator's fast-triage tool; the
workflow is the deep-dive review. They share the same vocabulary.

End-to-end:

    site YAML  ──►  load_site  ──►  Site
                                      │
                                      ▼
                                 score_site  ──►  SiteAssessment
                                      │           (per-dimension scores,
                                      │            weighted total,
                                      │            verdict, gaps)
                                      ▼
                              champion_rank  ──►  list[ChampionRanking]
                              (or just: highest-scoring champion)
"""
from .champion import (
    ChampionCandidate,
    ChampionRanking,
    rank_champions,
    score_champion,
)
from .loader import SiteLoadError, load_site
from .models import (
    DIMENSION_WEIGHTS,
    Dimension,
    DimensionScore,
    Site,
    SiteAssessment,
    Verdict,
)
from .scoring import score_site

__all__ = [
    "ChampionCandidate",
    "ChampionRanking",
    "Dimension",
    "DimensionScore",
    "DIMENSION_WEIGHTS",
    "Site",
    "SiteAssessment",
    "SiteLoadError",
    "Verdict",
    "load_site",
    "rank_champions",
    "score_champion",
    "score_site",
]
