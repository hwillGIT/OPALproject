# CUSTOMER ONBOARDING PLAYBOOK TEMPLATE
# Best-in-Class Framework for Mattermost Playbooks

================================================================================
PLAYBOOK SETTINGS
================================================================================
Name: Customer Onboarding - [SEGMENT]
Description: End-to-end customer onboarding from sales handoff to steady state
Run Summary Template: Onboarding: {{CustomerName}} | Segment: {{Segment}} | ARR: {{ARR}}

Keywords (auto-trigger): new customer, customer onboarding, kickoff
Default Owner: Customer Success Manager
Channel Name Template: onboarding-{{CustomerName | lowercase}}
Channel Playbook Link: Enabled

================================================================================
PHASE 0: PRE-ONBOARDING (SALES HANDOFF)
Duration: 1-3 days | Owner: Sales + CS Manager
================================================================================

## Checklist: Sales Handoff Document

### Customer Profile
- [ ] Company name, industry, size, geography documented
- [ ] ARR and contract length recorded
- [ ] Segment identified (Self-serve / Scaled / High-touch / Strategic)
- [ ] Contract start date confirmed

### Deal Context
- [ ] QUESTION: Why did they buy? (Business problem solved)
- [ ] QUESTION: Why now? (Trigger event)
- [ ] QUESTION: Why us? (Differentiator that won the deal)
- [ ] QUESTION: Who did they evaluate? (Competitors considered)
- [ ] QUESTION: What did we promise? (Specific commitments made)
- [ ] QUESTION: What concerns remain? (Unresolved objections)

### Stakeholder Map
- [ ] Executive Sponsor identified: [Name, Title, Email, Motivation]
- [ ] Project Lead identified: [Name, Title, Email, Working style]
- [ ] Technical Lead identified: [Name, Title, Email, Skill level]
- [ ] Change Champion identified: [Name, Title, Email, Influence level]
- [ ] Potential Blocker/Skeptic identified: [Name, Concerns]

### Success Criteria
- [ ] QUESTION: What does success look like to THIS customer?
- [ ] Primary success metric defined and quantified
- [ ] Target timeline documented
- [ ] Measurement method agreed

### Technical Environment
- [ ] Current tech stack documented
- [ ] Integration requirements listed
- [ ] Data migration scope assessed (volume, complexity, source)
- [ ] Security requirements identified (SSO, compliance, DPA)
- [ ] IT constraints noted (approval processes, change windows)

### Risk Assessment
- [ ] Timeline risks identified (hard deadlines, events)
- [ ] Resource risks identified (customer bandwidth, skills)
- [ ] Technical risks identified (complex integrations, legacy systems)
- [ ] Political risks identified (internal resistance, competing priorities)
- [ ] Budget risks identified (services budget, expansion potential)

## Checklist: Handoff Execution

- [ ] Handoff meeting scheduled (Sales + CS + Implementation)
- [ ] Sales presents handoff document (15 min)
- [ ] CS asks clarifying questions (10 min)
- [ ] Risks and mitigation discussed (10 min)
- [ ] Customer communication plan agreed
- [ ] Customer channel created in Mattermost
- [ ] Welcome email sent to customer introducing CS team
- [ ] Internal team briefed on customer context

### EXIT CRITERIA - PHASE 0
- [ ] Handoff document 100% complete
- [ ] CSM assigned and accepted
- [ ] Kickoff meeting scheduled with customer
- [ ] All internal stakeholders informed

================================================================================
PHASE 1: KICKOFF & DISCOVERY
Duration: 3-7 days | Owner: CS Manager
================================================================================

## Checklist: Pre-Kickoff Preparation

- [ ] Handoff document reviewed thoroughly
- [ ] Kickoff deck customized (not generic template)
- [ ] 3 key validation questions prepared
- [ ] Preliminary success plan drafted
- [ ] Meeting logistics confirmed (video link, attendees, duration)

## Checklist: Kickoff Meeting (60-90 min)

### Introductions (10 min)
- [ ] Your team introduced: who does what
- [ ] Their team introduced: roles and responsibilities
- [ ] Working styles and communication preferences discussed

### Confirm Understanding (15 min)
- [ ] VALIDATE: "Here's what we understand about your goals..."
- [ ] VALIDATE: "Here's what success looks like to you..."
- [ ] VALIDATE: "Here are the key dates and constraints..."
- [ ] Customer confirms or corrects understanding
- [ ] Any gaps in handoff document filled

### Success Metrics (15 min)
- [ ] Primary success metric confirmed
- [ ] QUESTION: How will we measure this metric?
- [ ] QUESTION: What is the baseline today?
- [ ] Target at 30 days defined
- [ ] Target at 60 days defined
- [ ] Target at 90 days defined

