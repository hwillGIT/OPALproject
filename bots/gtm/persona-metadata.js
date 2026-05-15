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
};

/**
 * Convenience accessor — returns a shallow clone of PERSONAS so
 * callers can iterate without risk of mutating the canonical object.
 */
export function getAllPersonaMetadata() {
  return { ...PERSONAS };
}
