"""Load a Site description from a YAML file.

The YAML mirrors the Site dataclass field-for-field. Champions are a
list of mappings. Validation surfaces clear errors at load time so
the CLI fails fast instead of producing a misleading score.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "pilot.loader requires pyyaml. Install with: pip install pyyaml",
    ) from exc

from .models import ChampionCandidate, Site


class SiteLoadError(ValueError):
    """Raised on a malformed pilot-site YAML."""


def load_site(path: str | Path) -> Site:
    """Parse + validate a site YAML; return a Site."""
    p = Path(path)
    if not p.exists():
        raise SiteLoadError(f"site file not found: {p}")
    try:
        raw = yaml.safe_load(p.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise SiteLoadError(f"failed to parse {p}: {exc}") from exc
    if not isinstance(raw, dict):
        raise SiteLoadError(
            f"{p.name}: top-level must be a mapping; got {type(raw).__name__}",
        )

    return _build_site(raw, source_name=p.name)


def _build_site(raw: dict[str, Any], *, source_name: str) -> Site:
    if "name" not in raw or not raw["name"]:
        raise SiteLoadError(f"{source_name}: missing required field 'name'")

    champion_candidates = tuple(
        _build_champion(c, source_name, i)
        for i, c in enumerate(raw.get("champion_candidates") or ())
    )

    return Site(
        name=str(raw["name"]),
        clinical_pain_addressed=bool(raw.get("clinical_pain_addressed", False)),
        week_one_plausible=bool(raw.get("week_one_plausible", False)),
        champion_candidates=champion_candidates,
        cmo_aligned=bool(raw.get("cmo_aligned", False)),
        c_suite_metric_mapped=bool(raw.get("c_suite_metric_mapped", False)),
        epic_version=str(raw.get("epic_version") or ""),
        epic_supported=bool(raw.get("epic_supported", False)),
        fhir_endpoints_exposed=bool(raw.get("fhir_endpoints_exposed", False)),
        device_provisioning_path=bool(raw.get("device_provisioning_path", False)),
        baa_path_days=_int_or_none(raw.get("baa_path_days"), source_name, "baa_path_days"),
        irb_required=_bool_or_none(raw.get("irb_required")),
        security_review_path=bool(raw.get("security_review_path", False)),
        pricing_fit=bool(raw.get("pricing_fit", False)),
        reference_design_value=bool(raw.get("reference_design_value", False)),
        site_bandwidth=bool(raw.get("site_bandwidth", False)),
        decision_maker_accessible=bool(raw.get("decision_maker_accessible", False)),
        notes=tuple(str(n) for n in (raw.get("notes") or ())),
    )


def _build_champion(
    raw: Any,
    source_name: str,
    index: int,
) -> ChampionCandidate:
    if not isinstance(raw, dict):
        raise SiteLoadError(
            f"{source_name}: champion_candidates[{index}] must be a mapping",
        )
    for required in ("name", "role"):
        if not raw.get(required):
            raise SiteLoadError(
                f"{source_name}: champion_candidates[{index}] missing {required!r}",
            )
    return ChampionCandidate(
        name=str(raw["name"]),
        role=str(raw["role"]),
        authority_level=_clamp_int(raw.get("authority_level", 0), 0, 3),
        bandwidth=_clamp_int(raw.get("bandwidth", 0), 0, 10),
        motivation=_clamp_int(raw.get("motivation", 0), 0, 10),
        evidence=tuple(str(e) for e in (raw.get("evidence") or ())),
    )


def _int_or_none(v: Any, source: str, field: str) -> int | None:
    if v is None or v == "":
        return None
    try:
        return int(v)
    except (TypeError, ValueError) as exc:
        raise SiteLoadError(f"{source}: {field} must be an integer; got {v!r}") from exc


def _bool_or_none(v: Any) -> bool | None:
    if v is None or v == "":
        return None
    return bool(v)


def _clamp_int(v: Any, lo: int, hi: int) -> int:
    try:
        n = int(v)
    except (TypeError, ValueError):
        n = 0
    return max(lo, min(hi, n))
