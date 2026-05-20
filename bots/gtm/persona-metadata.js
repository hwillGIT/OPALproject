/**
 * Persona metadata — single source of truth for tiers, departments,
 * and persona definitions.
 *
 * This file has ZERO external imports so it can be loaded by:
 *   - persona-router.js (the live router, with workspace deps)
 *   - validate-personas.js (the standalone validator, run as plain Node)
 *   - any future tooling that needs persona metadata without bringing
 *     in the bot infrastructure
 *
 * Rule of thumb: if you add an `import` to this file, you've broken
 * the standalone validator. Don't.
 *
 * The roster, tier mapping, and department mapping are documented
 * for humans in `bots/shared/personas/DEPARTMENTS.md` — that file
 * and this one MUST agree (`validate-personas.js` enforces it).
 */

/**
 * Valid tier values. Adding a new tier requires updating
 * DEPARTMENTS.md and the validator.
 */
export const TIERS = Object.freeze([
  'board-of-advisors',
  'core-team',
]);

/**
 * Valid department values. Board-of-advisors personas have
 * `department: null`. Adding a new department requires updating
 * DEPARTMENTS.md and the validator.
 */
export const DEPARTMENTS = Object.freeze([
  'Strategy & Leadership',
  'Engineering & Platform',
  'Hardware & Design',
  'Healthcare & Clinical',
  'Go-to-Market & Partnerships',
  'Finance & Operations',
]);

/**
 * Persona definitions with routing metadata.
 *
 * Required keys per persona:
 *   key, personaFile, name, label, tier, department,
 *   domains, emits, commands, mentionPatterns
 *
 * For board-of-advisors personas, department MUST be null.
 * For core-team personas, department MUST be one of DEPARTMENTS.
 */