### Project Scope & Timeline (20 min)
- [ ] What's IN scope for Phase 1 documented
- [ ] What's explicitly OUT of scope documented
- [ ] Key milestones identified with dates
- [ ] Dependencies identified
- [ ] Risks discussed and logged

### Governance (10 min)
- [ ] Meeting cadence agreed (weekly status recommended)
- [ ] Communication channel agreed (email/Mattermost/Slack)
- [ ] QUESTION: If we're stuck, who do we escalate to?
- [ ] Decision-making authority clarified
- [ ] Status report format agreed

### Next Steps (10 min)
- [ ] Action items captured with owners and dates
- [ ] Immediate next steps clear (what happens tomorrow)
- [ ] Customer deliverables this week identified

## Checklist: Technical Discovery

- [ ] Current architecture diagram obtained
- [ ] QUESTION: What SSO provider do you use?
- [ ] Integration inventory completed
- [ ] QUESTION: What APIs/webhooks/iPaaS do you use?
- [ ] Data sources and volumes documented
- [ ] Security/compliance questionnaire completed
- [ ] Network/firewall considerations documented

## Checklist: Process Discovery

- [ ] QUESTION: How do you do [core workflow] today?
- [ ] QUESTION: Where does the current process break down?
- [ ] QUESTION: Who are the users? How many? Where located?
- [ ] QUESTION: What reports/dashboards do you need?
- [ ] QUESTION: What decisions need data from this system?

## Checklist: Phase 1 Outputs

- [ ] Success Plan document created (customer sign-off required)
- [ ] Technical Requirements Document created
- [ ] Project Timeline with milestones created
- [ ] Risk Register created (risks + mitigation plans)
- [ ] Stakeholder Matrix finalized
- [ ] Communication Plan documented

### EXIT CRITERIA - PHASE 1
- [ ] Success Plan signed off by customer
- [ ] Technical requirements documented and validated
- [ ] Project timeline agreed by all parties
- [ ] All stakeholders identified and engaged
- [ ] Phase 2 kickoff scheduled

================================================================================
PHASE 2: TECHNICAL IMPLEMENTATION
Duration: 1-4 weeks | Owner: Implementation/Solutions Engineer
================================================================================

## Checklist: Workstream 1 - Core Setup (Week 1)

- [ ] Environment/tenant provisioned
- [ ] Organization settings configured
- [ ] User authentication set up
- [ ] Admin accounts created
- [ ] Roles and permissions configured
- [ ] Basic branding/customization applied
- [ ] CHECKPOINT: Admin can log in and navigate successfully

## Checklist: Workstream 2 - Integration Track (Weeks 1-3)

- [ ] Integration requirements reviewed with customer
- [ ] QUESTION: Do we have all API credentials from customer?
- [ ] API credentials obtained and securely stored
- [ ] Integration development/configuration started
- [ ] Integration testing in sandbox completed
- [ ] Integration testing in production completed
- [ ] Error handling and monitoring configured
- [ ] CHECKPOINT: Data flows correctly between systems

## Checklist: Workstream 3 - Data Migration (Weeks 2-3)

- [ ] Data inventory completed
- [ ] Data mapping document created
- [ ] QUESTION: Has customer cleaned source data?
- [ ] Data cleanup completed (customer responsibility)
- [ ] Migration scripts developed
- [ ] Dry run migration in sandbox completed
- [ ] Data validation and reconciliation completed
- [ ] Production migration scheduled with customer
- [ ] Production migration executed
- [ ] Post-migration validation completed
- [ ] CHECKPOINT: Historical data accessible and accurate

## Checklist: Workstream 4 - Security & Compliance (Parallel)

- [ ] Security questionnaire completed
- [ ] QUESTION: What SSO/SAML provider? Configuration details?
- [ ] SSO/SAML configuration completed
- [ ] MFA enabled (if required)
- [ ] Audit logging configured
- [ ] Data retention policies configured
- [ ] DPA/BAA signed (if required)
- [ ] Penetration test completed (if required)
- [ ] CHECKPOINT: Security team sign-off obtained

## Checklist: Workstream 5 - Customization (Weeks 2-4)

- [ ] Workflow requirements gathered from customer
- [ ] Custom fields/objects created
- [ ] Automations configured
- [ ] Reports/dashboards built
- [ ] Templates created
- [ ] Custom integrations built (if any)
- [ ] CHECKPOINT: Workflows operate as designed

## Checklist: Risk Mitigation

