"""Unit tests for the Contextual Router stub.

Uses a faked ``IntelligenceAnswerService`` so we don't hit ChromaDB
or any LLM provider during routing tests.
"""
from __future__ import annotations

from dataclasses import dataclass

import pytest

from epic_intelligence.assistant.voice_router_stub import (
    ContextualRouter,
    RouteDecision,
)
from epic_intelligence.synthesis import Answer, Citation


@dataclass
class FakeService:
    """Stand-in for IntelligenceAnswerService used in router tests."""

    name: str = "fake"
    model: str = "fake-1"
    last_question: str = ""

    @property
    def provider_name(self) -> str:
        return self.name

    @property
    def model_name(self) -> str:
        return self.model

    def answer(self, question: str, **kwargs) -> Answer:
        self.last_question = question
        return Answer(
            text=f"fake answer to {question!r} [1]",
            citations=(Citation(
                chunk_id="c1", title="t", source_url="https://x",
                section_path=("A",), snippet="s", score=0.5,
            ),),
            insufficient=False,
            provider_name=self.name,
            model_name=self.model,
        )


class TestRouting:
    def test_empty_question_out_of_domain(self) -> None:
        router = ContextualRouter(epic_service=FakeService())
        d = router.route("")
        assert d.target == "out_of_domain"
        assert d.answer is None

    def test_oncall_keyword_routes_to_on_call(self) -> None:
        router = ContextualRouter(epic_service=FakeService())
        d = router.route("Who is on call for cardiology tonight?")
        assert d.target == "on_call_schedule"
        assert d.answer is None

    def test_bedside_keyword_routes_to_workflow(self) -> None:
        router = ContextualRouter(epic_service=FakeService())
        d = router.route("Show me this patient's last vitals")
        assert d.target == "clinician_workflow"
        assert d.answer is None

    def test_epic_keyword_routes_to_epic_and_answers(self) -> None:
        svc = FakeService()
        router = ContextualRouter(epic_service=svc)
        d = router.route("What scope do I need for SMART on FHIR access?")
        assert d.target == "epic_intelligence"
        assert d.answer is not None
        assert "fake answer" in d.answer.text
        assert svc.last_question.startswith("What scope")
        # Metadata records the matched provider info
        assert d.metadata["provider"] == "fake"
        assert d.metadata["model"] == "fake-1"

    def test_unrelated_question_out_of_domain(self) -> None:
        router = ContextualRouter(epic_service=FakeService())
        d = router.route("What's the weather like?")
        assert d.target == "out_of_domain"
        assert d.answer is None

    def test_oncall_takes_precedence_over_epic(self) -> None:
        # If both 'on call' and 'epic' appear, on-call wins (it's more
        # operationally urgent + the router checks oncall first).
        router = ContextualRouter(epic_service=FakeService())
        d = router.route("Who is on call for the Epic integration team?")
        assert d.target == "on_call_schedule"

    def test_workflow_takes_precedence_over_epic(self) -> None:
        router = ContextualRouter(epic_service=FakeService())
        d = router.route(
            "For this patient, what FHIR resources are accessible?",
        )
        assert d.target == "clinician_workflow"


class TestRouteDecision:
    def test_decision_carries_matched_keywords(self) -> None:
        router = ContextualRouter(epic_service=FakeService())
        d = router.route("Tell me about CDS hooks and patient/Observation.read")
        assert d.target == "epic_intelligence"
        matched = d.metadata.get("matched_keywords") or []
        assert "cds hooks" in matched
        assert any("patient/" in m or "observation" in m for m in matched)
