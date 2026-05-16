"""Load + navigate the OPAL tag taxonomy (SKOS-like, in JSON).

Pure stdlib. The JSON format is a deliberate simplification of SKOS:
no Turtle, no rdflib dependency. The semantics we keep:

  - prefLabel:  canonical display name for a concept
  - altLabel:   list of synonyms (used for matching, not display)
  - broader:    list of parent concept keys
  - narrower:   list of child concept keys (informational; derivable
                from broader)

This is enough for the briefing engine and predicate matcher to do
hierarchy walks ("everything broader than clinical-workflow") without
pulling in rdflib.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping


@dataclass(frozen=True)
class Concept:
    """One node in the taxonomy."""

    key: str
    pref_label: str
    alt_labels: tuple[str, ...] = field(default_factory=tuple)
    broader: tuple[str, ...] = field(default_factory=tuple)
    narrower: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class Taxonomy:
    concepts: Mapping[str, Concept]

    def get(self, key: str) -> Concept | None:
        return self.concepts.get(key)


# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------


def load_taxonomy(path: Path) -> Taxonomy:
    """Parse a JSON taxonomy file into a Taxonomy."""
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    concepts_raw = raw.get("concepts") or {}
    concepts: dict[str, Concept] = {}
    for key, payload in concepts_raw.items():
        if not isinstance(payload, dict):
            continue
        concepts[key] = Concept(
            key=key,
            pref_label=str(payload.get("prefLabel", key)),
            alt_labels=tuple(payload.get("altLabel") or ()),
            broader=tuple(payload.get("broader") or ()),
            narrower=tuple(payload.get("narrower") or ()),
        )
    return Taxonomy(concepts=concepts)


# ---------------------------------------------------------------------------
# Walk + expand
# ---------------------------------------------------------------------------


def all_tags(tax: Taxonomy) -> set[str]:
    """Every canonical tag (preferred + alternates) in the taxonomy."""
    out: set[str] = set()
    for c in tax.concepts.values():
        out.add(c.key)
        out.add(c.pref_label)
        out.update(c.alt_labels)
    return out


def parent_of(tax: Taxonomy, tag: str) -> set[str]:
    """Return the keys of concepts broader than ``tag``."""
    c = _resolve(tax, tag)
    if c is None:
        return set()
    return set(c.broader)


def children_of(tax: Taxonomy, tag: str) -> set[str]:
    """Return the keys of concepts narrower than ``tag``.

    Walks broader links in reverse if explicit narrower isn't set, so
    a partial taxonomy still works.
    """
    c = _resolve(tax, tag)
    out: set[str] = set()
    if c is not None:
        out.update(c.narrower)
    for other in tax.concepts.values():
        if (c is not None and c.key in other.broader) or (c is None and tag in other.broader):
            out.add(other.key)
    return out


def expand_tag(
    tax: Taxonomy,
    tag: str,
    depth: int = 1,
    direction: str = "broader",
) -> set[str]:
    """Walk the hierarchy ``depth`` steps in ``direction``.

    ``direction`` is one of: 'broader', 'narrower', 'both'.
    Returns the closure including the starting tag.
    """
    out: set[str] = {tag}
    frontier = {tag}
    for _ in range(depth):
        nxt: set[str] = set()
        for t in frontier:
            if direction in ("broader", "both"):
                nxt |= parent_of(tax, t)
            if direction in ("narrower", "both"):
                nxt |= children_of(tax, t)
        nxt -= out
        out |= nxt
        frontier = nxt
        if not frontier:
            break
    return out


def _resolve(tax: Taxonomy, tag: str) -> Concept | None:
    """Look up a concept by key, prefLabel, OR altLabel."""
    c = tax.concepts.get(tag)
    if c is not None:
        return c
    for other in tax.concepts.values():
        if other.pref_label == tag or tag in other.alt_labels:
            return other
    return None
