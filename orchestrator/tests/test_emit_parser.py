"""Unit tests for the persona emit-block parser.

The parser is the contract surface between persona-authored reply
text and the typed-memory layer. Cover the happy path, every shape
of malformed input, the strip behavior (operator-visible text must
have no emit block), and the type-vocabulary check.
"""
from __future__ import annotations

import pytest

from orchestrator.emit_parser import (
    MalformedAttempt,
    ParsedEmit,
    parse_emits,
)


# --------------------------------------------------------------------------
# Happy path
# --------------------------------------------------------------------------


class TestHappyPath:
    def test_single_decision_emit(self) -> None:
        text = """\
Here is my call.

```memory-emit
- type: DECISION
  title: Going with ESP32-S3
```
"""
        r = parse_emits(text)
        assert r.malformed == ()
        assert len(r.emits) == 1
        assert r.emits[0] == ParsedEmit(
            type="DECISION", title="Going with ESP32-S3",
        )
        assert "memory-emit" not in r.clean_text
        assert r.clean_text.rstrip() == "Here is my call."

    def test_no_emit_block_is_fine(self) -> None:
        text = "Just prose. Nothing memory-worthy here.\n"
        r = parse_emits(text)
        assert r.emits == ()
        assert r.malformed == ()
        # When there's no emit block we preserve the text verbatim
        assert r.clean_text.strip() == "Just prose. Nothing memory-worthy here."

    def test_empty_emit_block_is_silently_allowed(self) -> None:
        # An empty YAML body — persona made the right choice not to emit
        text = """\
prose

```memory-emit

```
"""
        r = parse_emits(text)
        assert r.emits == ()
        assert r.malformed == ()
        assert "memory-emit" not in r.clean_text

    def test_multiple_emits_in_one_block(self) -> None:
        text = """\
prose

```memory-emit
- type: DECISION
  title: pick X
- type: ACTION
  title: order 10 of X
- type: PREDICTION
  title: this ships in 6 weeks
  confidence: 0.7
```
"""
        r = parse_emits(text)
        assert r.malformed == ()
        assert [e.type for e in r.emits] == ["DECISION", "ACTION", "PREDICTION"]
        assert r.emits[2].confidence == 0.7

    def test_emit_carries_optional_fields(self) -> None:
        text = """\
prose

```memory-emit
- type: INSIGHT
  title: brief headline
  content: |
    A longer body
    spanning lines.
  related: [evt-aaaa, evt-bbbb]
  tags: [esp32, hardware]
```
"""
        r = parse_emits(text)
        assert len(r.emits) == 1
        e = r.emits[0]
        assert e.content.startswith("A longer body")
        assert e.related == ("evt-aaaa", "evt-bbbb")
        assert e.tags == ("esp32", "hardware")

    def test_multiple_blocks_in_one_response(self) -> None:
        text = """\
first thought

```memory-emit
- type: DECISION
  title: first
```

then more prose

```memory-emit
- type: INSIGHT
  title: second
```
"""
        r = parse_emits(text)
        assert [e.title for e in r.emits] == ["first", "second"]
        assert "memory-emit" not in r.clean_text


# --------------------------------------------------------------------------
# Validation failures
# --------------------------------------------------------------------------


class TestMalformed:
    def test_invalid_yaml_records_malformed_attempt(self) -> None:
        text = """\
prose

```memory-emit
- type: DECISION
  title: "unbalanced quote
```
"""
        r = parse_emits(text)
        assert r.emits == ()
        assert len(r.malformed) == 1
        assert "invalid YAML" in r.malformed[0].reason

    def test_unknown_type_rejected(self) -> None:
        text = """\
```memory-emit
- type: WIZARDRY
  title: cast spell
```
"""
        r = parse_emits(text)
        assert r.emits == ()
        assert len(r.malformed) == 1
        assert "not in vocabulary" in r.malformed[0].reason

    def test_missing_title_rejected(self) -> None:
        text = """\
```memory-emit
- type: DECISION
```
"""
        r = parse_emits(text)
        assert r.emits == ()
        assert "missing required field 'title'" in r.malformed[0].reason

    def test_prediction_must_carry_confidence(self) -> None:
        text = """\
```memory-emit
- type: PREDICTION
  title: it will rain
```
"""
        r = parse_emits(text)
        assert r.emits == ()
        assert "requires 'confidence'" in r.malformed[0].reason

    def test_prediction_confidence_out_of_range_rejected(self) -> None:
        text = """\
```memory-emit
- type: PREDICTION
  title: x
  confidence: 1.5
```
"""
        r = parse_emits(text)
        assert "not in [0,1]" in r.malformed[0].reason

    def test_top_level_must_be_list(self) -> None:
        text = """\
```memory-emit
type: DECISION
title: not a list
```
"""
        r = parse_emits(text)
        assert "top-level must be a YAML list" in r.malformed[0].reason

    def test_mixed_valid_and_malformed_in_one_block(self) -> None:
        text = """\
```memory-emit
- type: DECISION
  title: good one
- type: NONSENSE
  title: bad one
- type: INSIGHT
  title: also good
```
"""
        r = parse_emits(text)
        assert [e.title for e in r.emits] == ["good one", "also good"]
        assert len(r.malformed) == 1
        assert "not in vocabulary" in r.malformed[0].reason

    def test_related_must_be_list_of_strings(self) -> None:
        text = """\
```memory-emit
- type: DECISION
  title: x
  related: 42
```
"""
        r = parse_emits(text)
        assert "related must be a list" in r.malformed[0].reason


# --------------------------------------------------------------------------
# Edge cases
# --------------------------------------------------------------------------


class TestEdgeCases:
    def test_empty_string_returns_empty_parse_result(self) -> None:
        r = parse_emits("")
        assert r.clean_text == ""
        assert r.emits == ()
        assert r.malformed == ()

    def test_fence_at_end_of_response_without_trailing_newline(self) -> None:
        text = "prose\n\n```memory-emit\n- type: DECISION\n  title: x\n```"
        r = parse_emits(text)
        assert len(r.emits) == 1

    def test_unrelated_fenced_code_block_left_alone(self) -> None:
        text = """\
here's some code:

```python
print("hello")
```

and prose.
"""
        r = parse_emits(text)
        assert r.emits == ()
        assert r.malformed == ()
        assert "print(\"hello\")" in r.clean_text
