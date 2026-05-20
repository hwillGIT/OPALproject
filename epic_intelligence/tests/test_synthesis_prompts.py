"""Unit tests for the synthesis prompt builder."""
from __future__ import annotations

from epic_intelligence.synthesis import (
    Citation,
    SynthesisRequest,
    build_synthesis_prompt,
)
from epic_intelligence.synthesis.prompts import SYSTEM_PROMPT


def _cite(idx: int) -> Citation:
    return Citation(
        chunk_id=f"chunk-{idx}",
        title=f"Title {idx}",
        source_url=f"https://example/{idx}",
        section_path=("A", "B"),
        snippet=f"snippet {idx}",
        score=0.5,
    )


def test_system_prompt_carries_hard_rules() -> None:
    # Smoke-check the three constraints the synthesizer relies on.
    assert "[1]" in SYSTEM_PROMPT
    assert "insufficient" in SYSTEM_PROMPT.lower()
    assert "do not guess" in SYSTEM_PROMPT.lower() or "do not invent" in SYSTEM_PROMPT.lower()


def test_user_prompt_includes_question() -> None:
    req = SynthesisRequest(question="What is foo?", citations=())
    _, user = build_synthesis_prompt(req)
    assert "What is foo?" in user


def test_user_prompt_includes_each_source_with_index() -> None:
    cites = tuple(_cite(i) for i in (1, 2, 3))
    req = SynthesisRequest(question="q", citations=cites)
    _, user = build_synthesis_prompt(req)
    for i in (1, 2, 3):
        assert f"[{i}]" in user
        assert f"chunk-{i}" in user
        assert f"https://example/{i}" in user
        assert f"snippet {i}" in user


def test_empty_sources_block_when_no_citations() -> None:
    req = SynthesisRequest(question="q", citations=())
    _, user = build_synthesis_prompt(req)
    assert "no sources provided" in user


def test_additional_instructions_propagate() -> None:
    req = SynthesisRequest(
        question="q", citations=(),
        instructions="speak in haiku form",
    )
    _, user = build_synthesis_prompt(req)
    assert "haiku" in user
    assert "ADDITIONAL INSTRUCTIONS" in user
