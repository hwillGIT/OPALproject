"""Deterministic identifier minting for scopes and transitions.

Pure functions. No I/O. Identifier shapes:

    scope-{slug}-{YYYY-MM}      e.g. scope-aurora-2026-05
    trans-{12 hex}              SHA-256 of (scope_id|from|to|timestamp)
    rb-{12 hex}                 SHA-256 of "rollback|{transition_id}"

The month suffix on scope ids disambiguates two initiatives that
happen to share a name across years. Transition + rollback ids are
deterministic so replaying the event log produces identical scope
identities on every rebuild.
"""
from __future__ import annotations

import hashlib
import re

_SLUG_INVALID = re.compile(r"[^a-z0-9]+")
_SLUG_TRIM = re.compile(r"^-+|-+$")


def slugify(name: str) -> str:
    """Lowercase, replace non-[a-z0-9] runs with single hyphens, trim hyphens.

    Examples:
        >>> slugify("Project Aurora")
        'project-aurora'
        >>> slugify("OPAL / LYNA — pilot 3a")
        'opal-lyna-pilot-3a'
        >>> slugify("___-")
        ''
    """
    lowered = name.strip().lower()
    hyphenated = _SLUG_INVALID.sub("-", lowered)
    return _SLUG_TRIM.sub("", hyphenated)


def make_scope_id(name: str, first_seen_iso: str) -> str:
    """Build a stable scope id from a display name + the YYYY-MM of first sight.

    ``first_seen_iso`` is parsed for its YYYY-MM prefix only (the date
    component is enough for disambiguation). Raises ValueError if the
    slugified name is empty.
    """
    slug = slugify(name)
    if not slug:
        raise ValueError(f"name {name!r} slugifies to empty string")
    month = first_seen_iso[:7]  # 'YYYY-MM' from ISO-8601
    if not re.match(r"^\d{4}-\d{2}$", month):
        raise ValueError(
            f"first_seen_iso must start with YYYY-MM; got {first_seen_iso!r}",
        )
    return f"scope-{slug}-{month}"


def make_transition_id(
    scope_id: str,
    from_status: str | None,
    to_status: str,
    timestamp_iso: str,
) -> str:
    """Deterministic id for a transition.

    Same inputs => same id, which makes JSONL replay idempotent on the
    transition store.
    """
    payload = f"{scope_id}|{from_status or ''}|{to_status}|{timestamp_iso}"
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]
    return f"trans-{digest}"


def make_rollback_id(transition_id: str) -> str:
    """Deterministic rollback handle for a transition.

    Same transition => same revert handle, every time. The handle is
    what `memory-scopes-revert` consumes to undo a Tier-1 or Tier-2
    autonomous move within its rollback window.
    """
    digest = hashlib.sha256(
        f"rollback|{transition_id}".encode("utf-8"),
    ).hexdigest()[:12]
    return f"rb-{digest}"
