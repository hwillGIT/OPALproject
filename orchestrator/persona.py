"""Persona loader — turns a persona key into a system prompt.

Reads ``bots/shared/personas/gtm/<key>.md`` and packages it as a
``Persona`` value the runner uses to call the LLM. The persona file
becomes the LLM's system prompt verbatim; we wrap it with a short
preamble that tells the model to stay in character for one phase.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PERSONAS_DIR = REPO_ROOT / "bots" / "shared" / "personas" / "gtm"


class PersonaNotFound(FileNotFoundError):
    """Raised when a persona key doesn't resolve to a file."""


@dataclass(frozen=True)
class Persona:
    key: str
    name: str
    label: str
    system_prompt: str
    source_path: Path | None = None


_PREAMBLE = """\
You are the persona described BELOW. Stay in character for this turn.
You are participating in ONE phase of a structured business workflow.
Answer the operator's questions for this phase, drawing only on your
declared expertise and stated communication style. Cite specifics when
you have them. When you don't know something for sure, say so.

If the phase declares productive tensions you are part of, name them
explicitly and argue your side — that's the point of the panel.

---

"""


def load_persona(
    key: str,
    *,
    personas_dir: Path | None = None,
    metadata: dict | None = None,
) -> Persona:
    """Load a persona by key. Looks up the .md in ``personas_dir``.

    ``metadata`` is the optional persona metadata dict (matching the
    shape in ``bots/gtm/persona-metadata.js``). When omitted, we use
    the file's first ``# ...`` line as the display name + the key
    itself as the label.
    """
    d = personas_dir or PERSONAS_DIR
    candidates = [d / f"{key}.md", d / key]
    for path in candidates:
        if path.exists():
            text = path.read_text(encoding="utf-8")
            name, label = _extract_name_label(text, key, metadata)
            return Persona(
                key=key,
                name=name,
                label=label,
                system_prompt=_PREAMBLE + text,
                source_path=path,
            )
    raise PersonaNotFound(
        f"persona file for key {key!r} not found under {d}; "
        f"tried {[str(c) for c in candidates]}",
    )


def _extract_name_label(text: str, key: str, metadata: dict | None) -> tuple[str, str]:
    """Pull a display name + role label from the file header.

    Preferred order:
      1. If ``metadata`` carries name/label, use those.
      2. The first markdown H1: ``# Name - Role`` (per existing personas).
      3. Fallback to the key.
    """
    if metadata:
        n = metadata.get("name") or key
        l = metadata.get("label") or key
        return n, l
    for line in text.splitlines():
        stripped = line.lstrip()
        if not stripped.startswith("# "):
            continue
        header = stripped[2:].strip()
        # Format: "Name - Role"
        if " - " in header:
            n, l = header.split(" - ", 1)
            return n.strip(), l.strip()
        return header, key
    return key, key
