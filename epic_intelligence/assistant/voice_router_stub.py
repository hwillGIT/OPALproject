"""Contextual Router stub — the contract the voice assistant will fulfill.

This is intentionally a **stub**: the real Contextual Router lives in
the OPAL wearable's firmware-adjacent stack (out of scope for this
repo). The stub here serves three purposes:

  1. It documents the routing decision the real router must make:
     "Is this question best answered from EPIC docs, from clinician
     workflow context, from the on-call schedule, or by escalating?"

  2. It provides a runnable Python reference implementation so the
     EPIC route can be exercised end-to-end during development
     without needing the real device.

  3. It defines the `RouteDecision` shape the device + cloud
     orchestrator agree on, so multiple downstream consumers
     (HUD render, TTS, telemetry) can be written against one
     contract.

Per Phase 3 Epic 4 in `hardware/opalDevice/docs/architecture/
opal-system-architecture-epics.md`:

  > Contextual Router uses multi-factor analysis with Hospital
  > Intelligence Module (RAG) to determine optimal recipient.

This file is the "Hospital Intelligence Module (RAG)" entry point.
The "multi-factor analysis" stays on-device; only the dispatch into
this service crosses the network.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from ..synthesis.models import Answer
from .service import IntelligenceAnswerService

RouteTarget = Literal[
    "epic_intelligence",  # the EPIC RAG layer — implemented here
    "clinician_workflow",  # bedside-context lookup — out of scope
    "on_call_schedule",    # paging/coverage lookup — out of scope
    "escalate_to_human",   # punt to a human on-call — out of scope
    "out_of_domain",       # not a question this assistant should answer
]


@dataclass(frozen=True)
class RouteDecision:
    """The output of a single routing decision.

    The real router will produce one of these per transcribed
    utterance; the stub below produces one based on simple keyword
    routing for demonstration.
    """

    target: RouteTarget
    confidence: float        # 0.0 .. 1.0
    reason: str              # human-readable, also surfaced in telemetry
    answer: Answer | None = None  # populated if target == 'epic_intelligence'
    metadata: dict = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Stub keyword router
# ---------------------------------------------------------------------------


# Keyword sets are deliberately narrow + auditable. The real router
# uses a more sophisticated multi-factor classifier; this stub serves
# the "Is the EPIC route reachable?" smoke test.
_EPIC_KEYWORDS = (
    "fhir", "epic", "smart on fhir", "oauth", "scope",
    "patient/", "user/", "system/", "observation", "medication",
    "cds hooks", "order-sign", "patient-view", "smart app launch",
    "uscdi", "app orchard", "backend services",
)

_WORKFLOW_KEYWORDS = (
    "this patient", "in this room", "current patient",
    "bedside", "right now", "this encounter",
)

_ONCALL_KEYWORDS = (
    "on call", "on-call", "page", "paging", "covering",
    "who is", "who's covering",
)


class ContextualRouter:
    """Stub keyword router with one real downstream: the EPIC service.

    Construct once; reuse. The EPIC service is lazy — it isn't
    instantiated until the first question that routes there, so
    bringing up the router doesn't open ChromaDB or call any LLM
    provider until needed.
    """

    def __init__(
        self,
        epic_service: IntelligenceAnswerService | None = None,
    ) -> None:
        self._explicit_service = epic_service
        self._service: IntelligenceAnswerService | None = epic_service

    def _epic(self) -> IntelligenceAnswerService:
        if self._service is None:
            self._service = IntelligenceAnswerService()
        return self._service

    def route(self, question: str) -> RouteDecision:
        """Classify + (if EPIC) execute. Pure decision logic + one
        side effect: the LLM call when the route is `epic_intelligence`."""
        q = (question or "").strip()
        if not q:
            return RouteDecision(
                target="out_of_domain", confidence=1.0,
                reason="empty question",
            )

        lowered = q.lower()
        if any(kw in lowered for kw in _ONCALL_KEYWORDS):
            return RouteDecision(
                target="on_call_schedule", confidence=0.8,
                reason="matched on-call keyword",
                metadata={"matched_keywords": [
                    kw for kw in _ONCALL_KEYWORDS if kw in lowered
                ]},
            )
        if any(kw in lowered for kw in _WORKFLOW_KEYWORDS):
            return RouteDecision(
                target="clinician_workflow", confidence=0.75,
                reason="matched bedside-context keyword",
                metadata={"matched_keywords": [
                    kw for kw in _WORKFLOW_KEYWORDS if kw in lowered
                ]},
            )
        if any(kw in lowered for kw in _EPIC_KEYWORDS):
            ans = self._epic().answer(q)
            return RouteDecision(
                target="epic_intelligence",
                confidence=0.9,
                reason="matched EPIC/FHIR/SMART keyword",
                answer=ans,
                metadata={
                    "matched_keywords": [
                        kw for kw in _EPIC_KEYWORDS if kw in lowered
                    ],
                    "provider": ans.provider_name,
                    "model": ans.model_name,
                },
            )
        return RouteDecision(
            target="out_of_domain", confidence=0.6,
            reason="no routing keywords matched",
        )
