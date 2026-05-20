"""Scope status state machine: allowed transitions + tier classification.

Pure data + pure predicates. No I/O. No side effects.

Tiered authority (from RTRevenue ADR-001, preserved):

  Tier 0   write-time tag application + scope creation
                                                     -> autonomous, no review
  Tier 1   provisional -> active                     -> autonomous, 7d rollback
  Tier 2   active -> canonical, * -> deprecated      -> autonomous + adversarial
                                                        review (gated externally)
  Tier 3   canonical -> active, active -> provisional -> operator-only
"""
from __future__ import annotations

from typing import Literal

from .models import ScopeStatus

Tier = Literal[0, 1, 2, 3]


# (from_status, to_status) -> tier. from_status=None means scope creation.
ALLOWED_TRANSITIONS: dict[tuple[ScopeStatus | None, ScopeStatus], Tier] = {
    # Creation
    (None, "provisional"): 0,

    # Tier 1 — autonomous + rollback window
    ("provisional", "active"): 1,

    # Tier 2 — autonomous + adversarial review
    ("active", "canonical"): 2,
    ("provisional", "deprecated"): 2,
    ("active", "deprecated"): 2,
    ("canonical", "deprecated"): 2,
    ("deprecated", "active"): 2,

    # Tier 3 — operator-only demotions (gated by actor at commit layer)
    ("canonical", "active"): 3,
    ("active", "provisional"): 3,
}


def can_transition(
    from_status: ScopeStatus | None,
    to_status: ScopeStatus,
) -> bool:
    """True iff the transition is in the allowed table."""
    return (from_status, to_status) in ALLOWED_TRANSITIONS


def tier_of(
    from_status: ScopeStatus | None,
    to_status: ScopeStatus,
) -> Tier:
    """Return the tier of a transition. Raises ValueError if disallowed."""
    try:
        return ALLOWED_TRANSITIONS[(from_status, to_status)]
    except KeyError as exc:
        raise ValueError(
            f"transition {from_status!r} -> {to_status!r} is not allowed",
        ) from exc
