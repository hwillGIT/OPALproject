"""Prompt construction for the synthesis layer.

Pure functions over `SynthesisRequest`. No I/O, no LLM calls.

The prompt is deliberately strict on three things:
  1. Cite by bracketed numeral (``[1]``, ``[2]``) — the UI relies on it
  2. If retrieval is thin, refuse to guess + name what's missing
  3. Stay grounded in the provided chunks; do NOT bring outside Epic
     knowledge into the answer

These three constraints are what makes the synthesizer safe enough
for a clinician-facing voice surface.
"""
from __future__ import annotations

from .models import Citation, SynthesisRequest


SYSTEM_PROMPT = """\
You are the OPAL Epic EHR Intelligence assistant. You answer
clinician + developer questions about Epic Systems' developer-facing
APIs (FHIR, SMART on FHIR, CDS Hooks, App Orchard) by synthesizing
ONLY from the cited source chunks the caller provides.

Hard rules:

1. EVERY factual claim in your answer MUST be supported by at least
   one citation. Citations use 1-indexed bracketed numerals: [1],
   [2], ... that map to the SOURCES section the caller provides.

2. If the SOURCES section is empty, irrelevant to the question, or
   insufficient to answer with confidence, say so explicitly. Name
   what would have been needed. Do NOT guess. Do NOT pad with
   general Epic / FHIR knowledge from your training data.

3. Stay tight. A clinician will hear this read aloud OR scan it on a
   small wearable HUD. Lead with the answer, then the supporting
   detail. Skip preamble.

4. When the question is ambiguous, answer the most likely
   interpretation AND name the ambiguity in one line.

5. Never invent URLs, claim numbers, scope names, or resource
   fields that aren't in the SOURCES. Made-up specificity is worse
   than acknowledging uncertainty.
"""


def _format_citation(idx: int, c: Citation) -> str:
    section = " > ".join(c.section_path) if c.section_path else "(top)"
    url = c.source_url or "(no source url)"
    return (
        f"[{idx}] {c.title}\n"
        f"    section: {section}\n"
        f"    source : {url}\n"
        f"    chunk  : {c.chunk_id}\n"
        f"    ---\n"
        f"    {c.snippet.strip()}\n"
    )


def build_synthesis_prompt(req: SynthesisRequest) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for the LLM call.

    The pair-return is provider-agnostic — providers convert it to
    their own message format (e.g. Anthropic's `messages=[{...}]`,
    OpenAI's `messages=[{...}]`, Gemini's `contents=[...]`).
    """
    sources_block = "\n".join(
        _format_citation(i + 1, c) for i, c in enumerate(req.citations)
    ) if req.citations else "(no sources provided)"

    extra = f"\n\nADDITIONAL INSTRUCTIONS:\n{req.instructions}" if req.instructions else ""

    user_prompt = (
        f"QUESTION:\n{req.question}\n\n"
        f"SOURCES (cite as [1], [2], ...):\n{sources_block}\n"
        f"{extra}\n\n"
        "Answer the QUESTION using ONLY the SOURCES. If the SOURCES are "
        "insufficient or off-topic, say so explicitly and name what "
        "would have been needed."
    )

    return SYSTEM_PROMPT, user_prompt
