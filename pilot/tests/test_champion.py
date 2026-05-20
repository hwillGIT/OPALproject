"""Unit tests for champion scoring.

The scoring is deterministic — same input always produces the same
ranking — so the tests assert on absolute numbers + ordering. If
weights change, these tests will need to follow.
"""
from __future__ import annotations

import pytest

from pilot.champion import rank_champions, score_champion
from pilot.models import ChampionCandidate


def _candidate(**kw) -> ChampionCandidate:
    base = dict(
        name="X",
        role="Role",
        authority_level=0,
        bandwidth=0,
        motivation=0,
        evidence=(),
    )
    base.update(kw)
    return ChampionCandidate(**base)


class TestScoreChampion:
    def test_perfect_champion_scores_at_top(self) -> None:
        c = _candidate(
            authority_level=3,
            bandwidth=10,
            motivation=10,
            evidence=("a", "b", "c"),
        )
        r = score_champion(c)
        # 35 (auth) + 40 (motivation) + 15 (bandwidth) + 10 (evidence; capped at 2 entries) = 100
        assert r.score == 100.0
        assert r.risks == ()

    def test_zero_everything_floors_near_zero(self) -> None:
        c = _candidate(
            authority_level=0, bandwidth=0, motivation=0, evidence=(),
        )
        r = score_champion(c)
        # 5 (floor auth points) + 0 + 0 + 0 = 5
        assert r.score == 5.0
        # Risks should fire for low motivation + no evidence + low-auth-no-evidence
        assert any("Low motivation" in risk for risk in r.risks)
        assert any("No evidence" in risk for risk in r.risks)
        assert any("Low-authority" in risk for risk in r.risks)

    def test_motivation_weighted_higher_than_authority(self) -> None:
        # High authority, low motivation
        a = _candidate(authority_level=3, motivation=2, bandwidth=5, evidence=("x",))
        # Low authority, high motivation
        b = _candidate(authority_level=0, motivation=10, bandwidth=5, evidence=("x",))
        ra = score_champion(a)
        rb = score_champion(b)
        assert rb.score > ra.score, (
            f"motivation-10 candidate ({rb.score}) should beat authority-3 "
            f"candidate ({ra.score}) — motivation is weighted higher"
        )

    def test_evidence_capped_at_two_entries(self) -> None:
        c = _candidate(authority_level=2, motivation=8, bandwidth=5, evidence=("e1", "e2"))
        d = _candidate(authority_level=2, motivation=8, bandwidth=5, evidence=("e1", "e2", "e3", "e4"))
        rc = score_champion(c)
        rd = score_champion(d)
        assert rc.score == rd.score, "evidence beyond the first two should not increase the score"

    def test_authority_out_of_range_is_clamped(self) -> None:
        c_low = _candidate(authority_level=-5, motivation=5)
        c_high = _candidate(authority_level=99, motivation=5)
        r_low = score_champion(c_low)
        r_high = score_champion(c_high)
        # Low clamps to 0 (5 pts); high clamps to 3 (35 pts) — so high > low
        assert r_high.score > r_low.score

    def test_low_authority_with_evidence_doesnt_trigger_no_evidence_risk(self) -> None:
        c = _candidate(
            authority_level=1, bandwidth=5, motivation=8,
            evidence=("attended panel", "scheduled discovery interview"),
        )
        r = score_champion(c)
        # The "Low-authority + no evidence" risk requires BOTH conditions.
        # With evidence present it should not fire.
        assert not any("Low-authority" in risk for risk in r.risks)


class TestRankChampions:
    def test_empty_input(self) -> None:
        assert rank_champions([]) == []

    def test_returns_sorted_highest_first(self) -> None:
        weak = _candidate(name="weak", motivation=2, bandwidth=2, authority_level=1)
        strong = _candidate(name="strong", motivation=10, bandwidth=10, authority_level=3,
                            evidence=("ev1", "ev2"))
        mid = _candidate(name="mid", motivation=5, bandwidth=5, authority_level=2,
                         evidence=("ev1",))
        ranked = rank_champions([weak, strong, mid])
        assert [r.candidate.name for r in ranked] == ["strong", "mid", "weak"]
        assert ranked[0].score > ranked[1].score > ranked[2].score
