"""Memory-First Protocol — typed events on top of the existing
ChromaDB/Neo4j memory system.

This subpackage adds an event-taxonomy layer (DECISION, ACTION,
INSIGHT, PREDICTION, OUTCOME, DEBATE, CONTEXT_CHANGE, ARTIFACT)
without touching the existing `save_session.py` / `recall_context.py`
session-level functions. Both layers coexist.

See `../PROTOCOL.md` for the operator-facing protocol description.
"""

from .schema import (
    EVENT_TYPES,
    Event,
    EventValidationError,
    new_event,
    validate_event,
)

__all__ = [
    "EVENT_TYPES",
    "Event",
    "EventValidationError",
    "new_event",
    "validate_event",
]
