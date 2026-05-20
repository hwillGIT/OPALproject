PROJECT: OPAL Project - SAFe PM System
ROOT: G:\Projects\OPALproject\ProjectWork

SYSTEM CONFIGURATION:
- Framework: SAFe 6.0
- Location: .github/spec-kit/
- Main Controller: .github/spec-kit/SAFe-Controller.ps1

AVAILABLE AGENTS (SAFe roles):
- Product Management (Program Level)
- Release Train Engineer (Program Level)
- Product Owner (Team Level)
- Scrum Master (Team Level)

SAFE INSTRUCTIONS:
Read .github/spec-kit/instructions/safe-roles/* for agent behaviors
Use .github/spec-kit/modules/* for SAFe tools (WSJF, Program Board, etc.)

---

AGENT TOPOLOGY (Mattermost bot platform):
- Persona roster + departments: bots/shared/personas/DEPARTMENTS.md
- Productive-tensions matrix:   bots/shared/personas/TENSIONS.md
- Router metadata:              bots/gtm/persona-metadata.js
- Persona validator:            node bots/gtm/scripts/validate-personas.js

BUSINESS WORKFLOWS (multi-persona, OPAL-domain):
- Workflow registry:            bots/shared/workflows/business/
- Workflow patterns:            bots/shared/workflows/*.yaml (orchestration)
- Workflow validator:           node bots/shared/workflows/validate.js
- See README:                   bots/shared/workflows/README.md

MEMORY-FIRST PROTOCOL (typed events):
- Protocol doc:                 memory_system/PROTOCOL.md
- Event schema:                 memory_system/events/schema.py
- Write + briefing CLI:         python -m memory_system.events.cli {write|briefing|rebuild}
- JSONL source of truth:        memory_system/events/log/YYYY-MM-DD.jsonl
- Pytest:                       python -m pytest memory_system/tests/

EPIC EHR INTELLIGENCE LAYER (RAG over Epic docs):
- Module:                       epic_intelligence/
- Pipeline:                     python -m epic_intelligence.ingestion.pipeline
- Citation-aware query:         python -m epic_intelligence.query "<question>" --top-k 5
- Pytest:                       python -m pytest epic_intelligence/tests/
