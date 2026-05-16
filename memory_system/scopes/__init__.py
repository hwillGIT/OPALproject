"""Scope/namespace primitive — living-vocabulary layer.

Adapted from the RTRevenue collab-memory ADR-001 pattern for OPAL's
memory_system. A Scope is a named cluster of related provisional tags
that the system has recognized as belonging together — it bridges the
free-form tag layer (any tag attached at write-time) and the curated
canonical ontology (in `memory_system/ontology/`).

Why we want it for OPAL: a clinical-pilot kickoff meeting introduces
a project codename ("Project Aurora") + 5-10 internal terms
(`unit-3a-icu`, `bedside-aurora-pilot`, ...). The writer should not
have to pre-declare each term before capturing the meeting.

Pipeline (left -> right):

    events tagged at write-time
              |
              v
       scopes.detect (burst detector)
              |
              v
       scopes.materialize -> (Scope, ScopeMember[], ScopeTransition)
              |
              v
       scopes.store (SQLite)
              |
              v
       scopes.lifecycle (provisional -> active -> canonical -> deprecated)

All modules in this package are pure-functional where possible.
Storage is the only I/O.
"""

from .adversarial import (
    AdversarialReviewer,
    ReviewRequest,
    ReviewVerdict,
    StubReviewer,
    Verdict,
    build_review_prompt,
    parse_review_response,
)
from .identifiers import (
    make_rollback_id,
    make_scope_id,
    make_transition_id,
    slugify,
)
from .lifecycle_gating import (
    GatingResult,
    annotate_transition_with_verdict,
    gate_tier_2,
)
from .models import (
    Scope,
    ScopeMember,
    ScopeStatus,
    ScopeTransition,
    TransitionActor,
)
from .transitions import (
    ALLOWED_TRANSITIONS,
    Tier,
    can_transition,
    tier_of,
)

__all__ = [
    "ALLOWED_TRANSITIONS",
    "AdversarialReviewer",
    "GatingResult",
    "ReviewRequest",
    "ReviewVerdict",
    "Scope",
    "ScopeMember",
    "ScopeStatus",
    "ScopeTransition",
    "StubReviewer",
    "Tier",
    "TransitionActor",
    "Verdict",
    "annotate_transition_with_verdict",
    "build_review_prompt",
    "can_transition",
    "gate_tier_2",
    "make_rollback_id",
    "make_scope_id",
    "make_transition_id",
    "parse_review_response",
    "slugify",
    "tier_of",
]
