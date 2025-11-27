# PLAYBOOK QUICK REFERENCE
# Structure Overview for Mattermost Playbooks UI

================================================================================
PLAYBOOK: Customer Onboarding
================================================================================

## Phase 0: Pre-Onboarding (1-3 days)
├── Checklist: Sales Handoff Document (19 tasks)
│   ├── Customer Profile (4)
│   ├── Deal Context (6) ← QUESTIONS
│   ├── Stakeholder Map (5)
│   ├── Success Criteria (4) ← QUESTIONS
│   ├── Technical Environment (5)
│   └── Risk Assessment (5)
├── Checklist: Handoff Execution (8 tasks)
└── Exit Criteria (4 tasks)

## Phase 1: Kickoff & Discovery (3-7 days)
├── Checklist: Pre-Kickoff Preparation (5 tasks)
├── Checklist: Kickoff Meeting (19 tasks)
│   ├── Introductions (3)
│   ├── Confirm Understanding (5)
│   ├── Success Metrics (6) ← QUESTIONS
│   ├── Project Scope (5)
│   ├── Governance (5) ← QUESTIONS
│   └── Next Steps (3)
├── Checklist: Technical Discovery (7 tasks) ← QUESTIONS
├── Checklist: Process Discovery (5 tasks) ← QUESTIONS
├── Checklist: Phase 1 Outputs (6 tasks)
└── Exit Criteria (5 tasks)

## Phase 2: Technical Implementation (1-4 weeks)
├── Checklist: Core Setup (7 tasks)
├── Checklist: Integration Track (9 tasks) ← QUESTIONS
├── Checklist: Data Migration (11 tasks) ← QUESTIONS
├── Checklist: Security & Compliance (9 tasks) ← QUESTIONS
├── Checklist: Customization (7 tasks)
├── Checklist: Risk Mitigation (6 tasks)
└── Exit Criteria (8 tasks)

## Phase 3: Training & Enablement (1-3 weeks)
├── Checklist: Change Management - ADKAR (5 tasks)
├── Checklist: Executive Sponsor Training (6 tasks) ← QUESTION
├── Checklist: Admin/Power User Training (10 tasks) ← QUESTION
├── Checklist: Project Lead Training (7 tasks)
├── Checklist: End User Training (10 tasks) ← QUESTION
├── Checklist: Change Champion Training (8 tasks)
├── Checklist: Training Resources (6 tasks)
├── Checklist: Training Metrics (5 tasks)
└── Exit Criteria (6 tasks)

## Phase 4: Go-Live & Hypercare (1-2 weeks)
├── Checklist: Go-Live Readiness - Technical (9 tasks)
├── Checklist: Go-Live Readiness - Users (8 tasks)
├── Checklist: Go-Live Readiness - Support (7 tasks)
├── Checklist: Go-Live Readiness - Business (5 tasks)
├── Checklist: Go-Live Execution (8 tasks)
├── Checklist: Hypercare Operations (7 tasks)
├── Checklist: Issue Management (5 tasks)
└── Exit Criteria (6 tasks)

## Phase 5: Steady State & Value Realization (Ongoing)
├── Checklist: Day 30 Check-in (10 tasks) ← QUESTIONS
├── Checklist: Day 60 Check-in (10 tasks) ← QUESTIONS
├── Checklist: Day 90 QBR (12 tasks) ← QUESTIONS
├── Checklist: Ongoing Health Monitoring (20 tasks)
├── Checklist: Expansion Triggers (5 tasks)
├── Checklist: Renewal Preparation (8 tasks)
└── Retrospective (12 tasks) ← QUESTIONS

================================================================================
TOTAL: ~300 tasks across 6 phases
================================================================================

## HOW TO CREATE IN MATTERMOST

1. Go to: Product Menu (≡) → Playbooks → Create Playbook

2. Name: "Customer Onboarding - [Segment]"

3. For each PHASE, create a new CHECKLIST:
   - Click "Add checklist"
   - Name it: "Phase X: [Name]"

4. For each TASK, add an item:
   - Click "Add a task"
   - Copy task name from template
   - Add description with questions/details

5. Configure ACTIONS:
   - Checklist: Actions → "When run starts"
   - Add: Create channel, invite members, send message

6. Configure STATUS UPDATES:
   - Settings → Status Updates
   - Enable weekly reminders
   - Use template from playbook doc

7. Configure RETROSPECTIVE:
   - Settings → Retrospective
   - Enable retrospective
   - Use template from playbook doc

================================================================================
AUTOMATION QUICK SETUP
================================================================================

## Run Start Actions
Channel: onboarding-{{participant0 | split: "@" | first}}
Invite: @cs-team
Message: Welcome to the onboarding run!

## When Task Overdue
Notify: Run owner
After: 48 hours

## Status Updates
Frequency: Weekly (Monday 9am)
Reminder: Yes

## Retrospective
Enabled: Yes
Reminder: 7 days after run ends
