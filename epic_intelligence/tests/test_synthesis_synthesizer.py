"""Unit tests for the synthesizer + provider factory + extraction logic."""
from __future__ import annotations

import os
from dataclasses import dataclass

import pytest

from epic_intelligence.index.store import QueryHit
from epic_intelligence.synthesis import (
    Answer,
    Citation,
    StubProvider,
    SynthesisRequest,
    get_provider,
    synthesize,
)
from epic_intelligence.synthesis.synthesizer import (
    _extract_referenced_indices,
    _is_insufficient,
    citation_from_hit,
    hits_to_citations,
)


def _cite(idx: int) -> Citation:
    return Citation(
        chunk_id=f"chunk-{idx}",
        title=f"Title {idx}",
        source_url=f"https://example/{idx}",
        section_path=("Sec", f"sub{idx}"),
        snippet=f"snippet {idx}",
        score=0.5,
    )


# --------------------------------------------------------------------------
# citation_from_hit / hits_to_citations
# --------------------------------------------------------------------------


def test_citation_from_hit_preserves_fields() -> None:
    hit = QueryHit(
        chunk_id="c1", score=0.5, title="t",
        source_url="https://x", section_path=("A", "B"),
        snippet="s", metadata={},
    )
    c = citation_from_hit(hit)
    assert c.chunk_id == "c1"
    assert c.source_url == "https://x"
    assert c.section_path == ("A", "B")


def test_hits_to_citations_preserves_order() -> None:
    hits = [
        QueryHit(chunk_id=f"c{i}", score=float(i), title="t",
                  source_url="u", section_path=(), snippet="s", metadata={})
        for i in range(3)
    ]
    cs = hits_to_citations(hits)
    assert [c.chunk_id for c in cs] == ["c0", "c1", "c2"]


# --------------------------------------------------------------------------
# pure helpers
# --------------------------------------------------------------------------


class TestExtractReferenced:
    def test_single_ref(self) -> None:
        assert _extract_referenced_indices("see [1] for details") == {1}

    def test_multiple_refs(self) -> None:
        assert _extract_referenced_indices(
            "A [1] B [2][3] C [1] D",
        ) == {1, 2, 3}

    def test_no_refs(self) -> None:
        assert _extract_referenced_indices("plain text") == set()


class TestIsInsufficient:
    def test_detects_insufficient_phrase(self) -> None:
        assert _is_insufficient("(insufficient sources) cannot answer")

    def test_detects_cannot_answer(self) -> None:
        assert _is_insufficient("I cannot answer based on the sources.")

    def test_negative_case(self) -> None:
        assert not _is_insufficient(
            "Per [1] and [2], the launch token includes patient context.",
        )


# --------------------------------------------------------------------------
# StubProvider + synthesize end-to-end
# --------------------------------------------------------------------------


class TestStubProvider:
    def test_cites_every_provided_source(self) -> None:
        p = StubProvider()
        text = p.complete(
            system_prompt="sys",
            user_prompt=(
                "QUESTION:\nq\n\nSOURCES (cite as [1], [2], ...):\n"
                "[1] x\n[2] y\n[3] z\n"
            ),
            max_tokens=100,
            temperature=0.0,
        )
        for i in (1, 2, 3):
            assert f"[{i}]" in text

    def test_empty_sources_flagged_insufficient(self) -> None:
        p = StubProvider()
        text = p.complete(
            system_prompt="sys",
            user_prompt="QUESTION:\nq\n\nSOURCES (cite as [1], [2], ...):\n",
            max_tokens=100,
            temperature=0.0,
        )
        assert "insufficient" in text.lower()


class TestSynthesizeEndToEnd:
    def test_happy_path(self) -> None:
        req = SynthesisRequest(
            question="What is foo?",
            citations=(_cite(1), _cite(2), _cite(3)),
        )
        ans = synthesize(req)
        assert isinstance(ans, Answer)
        assert ans.provider_name == "stub"
        assert ans.insufficient is False
        # Stub cites all three; synthesizer should narrow to referenced ones.
        assert {c.chunk_id for c in ans.citations} == {
            "chunk-1", "chunk-2", "chunk-3",
        }

    def test_no_sources_marks_insufficient(self) -> None:
        req = SynthesisRequest(question="q", citations=())
        ans = synthesize(req)
        assert ans.insufficient is True
        assert ans.citations == ()

    def test_unreferenced_citations_are_dropped(self) -> None:
        # A custom provider that ignores sources 2 and 3.
        @dataclass
        class OnlyCiteOne:
            name: str = "test"
            model: str = "test-1"

            def complete(self, system_prompt, user_prompt, max_tokens, temperature):
                return "Per [1] only, the answer is foo."

        req = SynthesisRequest(
            question="q", citations=(_cite(1), _cite(2), _cite(3)),
        )
        ans = synthesize(req, provider=OnlyCiteOne())
        assert [c.chunk_id for c in ans.citations] == ["chunk-1"]
        assert ans.metadata["candidate_count"] == 3
        assert ans.metadata["referenced_indices"] == [1]


# --------------------------------------------------------------------------
# Provider factory
# --------------------------------------------------------------------------


class TestProviderFactory:
    def test_stub_always_available(self) -> None:
        p = get_provider("stub")
        assert p.name == "stub"

    def test_auto_falls_back_to_stub_when_no_keys(
        self, monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        for k in ("ANTHROPIC_API_KEY", "OPENAI_API_KEY", "GOOGLE_API_KEY",
                  "OPAL_SYNTHESIS_PROVIDER"):
            monkeypatch.delenv(k, raising=False)
        p = get_provider("auto")
        assert p.name == "stub"

    def test_env_override(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("OPAL_SYNTHESIS_PROVIDER", "stub")
        p = get_provider("auto")
        assert p.name == "stub"

    def test_unknown_provider_raises(self) -> None:
        with pytest.raises(ValueError, match="unknown synthesis provider"):
            get_provider("nonsense")