export const PERSONAS = {
  strategist: {
    key: 'strategist',
    personaFile: 'gtm/strategist',
    name: 'Athena',
    label: 'Strategist',
    tier: 'core-team',
    department: 'Strategy & Leadership',
    domains: ['strategy'],
    emits: ['INSIGHT', 'PREDICTION', 'CONTEXT_CHANGE'],
    commands: ['!strategist', '!strategy', '!athena'],
    mentionPatterns: ['strategist', 'strategy', 'athena'],
  },
  'product-owner': {
    key: 'product-owner',
    personaFile: 'gtm/product-owner',
    name: 'Priya',
    label: 'Product Owner',
    tier: 'core-team',
    department: 'Strategy & Leadership',
    domains: ['product'],
    emits: ['DECISION', 'ACTION', 'ARTIFACT'],
    commands: ['!product', '!product-owner', '!priya', '!po'],
    mentionPatterns: ['product', 'product owner', 'priya', 'po'],
  },
  'growth-lead': {
    key: 'growth-lead',
    personaFile: 'gtm/growth-lead',
    name: 'Maya',
    label: 'Growth Lead',
    tier: 'core-team',
    department: 'Go-to-Market & Partnerships',
    domains: ['gtm'],
    emits: ['ACTION', 'PREDICTION', 'ARTIFACT'],
    commands: ['!growth', '!marketing', '!gtm', '!maya'],
    mentionPatterns: ['growth', 'marketing', 'gtm', 'maya', 'launch'],
  },
  'sales-bd': {
    key: 'sales-bd',
    personaFile: 'gtm/sales-bd',
    name: 'Rex',
    label: 'Sales & BD',
    tier: 'core-team',
    department: 'Go-to-Market & Partnerships',
    domains: ['gtm', 'operations'],
    emits: ['ACTION', 'INSIGHT', 'PREDICTION'],
    commands: ['!sales', '!bd', '!rex', '!deals'],
    mentionPatterns: ['sales', 'bd', 'business development', 'rex', 'pipeline', 'deal'],
  },
  'finance-analyst': {
    key: 'finance-analyst',
    personaFile: 'gtm/finance-analyst',
    name: 'Kai',
    label: 'Finance Analyst',
    tier: 'core-team',
    department: 'Finance & Operations',
    domains: ['finance'],
    emits: ['INSIGHT', 'PREDICTION', 'ARTIFACT'],
    commands: ['!finance', '!kai', '!budget', '!runway'],
    mentionPatterns: ['finance', 'kai', 'budget', 'runway', 'investor', 'fundrais'],
  },
  'compliance-ops': {
    key: 'compliance-ops',
    personaFile: 'gtm/compliance-ops',
    name: 'Suki',
    label: 'Compliance & Ops',
    tier: 'core-team',
    department: 'Go-to-Market & Partnerships',
    domains: ['compliance', 'operations'],
    emits: ['INSIGHT', 'ACTION', 'CONTEXT_CHANGE'],
    commands: ['!compliance', '!ops', '!suki', '!legal'],
    mentionPatterns: ['compliance', 'ops', 'operations', 'suki', 'fcc', 'legal', 'supply chain'],
  },

  // === TECHNICAL SUB-TEAM ===

  'software-architect': {
    key: 'software-architect',
    personaFile: 'gtm/software-architect',
    name: 'Marcus',
    label: 'Software Architect',
    tier: 'core-team',
    department: 'Engineering & Platform',
    domains: ['engineering'],
    emits: ['INSIGHT', 'DECISION', 'ARTIFACT'],
    commands: ['!software', '!architect', '!marcus', '!code'],
    mentionPatterns: ['software', 'architect', 'marcus', 'api', 'architecture', 'system design'],
  },
  'enterprise-architect': {
    key: 'enterprise-architect',
    personaFile: 'gtm/enterprise-architect',
    name: 'Helena',
    label: 'Enterprise Architect (Healthcare)',
    tier: 'core-team',
    department: 'Healthcare & Clinical',
    domains: ['healthcare-systems'],
    emits: ['INSIGHT', 'DECISION', 'ARTIFACT'],
    commands: ['!enterprise', '!ehr', '!fhir', '!hl7', '!helena'],
    mentionPatterns: ['enterprise', 'ehr', 'emr', 'fhir', 'hl7', 'helena', 'epic', 'cerner', 'integration'],
  },
  'security-architect': {
    key: 'security-architect',
    personaFile: 'gtm/security-architect',
    name: 'Cyrus',
    label: 'Security & Privacy Architect',
    tier: 'core-team',
    department: 'Engineering & Platform',
    domains: ['security'],
    emits: ['INSIGHT', 'ACTION', 'GAP'],
    commands: ['!security', '!hipaa', '!privacy', '!cyrus'],
    mentionPatterns: ['security', 'hipaa', 'privacy', 'cyrus', 'encryption', 'authentication', 'breach'],
  },
  'cloud-architect': {
    key: 'cloud-architect',
    personaFile: 'gtm/cloud-architect',
    name: 'Nimbus',
    label: 'Cloud Architect',
    tier: 'core-team',
    department: 'Engineering & Platform',
    domains: ['infrastructure'],
    emits: ['INSIGHT', 'DECISION', 'ARTIFACT'],
    commands: ['!cloud', '!infra', '!infrastructure', '!nimbus', '!aws', '!azure', '!gcp'],
    mentionPatterns: ['cloud', 'infrastructure', 'nimbus', 'aws', 'azure', 'gcp', 'kubernetes', 'serverless'],
  },
  'healthcare-analyst': {
    key: 'healthcare-analyst',
    personaFile: 'gtm/healthcare-analyst',
    name: 'Vera',
    label: 'Healthcare Industry Analyst',
    tier: 'board-of-advisors',
    department: null,
    domains: ['healthcare-industry'],
    emits: ['INSIGHT', 'PREDICTION', 'CONTEXT_CHANGE'],
    commands: ['!healthcare', '!industry', '!vera', '!market-intel'],
    mentionPatterns: ['healthcare', 'vera', 'epic', 'cerner', 'vendor', 'incumbent', 'market intel'],
  },
  'clinical-advisor': {
    key: 'clinical-advisor',
    personaFile: 'gtm/clinical-advisor',
    name: 'Dr. Claire',
    label: 'Clinical Advisor',
    tier: 'board-of-advisors',
    department: null,
    domains: ['clinical'],
    emits: ['INSIGHT', 'GAP', 'DECISION'],
    commands: ['!clinical', '!claire', '!doctor', '!clinician'],
    mentionPatterns: ['clinical', 'claire', 'doctor', 'clinician', 'nurse', 'physician', 'patient', 'workflow'],
  },
  'ml-engineer': {
    key: 'ml-engineer',
    personaFile: 'gtm/ml-engineer',
    name: 'Tensor',
    label: 'ML/AI Engineer',
    tier: 'core-team',
    department: 'Engineering & Platform',
    domains: ['ai-ml'],
    emits: ['INSIGHT', 'DECISION', 'ARTIFACT'],
    commands: ['!ml', '!ai', '!tensor', '!model'],
    mentionPatterns: ['ml', 'machine learning', 'ai', 'tensor', 'model', 'inference', 'training', 'edge ai'],
  },
  'regulatory-affairs': {
    key: 'regulatory-affairs',
    personaFile: 'gtm/regulatory-affairs',
    name: 'Regina',
    label: 'Regulatory Affairs Specialist',
    tier: 'core-team',
    department: 'Healthcare & Clinical',
    domains: ['regulatory'],
    emits: ['INSIGHT', 'ACTION', 'GAP'],
    commands: ['!fda', '!510k', '!regina', '!regulatory-affairs', '!samd'],
    mentionPatterns: ['fda', '510k', 'de novo', 'regina', 'samd', 'clearance', 'submission', 'mdr'],
  },

  // === HARDWARE & DESIGN (PR 3) ===

  'hardware-lead': {
    key: 'hardware-lead',
    personaFile: 'gtm/hardware-lead',
    name: 'Diego',
    label: 'Hardware Lead',
    tier: 'core-team',
    department: 'Hardware & Design',
    domains: ['hardware', 'firmware'],
    emits: ['INSIGHT', 'DECISION', 'ARTIFACT', 'GAP'],
    commands: ['!hardware', '!firmware', '!diego', '!esp32'],
    mentionPatterns: ['hardware', 'firmware', 'diego', 'esp32', 'pcb', 'i2c', 'ota', 'codec'],
  },
  'industrial-designer': {
    key: 'industrial-designer',
    personaFile: 'gtm/industrial-designer',
    name: 'Yuki',
    label: 'Industrial Designer',
    tier: 'core-team',
    department: 'Hardware & Design',
    domains: ['industrial-design'],
    emits: ['INSIGHT', 'DECISION', 'ARTIFACT', 'GAP'],
    commands: ['!id', '!industrial-design', '!yuki', '!form-factor'],
    mentionPatterns: ['industrial design', 'form factor', 'ergonomic', 'wearable design', 'yuki', 'enclosure'],
  },
  'ui-ux-expert': {
    key: 'ui-ux-expert',
    personaFile: 'gtm/ui-ux-expert',
    name: 'Sasha',
    label: 'UI/UX Expert',
    tier: 'core-team',
    department: 'Hardware & Design',
    domains: ['ux', 'ui', 'design-system'],
    emits: ['INSIGHT', 'DECISION', 'ARTIFACT', 'GAP'],
    commands: ['!ux', '!ui', '!sasha', '!design'],
    mentionPatterns: ['ux', 'ui', 'sasha', 'dashboard', 'screen', 'design system', 'figma', 'wireframe', 'accessibility'],
  },
  'reliability-engineer': {
    key: 'reliability-engineer',
    personaFile: 'gtm/reliability-engineer',
    name: 'Bjorn',
    label: 'Reliability Engineer',
    tier: 'core-team',
    department: 'Hardware & Design',
    domains: ['reliability', 'safety'],
    emits: ['INSIGHT', 'GAP', 'ACTION', 'DECISION'],
    commands: ['!reliability', '!fmea', '!bjorn', '!safety'],
    mentionPatterns: ['reliability', 'fmea', 'bjorn', 'failure mode', 'incident', 'post-mortem', 'sla', 'mtbf'],
  },

  // === HEALTHCARE & CLINICAL (PR 3) ===

  'clinical-ops': {
    key: 'clinical-ops',
    personaFile: 'gtm/clinical-ops',
    name: 'Imani',
    label: 'Clinical Operations / Pilot Manager',
    tier: 'core-team',
    department: 'Healthcare & Clinical',
    domains: ['clinical-ops', 'pilots', 'deployment'],
    emits: ['INSIGHT', 'ACTION', 'OUTCOME', 'CONTEXT_CHANGE'],
    commands: ['!pilot', '!clinical-ops', '!imani', '!deployment'],
    mentionPatterns: ['pilot', 'clinical ops', 'imani', 'deployment', 'site', 'champion', 'irb', 'baa'],
  },

  // === BOARD OF ADVISORS (PR 3) ===

  'cmo-advisor': {
    key: 'cmo-advisor',
    personaFile: 'gtm/cmo-advisor',
    name: 'Dr. Devon',
    label: 'CMO Advisor',
    tier: 'board-of-advisors',
    department: null,
    domains: ['clinical-executive'],
    emits: ['INSIGHT', 'GAP', 'DECISION'],
    commands: ['!cmo', '!devon', '!exec-clinical'],
    mentionPatterns: ['cmo', 'devon', 'chief medical', 'medical leadership', 'executive sponsor', 'hcahps', 'value based care'],
  },
  'ip-counsel': {
    key: 'ip-counsel',
    personaFile: 'gtm/ip-counsel',
    name: 'Adriana',
    label: 'IP Counsel',
    tier: 'board-of-advisors',
    department: null,
    domains: ['ip', 'patent', 'legal'],
    emits: ['INSIGHT', 'GAP', 'DECISION', 'CONTEXT_CHANGE'],
    commands: ['!ip', '!patent', '!adriana', '!claim'],
    mentionPatterns: ['patent', 'ip', 'adriana', 'claim', 'prior art', 'uspto', 'freedom to operate', 'fto', 'defensive publication'],
  },

  // === GO-TO-MARKET & PARTNERSHIPS (PR 3) ===

  'partnership-lead': {
    key: 'partnership-lead',
    personaFile: 'gtm/partnership-lead',
    name: 'Wei',
    label: 'Partnership Lead',
    tier: 'core-team',
    department: 'Go-to-Market & Partnerships',
    domains: ['partnerships', 'channels'],
    emits: ['ACTION', 'DECISION', 'PREDICTION', 'ARTIFACT'],
    commands: ['!partnership', '!wei', '!alliance', '!app-orchard'],
    mentionPatterns: ['partnership', 'wei', 'app orchard', 'alliance', 'oem', 'channel', 'integration partner'],
  },

  // === FINANCE & OPERATIONS (PR 3) ===

  cfo: {
    key: 'cfo',
    personaFile: 'gtm/cfo',
    name: 'Naomi',
    label: 'CFO',
    tier: 'core-team',
    department: 'Finance & Operations',
    domains: ['finance', 'capital', 'fundraising'],
    emits: ['INSIGHT', 'DECISION', 'PREDICTION', 'ARTIFACT'],
    commands: ['!cfo', '!naomi', '!runway', '!term-sheet'],
    mentionPatterns: ['cfo', 'naomi', 'runway', 'term sheet', 'cap table', 'dilution', 'liquidation preference', 'series a', 'fundraise'],
  },
  'manufacturing-ops': {
    key: 'manufacturing-ops',
    personaFile: 'gtm/manufacturing-ops',
    name: 'Ramon',
    label: 'Manufacturing Operations',
    tier: 'core-team',
    department: 'Finance & Operations',
    domains: ['manufacturing', 'supply-chain'],
    emits: ['INSIGHT', 'ACTION', 'DECISION', 'ARTIFACT'],
    commands: ['!manufacturing', '!ramon', '!supplier', '!bom', '!dfm'],
    mentionPatterns: ['manufacturing', 'ramon', 'supplier', 'bom', 'dfm', 'tooling', 'yield', 'moq', 'lead time'],
  },
};

/**
 * Convenience accessor — returns a shallow clone of PERSONAS so
 * callers can iterate without risk of mutating the canonical object.
 */
export function getAllPersonaMetadata() {
  return { ...PERSONAS };
}
