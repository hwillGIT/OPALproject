"""Parse persona-authored memory emit blocks out of LLM responses.

The persona is taught (via orchestrator/persona.py's _PREAMBLE) to
append a fenced YAML block whenever its reply contains a memory-worthy
moment:

    prose reply...

    ```memory-emit
    - type: DECISION
      title: short headline
      content: |
        optional body
      confidence: 0.8        # required for PREDICTION
      related: [evt-...]
      tags: [extra]
    ```

This module does three things:

  1. Extract every fenced ``memory-emit`` block from the response
  2. Parse + validate each emit against the schema
  3. Strip the blocks from the response so the operator-visible text
     is just the prose

Validation failures (bad YAML, unknown type, missing required field)
are returned as MalformedAttempt objects so the caller can record a
CONTEXT_CHANGE event preserving the persona's intent. The persona is
NEVER silently ignored.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

import yaml

from .loader import MEMORY_EVENT_TYPES


# A fenced block tagged ``memory-emit``. Captures the body. Tolerant
# of trailing whitespace, optional CRLFs, and either ``~~~`` or ``\`\`\``
# fences — though we only document the backtick form.
_FENCE_RE = re.compile(
    r"^(?P<fence>`{3,}|~{3,})[ \t]*memory-emit[ \t]*\r?\n"
    r"(?P<body>.*?)"
    r"^(?P=fence)[ \t]*$",
    re.DOTALL | re.MULTILINE,
)


@dataclass(frozen=True)
class ParsedEmit:
    """One validated emit ready to become a memory event."""

    type: str
    title: str
    content: str | None = None
    confidence: float | None = None
    related: tuple[str, ...] = field(default_factory=tuple)
    tags: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class MalformedAttempt:
    """A fenced block the persona tried to emit but we couldn't accept.

    Carries the raw text + a one-line reason. The runner records this
    as a CONTEXT_CHANGE so the operator can see what the persona
    intended.
    """

    raw: str
    reason: str


@dataclass(frozen=True)
class ParseResult:
    """The full output of parse_emits."""

    clean_text: str            # response with memory-emit blocks removed
    emits: tuple[ParsedEmit, ...]
    malformed: tuple[MalformedAttempt, ...]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def parse_emits(response_text: str) -> ParseResult:
    """Extract + validate every memory-emit fenced block in a response."""
    if not response_text:
        return ParseResult(clean_text=response_text or "", emits=(), malformed=())

    emits: list[ParsedEmit] = []
    malformed: list[MalformedAttempt] = []

    def _strip(match: re.Match) -> str:
        body = match.group("body")
        raw_block = match.group(0)
        for entry_emits, entry_malformed in _parse_one_block(body, raw_block):
            emits.extend(entry_emits)
            malformed.extend(entry_malformed)
        return ""  # remove the fenced block from the visible text

    clean = _FENCE_RE.sub(_strip, response_text)
    # Trim the trailing blank lines a stripped fence leaves behind
    clean = re.sub(r"\n{3,}", "\n\n", clean).rstrip() + "\n" if clean.strip() else ""

    return ParseResult(
        clean_text=clean,
        emits=tuple(emits),
        malformed=tuple(malformed),
    )


# ---------------------------------------------------------------------------
# Internals
# ---------------------------------------------------------------------------


def _parse_one_block(
    body: str,
    raw_block: str,
) -> list[tuple[list[ParsedEmit], list[MalformedAttempt]]]:
    """Parse one fenced block. Returns a single (emits, malformed) pair."""
    try:
        loaded = yaml.safe_load(body)
    except yaml.YAMLError as exc:
        return [([], [MalformedAttempt(raw=raw_block, reason=f"invalid YAML: {exc}")])]

    if loaded is None:
        # Empty block — silently allowed; persona did the right thing
        # by not emitting anything
        return [([], [])]

    if not isinstance(loaded, list):
        return [([], [MalformedAttempt(
            raw=raw_block,
            reason=f"top-level must be a YAML list of emit entries; got {type(loaded).__name__}",
        )])]

    emits: list[ParsedEmit] = []
    malformed: list[MalformedAttempt] = []
    for i, entry in enumerate(loaded):
        result = _validate_entry(entry, index=i)
        if isinstance(result, ParsedEmit):
            emits.append(result)
        else:
            # result is a reason string
            malformed.append(MalformedAttempt(
                raw=yaml.safe_dump(entry, sort_keys=False) if isinstance(entry, dict) else str(entry),
                reason=result,
            ))
    return [(emits, malformed)]


def _validate_entry(entry: Any, *, index: int) -> ParsedEmit | str:
    """Validate one parsed YAML entry. Returns ParsedEmit or a reason string."""
    if not isinstance(entry, dict):
        return f"entry #{index} must be a YAML mapping; got {type(entry).__name__}"

    etype = entry.get("type")
    if not etype:
        return f"entry #{index} missing required field 'type'"
    if etype not in MEMORY_EVENT_TYPES:
        return (
            f"entry #{index}: type {etype!r} not in vocabulary "
            f"({sorted(MEMORY_EVENT_TYPES)})"
        )

    title = entry.get("title")
    if not title or not isinstance(title, str):
        return f"entry #{index} ({etype}) missing required field 'title'"

    confidence = entry.get("confidence")
    if etype == "PREDICTION":
        if confidence is None:
            return f"entry #{index}: PREDICTION requires 'confidence' in [0,1]"
        try:
            confidence = float(confidence)
        except (TypeError, ValueError):
            return f"entry #{index}: PREDICTION confidence must be numeric; got {confidence!r}"
        if not (0.0 <= confidence <= 1.0):
            return f"entry #{index}: PREDICTION confidence {confidence} not in [0,1]"
    elif confidence is not None:
        try:
            confidence = float(confidence)
        except (TypeError, ValueError):
            return f"entry #{index}: confidence must be numeric; got {confidence!r}"
        if not (0.0 <= confidence <= 1.0):
            return f"entry #{index}: confidence {confidence} not in [0,1]"

    content = entry.get("content")
    if content is not None and not isinstance(content, str):
        return f"entry #{index}: content must be a string"

    related = entry.get("related")
    if related is None:
        related = []
    if not isinstance(related, list) or not all(isinstance(r, str) for r in related):
        return f"entry #{index}: related must be a list of event-id strings"

    tags = entry.get("tags")
    if tags is None:
        tags = []
    if not isinstance(tags, list) or not all(isinstance(t, str) for t in tags):
        return f"entry #{index}: tags must be a list of strings"

    return ParsedEmit(
        type=str(etype),
        title=str(title).strip(),
        content=str(content) if content is not None else None,
        confidence=confidence,
        related=tuple(related),
        tags=tuple(tags),
    )
