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

MEMORY-FIRST PROTOCOL (typed events + scopes + retrieval + ontology):
- Protocol doc:                 memory_system/PROTOCOL.md
- Event schema:                 memory_system/events/schema.py
- Write + briefing CLI:         python -m memory_system.events.cli {write|briefing|briefing-post|rebuild|neo4j-rebuild}
- Briefing -> Mattermost cron:  memory_system/events/BRIEFING_POST.md (uses MATTERMOST_BRIEFING_WEBHOOK_URL)
- JSONL source of truth:        memory_system/events/log/YYYY-MM-DD.jsonl
- Scope primitive (auto-detect on every write):
                                memory_system/scopes/ + python -m memory_system.scopes.cli {list|lifecycle|revert|rebuild}
- Hybrid retrieval pipeline:    memory_system/retrieval/ (filter -> hybrid_search -> scope_expand -> window_truncate)
- Ontology + predicate engine:  memory_system/ontology/{taxonomy,predicates}.json
- Pytest:                       python -m pytest memory_system/tests/

EPIC EHR INTELLIGENCE LAYER (RAG over Epic docs):
- Module:                       epic_intelligence/
- Pipeline:                     python -m epic_intelligence.ingestion.pipeline
- Citation-aware query:         python -m epic_intelligence.query "<question>" --top-k 5
- Pytest:                       python -m pytest epic_intelligence/tests/

PILOT-SITE RUBRIC (D-1; scoring + champion ID):
- Module:                       pilot/
- Score a site:                 python -m pilot.cli score <site.yaml> [--json]
- Rank champions:               python -m pilot.cli champions <site.yaml>
- Example sites:                pilot/examples/{strong-fit,weak-fit,mt-sinai}.yaml
- README:                       pilot/README.md
- Pytest:                       python -m pytest pilot/tests/

BAA + IRB WORKFLOW TEMPLATES (D-2):
- BAA workflow:                 bots/shared/workflows/business/baa-negotiation.yaml
- BAA checklist (operator):     pilot/templates/baa-checklist.md
- IRB workflow:                 bots/shared/workflows/business/irb-submission.yaml
- IRB protocol skeleton:        pilot/templates/irb-protocol-skeleton.md
- Run BAA / IRB workflow:       python -m orchestrator.cli run {baa-negotiation|irb-submission} [--provider auto]

WORKFLOW ORCHESTRATOR RUNTIME (turns YAML workflows into executable runs):
- Module:                       orchestrator/
- List workflows:               python -m orchestrator.cli list
- Show one workflow:            python -m orchestrator.cli show <name>
- Run a workflow:               python -m orchestrator.cli run <name> [--provider stub|auto|...] [--dry-run] [--json]
- Default provider:             built-in StubProvider (no deps, no API key)
- Real LLMs:                    --provider auto delegates to epic_intelligence.synthesis
- Memory-emit protocol:         personas author fenced YAML blocks; runner parses + validates
                                (see orchestrator/README.md "Memory-emit protocol" section)
- Post-write predicates:        memory_system/ontology/predicates.json — runner evaluates
                                post_write triggers after each phase's emits land
- Pytest:                       python -m pytest orchestrator/tests/