- [ ] Change request process defined and communicated
- [ ] Customer IT engaged and SLAs agreed
- [ ] Data audit completed before migration
- [ ] SSO POC completed before full rollout
- [ ] Named contacts and backups confirmed
- [ ] Weekly checkpoints scheduled with early warning triggers

### EXIT CRITERIA - PHASE 2
- [ ] Core platform configured and tested
- [ ] All critical integrations working
- [ ] Data migrated and validated
- [ ] Security requirements met with sign-off
- [ ] Admin trained on basic operations
- [ ] Test users validated key workflows
- [ ] Technical documentation complete
- [ ] Ready for training phase

================================================================================
PHASE 3: TRAINING & ENABLEMENT
Duration: 1-3 weeks | Owner: CS Manager + Training
================================================================================

## Checklist: Change Management Foundation (ADKAR)

- [ ] Awareness: "Why" communicated to all stakeholders
- [ ] Desire: "What's in it for me" articulated per role
- [ ] Knowledge: Training curriculum mapped to roles
- [ ] Ability: Hands-on practice environment ready
- [ ] Reinforcement: Recognition and support plan ready

## Checklist: Executive Sponsor Training (30 min)

- [ ] Training scheduled with Executive Sponsor
- [ ] Business value dashboard walkthrough
- [ ] Success metrics overview
- [ ] Escalation and support process explained
- [ ] Quarterly business review preview
- [ ] QUESTION: Any concerns or questions from sponsor?

## Checklist: Admin/Power User Training (4-8 hours)

- [ ] Training sessions scheduled
- [ ] System administration covered
- [ ] User management covered
- [ ] Configuration and customization covered
- [ ] Reporting and analytics covered
- [ ] Troubleshooting basics covered
- [ ] Best practices shared
- [ ] Certification exam offered (optional)
- [ ] QUESTION: Do admins feel confident to manage day-to-day?

## Checklist: Project Lead Training (2 hours)

- [ ] Training scheduled with Project Lead
- [ ] Project tracking features covered
- [ ] Status reporting covered
- [ ] Team management covered
- [ ] Integration overview provided
- [ ] Support and escalation explained
- [ ] CHECKPOINT: Project Lead can run status independently

## Checklist: End User Training (1-2 hours per workflow)

- [ ] Training sessions scheduled (multiple if needed)
- [ ] Login and navigation covered
- [ ] Core workflow #1 trained
- [ ] Core workflow #2 trained
- [ ] Core workflow #3 trained (if applicable)
- [ ] Getting help (self-service + support) explained
- [ ] Tips and tricks shared
- [ ] Quick reference guide distributed
- [ ] QUESTION: What questions do users have?

## Checklist: Change Champion Training (3-4 hours)

- [ ] Champions identified (1 per team/department)
- [ ] All end-user training completed
- [ ] Advanced features training
- [ ] "How to train others" session
- [ ] Feedback collection process
- [ ] Internal advocacy role explained
- [ ] Community/forum access provided
- [ ] Champion recognition program explained

## Checklist: Training Delivery & Resources

- [ ] Live sessions recorded for future reference
- [ ] Self-paced e-learning modules available
- [ ] In-app guides/tooltips configured
- [ ] Documentation/knowledge base accessible
- [ ] Sandbox environment available for practice
- [ ] Office hours scheduled for ongoing questions

## Checklist: Training Metrics

- [ ] Training completion rate tracked (target: >85%)
- [ ] Assessment scores tracked (target: >80%)
- [ ] Time-to-first-solo-workflow measured
- [ ] User confidence survey sent
- [ ] Support tickets from training tracked

### EXIT CRITERIA - PHASE 3
- [ ] Training completion rate >85%
- [ ] All personas trained (exec, admin, PM, users, champions)
- [ ] Champions activated and engaged
- [ ] Support resources accessible
- [ ] Users can perform core workflows independently
- [ ] Go-live readiness confirmed

================================================================================
PHASE 4: GO-LIVE & HYPERCARE
Duration: 1-2 weeks | Owner: CS Manager + Support
================================================================================

## Checklist: Go-Live Readiness - Technical

- [ ] All integrations tested in production
- [ ] Data migration completed and validated
- [ ] Performance baseline captured
- [ ] Monitoring and alerting configured
- [ ] Backup and recovery tested
- [ ] Rollback plan documented and tested
- [ ] SSL/TLS certificates valid
- [ ] DNS configured correctly
- [ ] Load testing completed (if applicable)

## Checklist: Go-Live Readiness - Users

