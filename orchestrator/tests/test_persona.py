"""Unit tests for the persona loader.

The loader is tiny but load-bearing: it wraps the persona's markdown
with our "stay in character for one phase" preamble and pulls a
display name + role label out of the H1 header. Exercise both paths
(metadata-driven, header-driven) against fake .md files in tmp_path,
plus the not-found path.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from orchestrator.persona import (
    Persona,
    PersonaNotFound,
    _extract_name_label,
    load_persona,
)


PERSONA_BODY = """\
# Athena Vance - Chief Strategist

You are Athena Vance, Chief Strategist.

You speak in punchy, decision-oriented sentences and you defend
your call.
"""


class TestLoadPersona:
    def test_load_persona_wraps_body_with_preamble(self, tmp_path: Path) -> None:
        (tmp_path / "athena.md").write_text(PERSONA_BODY, encoding="utf-8")
        p = load_persona("athena", personas_dir=tmp_path)
        assert isinstance(p, Persona)
        assert p.key == "athena"
        assert p.name == "Athena Vance"
        assert p.label == "Chief Strategist"
        # Preamble must precede the file body
        assert "Stay in character for this turn." in p.system_prompt
        assert p.system_prompt.endswith(PERSONA_BODY)
        assert p.source_path == tmp_path / "athena.md"

    def test_load_persona_falls_back_to_no_extension(self, tmp_path: Path) -> None:
        # No .md suffix — loader should still find it
        (tmp_path / "diego").write_text(PERSONA_BODY, encoding="utf-8")
        p = load_persona("diego", personas_dir=tmp_path)
        assert p.source_path == tmp_path / "diego"

    def test_load_persona_uses_metadata_when_supplied(self, tmp_path: Path) -> None:
        (tmp_path / "x.md").write_text("# Ignored Header - Should Not Be Used\nbody",
                                        encoding="utf-8")
        p = load_persona(
            "x",
            personas_dir=tmp_path,
            metadata={"name": "Overridden Name", "label": "Overridden Label"},
        )
        assert p.name == "Overridden Name"
        assert p.label == "Overridden Label"

    def test_missing_persona_raises_typed_error(self, tmp_path: Path) -> None:
        with pytest.raises(PersonaNotFound, match="not found"):
            load_persona("ghost", personas_dir=tmp_path)


class TestExtractNameLabel:
    def test_extracts_name_and_role_from_dash_header(self) -> None:
        n, l = _extract_name_label("# Bob Smith - VP of Sales\nrest", "bob", None)
        assert (n, l) == ("Bob Smith", "VP of Sales")

    def test_header_with_no_dash_uses_key_as_label(self) -> None:
        n, l = _extract_name_label("# Solo Name\nrest", "solo-key", None)
        assert n == "Solo Name"
        assert l == "solo-key"

    def test_no_header_falls_back_to_key(self) -> None:
        n, l = _extract_name_label("no header here", "fallback-key", None)
        assert n == "fallback-key"
        assert l == "fallback-key"

    def test_metadata_short_circuits_header_parsing(self) -> None:
        n, l = _extract_name_label("# Header Will Be Ignored",
                                    "k", {"name": "M-name", "label": "M-label"})
        assert (n, l) == ("M-name", "M-label")

    def test_metadata_with_partial_keys_uses_key_for_missing(self) -> None:
        # Only `name` set; label should fall back to the key
        n, l = _extract_name_label("# h", "the-key", {"name": "Just Name"})
        assert n == "Just Name"
        assert l == "the-key"
