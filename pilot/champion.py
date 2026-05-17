"""Champion identification framework.

A "clinical champion" is the named person at a pilot site who carries
the project through internal friction. The pilot-site-assessment
workflow's backpressure gate names them as the precondition for any
signed pilot: "Named clinical champion identified at the site (not
'the IT team')".

This module turns an operator's notes about candidate champions into a
deterministic 0-100 score per person, with the reasoning surfaced.
The dimensions reflect what actually predicts champion success:

  - authority_level  (35%): can they greenlight + remove blockers?
  - motivation       (40%): do they care about THIS problem?
  - bandwidth        (15%): can they spend time on this?
  - evidence         (10%): is there a real trace, not aspiration?

Motivation outweighs authority because a high-authority bored
executive ghosts; a passionate floor manager unblocks weekly.
"""
from __future__ import annotations

from dataclasses import dataclass

from .models import ChampionCandidate


@dataclass(frozen=True)
class ChampionRanking:
    """A scored + explained champion candidate."""

    candidate: ChampionCandidate
    score: float                 # 0-100
    rationale: tuple[str, ...]   # bullets explaining the score
    risks: tuple[str, ...]       # what could derail this champion


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------


def score_champion(candidate: ChampionCandidate) -> ChampionRanking:
    """Score a champion candidate; return a ChampionRanking."""
    rationale: list[str] = []
    risks: list[str] = []
    score = 0.0

    # Authority — 35 points. Floor staff can be amazing champions but
    # they need to escalate to greenlight things; directors+ can act.
    auth_pts = {
        0: (5, "Floor-level — can advocate but cannot greenlight or remove most blockers."),
        1: (18, "Manager-level — can clear local blockers, escalates strategic asks."),
        2: (28, "Director-level — can greenlight pilots within their function."),
        3: (35, "VP/C-suite — can greenlight + remove cross-functional blockers."),
    }
    auth_score, auth_reason = auth_pts.get(
        max(0, min(3, candidate.authority_level)),
        (5, "Authority level unrecognized; defaulting low."),
    )
    score += auth_score
    rationale.append(auth_reason)
    if candidate.authority_level <= 1 and not candidate.evidence:
        risks.append("Low-authority champion with no evidence trail; bring an escalation path.")

    # Motivation — 40 points (highest weight). Capped to [0,10].
    mot = max(0, min(10, candidate.motivation))
    mot_pts = round(4.0 * mot, 1)
    score += mot_pts
    rationale.append(f"Motivation {mot}/10 -> {mot_pts:.0f}/40 points.")
    if mot <= 4:
        risks.append(
            "Low motivation — champion likely to deprioritize this when their "
            "week gets busy."
        )

    # Bandwidth — 15 points. Capped to [0,10].
    bw = max(0, min(10, candidate.bandwidth))
    bw_pts = round(1.5 * bw, 1)
    score += bw_pts
    rationale.append(f"Bandwidth {bw}/10 -> {bw_pts:.0f}/15 points.")
    if bw <= 3:
        risks.append("Low bandwidth — meetings will slip; build async checkpoints.")

    # Evidence — 10 points. We score the FIRST 2 pieces of evidence
    # (5 each) to discourage stuffing the list with weak items.
    n_ev = min(2, len(candidate.evidence))
    ev_pts = n_ev * 5
    score += ev_pts
    if n_ev > 0:
        rationale.append(
            f"{n_ev} concrete piece(s) of evidence cited "
            f"({ev_pts}/10 points)."
        )
    else:
        rationale.append("No concrete evidence cited (0/10 points).")
        risks.append("No evidence the champion has actually committed time/voice; aspirational.")

    final_score = round(max(0.0, min(100.0, score)), 1)
    return ChampionRanking(
        candidate=candidate,
        score=final_score,
        rationale=tuple(rationale),
        risks=tuple(risks),
    )


def rank_champions(
    candidates: list[ChampionCandidate] | tuple[ChampionCandidate, ...],
) -> list[ChampionRanking]:
    """Score every candidate and return them sorted highest-first."""
    scored = [score_champion(c) for c in candidates]
    return sorted(scored, key=lambda r: r.score, reverse=True)