- [ ] All users have active accounts
- [ ] SSO working for all users
- [ ] Training completion verified (>85%)
- [ ] Quick reference guides distributed
- [ ] Support resources documented and shared
- [ ] Champions confirmed and active
- [ ] Go-live communication drafted
- [ ] Feedback channel established

## Checklist: Go-Live Readiness - Support

- [ ] Support team briefed on this customer
- [ ] Known issues documented
- [ ] Escalation contacts confirmed (both sides)
- [ ] Hypercare SLAs activated (4h response)
- [ ] War room channel created
- [ ] On-call schedule confirmed
- [ ] CS team added to escalation path

## Checklist: Go-Live Readiness - Business

- [ ] Executive sponsor informed of go-live date
- [ ] Success metrics baseline captured
- [ ] Go-live announcement prepared
- [ ] Celebration planned
- [ ] First business review scheduled (Day 90)

## Checklist: Go-Live Execution

- [ ] Final go/no-go decision made
- [ ] Go-live communication sent to all users
- [ ] Production environment activated
- [ ] Old system access modified (if applicable)
- [ ] Monitoring dashboards active
- [ ] War room staffed
- [ ] First hours: no critical issues
- [ ] End of Day 1: status update sent

## Checklist: Hypercare Operations (Daily)

### Daily Rhythm
- [ ] Morning: Check dashboards, review overnight issues
- [ ] Morning: Standup with internal team
- [ ] Midday: Proactive outreach to customer PM
- [ ] Afternoon: Issue triage and prioritization
- [ ] End of day: Status update to stakeholders

