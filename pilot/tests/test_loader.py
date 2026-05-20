"""Unit tests for the site YAML loader."""
from __future__ import annotations

from pathlib import Path

import pytest

from pilot.loader import SiteLoadError, load_site


MINIMAL = """\
name: Tiny Hospital
clinical_pain_addressed: true
"""


def _write(tmp_path: Path, body: str) -> Path:
    p = tmp_path / "site.yaml"
    p.write_text(body, encoding="utf-8")
    return p


class TestHappyPath:
    def test_minimal_site_loads(self, tmp_path: Path) -> None:
        s = load_site(_write(tmp_path, MINIMAL))
        assert s.name == "Tiny Hospital"
        assert s.clinical_pain_addressed is True
        # Defaults fill the rest
        assert s.week_one_plausible is False
        assert s.champion_candidates == ()
        assert s.baa_path_days is None
        assert s.irb_required is None

    def test_champion_candidates_parsed(self, tmp_path: Path) -> None:
        body = MINIMAL + """
champion_candidates:
  - name: Alice
    role: Director, Nursing
    authority_level: 2
    bandwidth: 7
    motivation: 9
    evidence:
      - "Sent intro email Q1"
      - "Attended discovery call"
"""
        s = load_site(_write(tmp_path, body))
        assert len(s.champion_candidates) == 1
        c = s.champion_candidates[0]
        assert c.name == "Alice"
        assert c.role == "Director, Nursing"
        assert c.authority_level == 2
        assert c.bandwidth == 7
        assert c.motivation == 9
        assert c.evidence == ("Sent intro email Q1", "Attended discovery call")

    def test_int_or_none_for_baa_days(self, tmp_path: Path) -> None:
        body = MINIMAL + "\nbaa_path_days: 45\n"
        s = load_site(_write(tmp_path, body))
        assert s.baa_path_days == 45

    def test_bool_or_none_for_irb(self, tmp_path: Path) -> None:
        s_true = load_site(_write(tmp_path, MINIMAL + "\nirb_required: true\n"))
        assert s_true.irb_required is True
        # null preserved as None
        s_null = load_site(_write(tmp_path, MINIMAL + "\nirb_required: null\n"))
        assert s_null.irb_required is None


class TestValidationFailures:
    def test_missing_file(self, tmp_path: Path) -> None:
        with pytest.raises(SiteLoadError, match="not found"):
            load_site(tmp_path / "ghost.yaml")

    def test_missing_name(self, tmp_path: Path) -> None:
        body = "clinical_pain_addressed: true\n"
        with pytest.raises(SiteLoadError, match="missing required field 'name'"):
            load_site(_write(tmp_path, body))

    def test_top_level_not_mapping(self, tmp_path: Path) -> None:
        with pytest.raises(SiteLoadError, match="top-level must be a mapping"):
            load_site(_write(tmp_path, "- just a list\n- of items\n"))

    def test_champion_missing_required_field(self, tmp_path: Path) -> None:
        body = MINIMAL + """
champion_candidates:
  - role: Director
"""
        with pytest.raises(SiteLoadError, match="missing 'name'"):
            load_site(_write(tmp_path, body))

    def test_baa_days_non_integer(self, tmp_path: Path) -> None:
        body = MINIMAL + "\nbaa_path_days: not-a-number\n"
        with pytest.raises(SiteLoadError, match="must be an integer"):
            load_site(_write(tmp_path, body))

    def test_authority_clamps_out_of_range(self, tmp_path: Path) -> None:
        body = MINIMAL + """
champion_candidates:
  - name: x
    role: r
    authority_level: 99
"""
        s = load_site(_write(tmp_path, body))
        assert s.champion_candidates[0].authority_level == 3
