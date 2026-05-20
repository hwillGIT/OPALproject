"""Voice-assistant-facing service over the EPIC Intelligence Layer.

This is the contract the OPAL voice assistant's **Contextual Router**
(Phase 3, Epic 4 in
`hardware/opalDevice/docs/architecture/opal-system-architecture-epics.md`)
will call when it determines that a clinician's spoken question
should be answered from the EPIC knowledge base.

End-to-end flow:

    Clinician voice question
              |
              v
    ASR transcription (out of scope)
              |
              v
    Contextual Router (voice_router_stub.py)
              |
              v
    IntelligenceAnswerService.answer(question)
              |
              v
    epic_intelligence.query     ──>  ChromaDB retrieval
              |
              v
    epic_intelligence.synthesis ──>  LLM provider (anthropic/openai/gemini/stub)
              |
              v
    Answer{text, citations}     ──>  TTS + on-glasses HUD render
"""

from .service import (
    AnswerServiceConfig,
    IntelligenceAnswerService,
    answer as quick_answer,
)
from .voice_router_stub import (
    ContextualRouter,
    RouteDecision,
)

__all__ = [
    "AnswerServiceConfig",
    "ContextualRouter",
    "IntelligenceAnswerService",
    "RouteDecision",
    "quick_answer",
]
