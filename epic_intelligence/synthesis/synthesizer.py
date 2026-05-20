"""End-to-end synthesis: request -> prompt -> LLM -> Answer.

Pure orchestration. The provider and the prompt builder are
swappable; this module wires them together and post-processes the
LLM output into a clean Answer with verified citations.
"""
from __future__ import annotations

import re
from typing import Sequence

from ..index.store import QueryHit
from .models import Answer, Citation, SynthesisRequest
from .prompts import build_synthesis_prompt
from .provider import LlmProvider, StubProvider


def citation_from_hit(hit: QueryHit) -> Citation:
    """Adapter: turn a retrieval QueryHit into a synthesis Citation."""
    return Citation(
        chunk_id=hit.chunk_id,
        title=hit.title,
        source_url=hit.source_url,
        section_path=hit.section_path,
        snippet=hit.snippet,
        score=hit.score,
    )


def hits_to_citations(hits: Sequence[QueryHit]) -> tuple[Citation, ...]:
    return tuple(citation_from_hit(h) for h in hits)


def _extract_referenced_indices(text: str) -> set[int]:
    """Return the 1-indexed citation numbers actually referenced in `text`."""
    return {int(m) for m in re.findall(r"\[(\d+)\]", text)}


def _is_insufficient(text: str) -> bool:
    """Detect refusal-to-guess responses the prompt encourages.

    Looks for the explicit phrases the system prompt steers the LLM
    towards ("insufficient", "cannot answer", "no sources").
    """
    lowered = text.lower()
    needles = (
        "insufficient sources",
        "insufficient evidence",
        "cannot answer",
        "no sources",
        "do not have enough",
        "not enough information",
    )
    return any(n in lowered for n in needles)


def synthesize(
    request: SynthesisRequest,
    provider: LlmProvider | None = None,
) -> Answer:
    """Run the synthesis end-to-end.

    Returns an `Answer` whose `citations` field is restricted to the
    citations the LLM actually referenced in its text. Unreferenced
    citations are dropped — they're noise from the retriever's
    perspective even if they were in the candidate set. (If you want
    them anyway for debugging, look at the `metadata['all_candidates']`
    field.)
    """
    provider = provider or StubProvider()
    system_prompt, user_prompt = build_synthesis_prompt(request)
    text = provider.complete(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        max_tokens=request.max_tokens_out,
        temperature=request.temperature,
    )

    insufficient = _is_insufficient(text)

    referenced = _extract_referenced_indices(text)
    used_citations: tuple[Citation, ...] = tuple(
        c for i, c in enumerate(request.citations, start=1)
        if i in referenced
    ) if not insufficient else ()

    return Answer(
        text=text,
        citations=used_citations,
        insufficient=insufficient,
        provider_name=provider.name,
        model_name=getattr(provider, "model", "unknown"),
        metadata={
            "all_candidates": [c.chunk_id for c in request.citations],
            "candidate_count": len(request.citations),
            "referenced_indices": sorted(referenced),
        },
    )