### Hypercare Standards
- [ ] Response time: 4 hours (not 24)
- [ ] Named contact (not queue-based)
- [ ] Real-time channel active (not just tickets)
- [ ] Proactive monitoring (don't wait for tickets)
- [ ] Direct engineering escalation path

## Checklist: Issue Management

- [ ] P1 issues: Resolved within 4 hours
- [ ] P2 issues: Resolved within 24 hours
- [ ] P3 issues: Tracked and communicated
- [ ] Known issues list maintained
- [ ] Customer updated on all open issues daily

### EXIT CRITERIA - PHASE 4
- [ ] 7 consecutive days with no P1 issues
- [ ] Support ticket volume stabilized
- [ ] Key workflows operating normally
- [ ] Customer PM confirms comfort level
- [ ] Health score in green zone (>75)
- [ ] Hypercare period formally ended

================================================================================
PHASE 5: STEADY STATE & VALUE REALIZATION
Duration: Ongoing | Owner: CS Manager
================================================================================

## Checklist: Day 30 Check-in

- [ ] Day 30 meeting scheduled with customer
- [ ] Initial adoption metrics reviewed
  - [ ] DAU/WAU tracked
  - [ ] Feature adoption measured
  - [ ] Login frequency analyzed
- [ ] Early feedback collected
  - [ ] QUESTION: What's working well?
  - [ ] QUESTION: What's frustrating?
  - [ ] QUESTION: What's missing?
- [ ] Quick wins identified and celebrated
- [ ] Blockers identified and addressed
- [ ] Training reinforcement (if needed)
- [ ] Plan adjusted based on reality
- [ ] Day 60 check-in scheduled

## Checklist: Day 60 Check-in

- [ ] Day 60 meeting scheduled
- [ ] Value realization check
  - [ ] QUESTION: Are you seeing the value you expected?
  - [ ] Compare metrics to baseline
  - [ ] Document wins and ROI indicators
- [ ] Feature adoption depth reviewed
- [ ] Optimization opportunities identified
- [ ] Expansion conversations initiated
  - [ ] Additional users?
  - [ ] Additional features?
  - [ ] Additional use cases?
- [ ] Support health reviewed
- [ ] Stakeholder pulse check
- [ ] QBR preparation started

## Checklist: Day 90 Business Review (QBR)

### Preparation
- [ ] QBR deck prepared
- [ ] Success metrics vs targets analyzed
- [ ] ROI calculation completed
- [ ] Roadmap preview prepared
- [ ] Expansion proposal drafted (if applicable)
- [ ] Reference/case study ask prepared
- [ ] Renewal discussion points prepared

### QBR Agenda (60 min)
- [ ] Partnership recap (5 min)
- [ ] Success metrics review (15 min)
- [ ] ROI and business impact (10 min)
- [ ] Roadmap and upcoming features (10 min)
- [ ] QUESTION: What are your priorities for next quarter?
- [ ] Expansion discussion (10 min)
- [ ] Action items and next steps (10 min)

### Post-QBR
- [ ] QBR summary sent to customer
- [ ] Action items tracked
- [ ] Expansion opportunities logged in CRM
- [ ] Reference/case study follow-up sent
- [ ] Next QBR scheduled

## Checklist: Ongoing Health Monitoring

### Product Health (Weekly)
- [ ] DAU/WAU/MAU trends tracked
- [ ] Feature adoption depth measured
- [ ] Session duration monitored
- [ ] Error rates checked
- [ ] Performance metrics reviewed

### Support Health (Weekly)
- [ ] Ticket volume trend analyzed
- [ ] Resolution time measured
- [ ] Sentiment monitored
- [ ] Repeat issues identified
- [ ] Self-service ratio tracked

### Relationship Health (Monthly)
- [ ] Meeting attendance tracked
- [ ] Response times measured
- [ ] NPS/CSAT scores collected
- [ ] Stakeholder changes noted
- [ ] Expansion signals identified

### Business Health (Quarterly)
- [ ] Value metrics vs targets
- [ ] ROI realized
- [ ] Renewal likelihood assessed
- [ ] Expansion potential evaluated
- [ ] Reference-ability confirmed

## Checklist: Expansion Triggers

- [ ] High adoption (>80% WAU) → Ready for more seats
- [ ] Power users identified → Ready for advanced features
- [ ] Business growth signals → Ready for additional use cases
- [ ] Positive sentiment (NPS >50) → Ready for referral/case study
- [ ] Contract renewal approaching → Expansion conversation

## Checklist: Renewal Preparation (60 days before)

- [ ] Usage and adoption summary prepared
- [ ] Value delivered documented
- [ ] Renewal proposal drafted
- [ ] Expansion options included
- [ ] Pricing confirmed
- [ ] Stakeholder alignment confirmed
- [ ] Renewal meeting scheduled
- [ ] Contract sent for signature

================================================================================
RETROSPECTIVE TEMPLATE
================================================================================

## To be completed at end of each onboarding

### What Went Well
- [ ] QUESTION: What worked that we should repeat?
- [ ] QUESTION: What made the customer successful?
- [ ] QUESTION: What automation saved time?

### What Could Be Improved
- [ ] QUESTION: Where did we struggle?
- [ ] QUESTION: What took longer than expected?
- [ ] QUESTION: What did the customer complain about?

### Action Items for Process Improvement
- [ ] Update playbook based on learnings
- [ ] Share insights with team
- [ ] Update templates/resources
- [ ] Escalate systemic issues

### Metrics Summary
- [ ] Time-to-First-Value: ___ days (target: <14)
- [ ] Time-to-Go-Live: ___ days (target: segment-based)
- [ ] Training Completion: ___% (target: >85%)
- [ ] Go-Live CSAT: ___/5 (target: >4.5)
- [ ] Day 90 NPS: ___ (target: >50)
- [ ] Health Score: ___ (target: >75)

================================================================================
AUTOMATION TRIGGERS (Configure in Playbooks Settings)
================================================================================

## When Run Starts
- Create channel: onboarding-{{customer}}
- Invite members: @cs-team, @implementation
- Post welcome message with run link
- Create Jira epic: "Onboarding: {{customer}}"
- Send Slack/email notification to CS Manager

## When Task Completed: "Kickoff meeting completed"
- Post to channel: "Kickoff complete!"
- Update Jira epic status
- Trigger Phase 2 task assignments

## When Task Overdue (>48 hours)
- @mention task owner in channel
- After 24 more hours: notify CS Manager
- After 48 more hours: notify CS Leadership

## When Phase Completed
- Post phase summary to channel
- Send stakeholder notification
- Update CRM customer record
- Trigger next phase timeline

## When Status Update Due (Weekly)
- Auto-post status update request
- Include health score and open tasks
- Tag run owner

## When Health Score < 75
- Alert CS Manager immediately
- Create risk ticket in Jira
- Add to at-risk review queue

## When Run Completed (Go-Live)
- Post celebration message
- Send CSAT survey
- Schedule Day 30 check-in
- Trigger steady-state monitoring
- Request testimonial (after 30 days)

================================================================================
STATUS UPDATE TEMPLATE
================================================================================

## Weekly Status Update

**Customer:** {{CustomerName}}
**Week:** {{WeekNumber}}
**Health Score:** {{HealthScore}} (🟢/🟡/🔴)

### Progress This Week
- Completed: [list tasks]
- In Progress: [list tasks]

### Blockers/Risks
- [List any blockers]
- [List any risks]

### Customer Sentiment
- [Brief note on customer mood/feedback]

### Next Week Focus
- [Priority 1]
- [Priority 2]
- [Priority 3]

### Needs Attention
- [Any escalations or asks]

================================================================================
END OF PLAYBOOK TEMPLATE
================================================================================
