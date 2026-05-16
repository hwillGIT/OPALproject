/**
 * Persona Router - Routes messages to the appropriate GTM persona
 *
 * Routing priority:
 * 1. Explicit command: !strategist, !finance, !growth, !sales, !product, !compliance, !ops
 * 2. Channel mapping (config-driven)
 * 3. @mention with role: "@gtm strategist", "@gtm finance"
 * 4. Topic detection (keyword patterns)
 * 5. Default: strategist
 *
 * Each persona carries `tier` and `department` metadata so future
 * routing rules can fire on those (e.g. "for any strategic question
 * in #leadership, default to Board of Advisors first, Core Team
 * second"). The taxonomy is documented in
 * `bots/shared/personas/DEPARTMENTS.md`. Productive-tensions pairings
 * live in `bots/shared/personas/TENSIONS.md`.
 *
 * Validation: `node bots/gtm/scripts/validate-personas.js` enforces
 * router-vs-DEPARTMENTS consistency.
 */

import personaManager from 'bots-shared/persona-manager.js';

// Persona metadata + tier/department vocabulary live in a sibling
// file with zero external imports, so the standalone validator
// (bots/gtm/scripts/validate-personas.js) can load them without
// pulling in the workspace `bots-shared` dependency.
import {
  TIERS,
  DEPARTMENTS,
  PERSONAS as PERSONA_METADATA,
} from './persona-metadata.js';

export { TIERS, DEPARTMENTS };

// Re-bound to the local name so the rest of this file (route(),
// getPersona(), etc.) keeps reading from `PERSONAS` unchanged.
const PERSONAS = PERSONA_METADATA;

// Topic keywords for automatic persona detection
const TOPIC_PATTERNS = {
  strategist: [
    'competitive', 'positioning', 'market entry', 'strategic', 'differentiation',
    'moat', 'vision', 'blue ocean', 'swot', 'porter', 'tam', 'sam', 'som',
    'market size', 'market share', 'first mover', 'platform strategy',
  ],
  'product-owner': [
    'feature', 'roadmap', 'user story', 'backlog', 'sprint', 'mvp', 'prototype',
    'esp32', 'firmware', 'beta', 'acceptance criteria', 'rice', 'moscow',
    'product-market fit', 'pmf', 'amoled', 'user experience', 'ux',
  ],
  'growth-lead': [
    'launch', 'campaign', 'marketing', 'acquisition', 'funnel', 'content',
    'social media', 'crowdfunding', 'kickstarter', 'community', 'developer relations',
    'seo', 'pr', 'press', 'influencer', 'cac', 'conversion',
  ],
  'sales-bd': [
    'pipeline', 'deal', 'partnership', 'distributor', 'oem', 'prospect',
    'outreach', 'close', 'contract', 'pricing', 'volume', 'wholesale',
    'b2b', 'enterprise', 'procurement', 'rfp', 'rfi',
  ],
  'finance-analyst': [
    'revenue', 'cost', 'margin', 'fundraising', 'investor', 'valuation',
    'burn', 'runway', 'bom', 'unit economics', 'cogs', 'ltv',
    'financial model', 'p&l', 'cash flow', 'series a', 'seed',
  ],
  'compliance-ops': [
    'fcc', 'ce mark', 'certification', 'legal', 'patent',
    'supply chain', 'manufacturing', 'quality', 'rohs', 'ul', 'iec',
    'shipping', 'customs', 'export', 'fulfillment', 'yield',
  ],

  // === TECHNICAL SUB-TEAM ===

  'software-architect': [
    'architecture', 'api design', 'system design', 'microservice', 'monolith',
    'database', 'scalability', 'latency', 'rtos', 'firmware', 'embedded',
    'code review', 'technical debt', 'refactor', 'ci cd', 'devops',
  ],
  'enterprise-architect': [
    'hl7', 'fhir', 'ehr', 'emr', 'epic', 'cerner', 'meditech', 'allscripts',
    'interoperability', 'adt', 'orm', 'oru', 'patient matching', 'mpi',
    'smart on fhir', 'carequality', 'commonwell', 'hie',
  ],
  'security-architect': [
    'hipaa', 'security', 'privacy', 'encryption', 'authentication', 'authorization',
    'audit log', 'phi', 'breach', 'vulnerability', 'penetration', 'soc 2',
    'hitrust', 'access control', 'zero trust', 'key management',
  ],
  'cloud-architect': [
    'aws', 'azure', 'gcp', 'cloud', 'infrastructure', 'kubernetes', 'docker',
    'serverless', 'lambda', 'terraform', 'iac', 'disaster recovery', 'ha',
    'availability', 'sla', 'cost optimization', 'finops', 'baa',
  ],
  'healthcare-analyst': [
    'healthcare market', 'epic market', 'cerner market', 'ehr vendor', 'competitor',
    'market share', 'incumbent', 'acquisition', 'funding round', 'digital health',
    'telehealth', 'remote monitoring', 'population health', 'value based care',
  ],
  'clinical-advisor': [
    'clinical workflow', 'clinician', 'physician', 'nurse', 'patient',
    'bedside', 'clinical validation', 'clinical evidence', 'alert fatigue',
    'clinical decision support', 'patient safety', 'patient outcome',
  ],
  'ml-engineer': [
    'machine learning', 'model', 'inference', 'training', 'edge ai', 'tinyml',
    'tensorflow', 'quantization', 'pruning', 'mlops', 'dataset', 'labeling',
    'accuracy', 'precision', 'recall', 'bias', 'federated learning',
  ],
  'regulatory-affairs': [
    'fda', '510k', 'de novo', 'pma', 'samd', 'software as medical device',
    'presubmission', 'clinical trial', 'predicate', 'classification',
    'post-market', 'qms', 'mdr', 'ce marking medical', 'notified body',
  ],

  // === HARDWARE & DESIGN ===

  'hardware-lead': [
    'firmware', 'pcb', 'i2c', 'i2s', 'spi', 'adc', 'esp32', 'esp-idf', 'esp-adf',
    'ota', 'audio codec', 'es8311', 'pull-up', 'battery', 'lipo', 'wearable hardware',
    'antenna', 'thermal', 'power budget', 'low power', 'sleep mode', 'signal integrity',
  ],
  'industrial-designer': [
    'industrial design', 'form factor', 'ergonomic', 'ergonomics', 'anthropometric',
    'wearable design', 'enclosure', 'mould', 'moulding', 'finish', 'haptic',
    'led placement', 'audio aperture', 'wear test', 'fit', 'comfort', 'tactile',
  ],
  'ui-ux-expert': [
    'dashboard', 'ux', 'ui', 'design system', 'figma', 'wireframe', 'mockup',
    'accessibility', 'wcag', 'screen', 'flow', 'companion app', 'admin console',
    'on-screen', 'hud', 'visual hierarchy', 'usability test',
  ],
  'reliability-engineer': [
    'reliability', 'fmea', 'failure mode', 'incident', 'post-mortem', 'postmortem',
    'sla', 'slo', 'error budget', 'mtbf', 'mttr', 'blast radius', 'rollback',
    'feature flag', 'observability', 'telemetry', 'alerting', 'iec 62366', 'iso 14971',
  ],

  // === HEALTHCARE & CLINICAL (PR 3) ===

  'clinical-ops': [
    'pilot', 'pilot site', 'deployment', 'site selection', 'clinical champion',
    'irb', 'baa', 'procurement', 'training', 'change management', 'go-live',
    'site readiness', 'pilot kickoff', 'week-one',
  ],

  // === BOARD OF ADVISORS (PR 3) ===

  'cmo-advisor': [
    'cmo', 'chief medical officer', 'medical leadership', 'medical staff',
    'executive sponsor', 'hcahps', 'cms quality', 'value based care',
    'readmission', 'length of stay', 'malpractice exposure', 'rn turnover',
    'board reportable', 'amc', 'community hospital',
  ],
  'ip-counsel': [
    'patent', 'ip', 'claim', 'prior art', 'uspto', 'epo', 'pct',
    'freedom to operate', 'fto', 'defensive publication', 'trade secret',
    'file history', 'claim construction', 'alice', 'doctrine of equivalents',
    'design around',
  ],

  // === GO-TO-MARKET & PARTNERSHIPS (PR 3) ===

  'partnership-lead': [
    'partnership', 'alliance', 'app orchard', 'oem', 'white-label', 'co-sell',
    'rev share', 'channel', 'integration partner', 'master service agreement',
    'msa', 'mfn', 'exclusivity', 'system contract',
  ],

  // === FINANCE & OPERATIONS (PR 3) ===

  cfo: [
    'cfo', 'runway', 'term sheet', 'cap table', 'dilution', 'liquidation preference',
    'preferred', 'series a', 'series b', 'pre-money', 'post-money', 'fundraise',
    'bridge round', 'board reporting', 'investor update', 'sbir', 'sttr',
  ],
  'manufacturing-ops': [
    'manufacturing', 'supplier', 'contract manufacturer', 'bom', 'dfm', 'dfa',
    'tooling', 'mould tooling', 'yield', 'moq', 'lead time', 'consignment',
    'iso 13485', 'inventory', 'second source', 'single source',
  ],
};

// Channel-to-persona mapping (configured in config.json, set at init)
let channelPersonaMap = {};

/**
 * Initialize the router with channel mappings from config.
 */
export function init(config = {}) {
  channelPersonaMap = config.channelPersonaMap || {};
}

/**
 * Route a message to the appropriate persona.
 *
 * @param {string} text - Message text
 * @param {string} channelId - Channel where the message was sent
 * @param {Object} [options] - Additional context
 * @returns {{ persona: Object, reason: string, strippedText: string }}
 */
export function route(text, channelId, options = {}) {
  const lower = text.toLowerCase().trim();

  // 1. Explicit command
  for (const [key, def] of Object.entries(PERSONAS)) {
    for (const cmd of def.commands) {
      if (lower.startsWith(cmd)) {
        const strippedText = text.slice(cmd.length).trim();
        return {
          persona: def,
          reason: `command:${cmd}`,
          strippedText: strippedText || text,
        };
      }
    }
  }

  // 2. Channel mapping
  if (channelPersonaMap[channelId] && PERSONAS[channelPersonaMap[channelId]]) {
    return {
      persona: PERSONAS[channelPersonaMap[channelId]],
      reason: `channel:${channelId}`,
      strippedText: text,
    };
  }

  // 3. @mention with role (e.g., "@gtm strategist" or "strategist,")
  for (const [key, def] of Object.entries(PERSONAS)) {
    for (const pattern of def.mentionPatterns) {
      // Match patterns like "strategist" or "@gtm strategist" near the start
      const mentionRegex = new RegExp(`(?:@gtm[- ])?${pattern}[,:]?\\s`, 'i');
      if (mentionRegex.test(lower.slice(0, 50))) {
        const strippedText = text.replace(mentionRegex, '').trim();
        return {
          persona: def,
          reason: `mention:${pattern}`,
          strippedText: strippedText || text,
        };
      }
    }
  }

  // 4. Topic detection (score-based)
  const scores = {};
  for (const [key, patterns] of Object.entries(TOPIC_PATTERNS)) {
    scores[key] = patterns.filter(p => lower.includes(p)).length;
  }

  const maxScore = Math.max(...Object.values(scores));
  if (maxScore > 0) {
    const topPersona = Object.entries(scores).find(([, score]) => score === maxScore)?.[0];
    if (topPersona && PERSONAS[topPersona]) {
      return {
        persona: PERSONAS[topPersona],
        reason: `topic:${topPersona} (score:${maxScore})`,
        strippedText: text,
      };
    }
  }

  // 5. Default: strategist
  return {
    persona: PERSONAS.strategist,
    reason: 'default',
    strippedText: text,
  };
}

/**
 * Get a persona definition by key.
 */
export function getPersona(key) {
  return PERSONAS[key] || null;
}

/**
 * Get all persona definitions.
 */
export function getAllPersonas() {
  return { ...PERSONAS };
}

/**
 * Load the full persona markdown content for a given persona key.
 */
export function loadPersonaContent(key) {
  const def = PERSONAS[key];
  if (!def) return null;
  return personaManager.getBotPersona(def.personaFile);
}

/**
 * Build a system prompt for a specific persona.
 */
export function buildSystemPrompt(personaKey, options = {}) {
  const persona = loadPersonaContent(personaKey);
  if (!persona) return '';

  const parts = [];

  if (persona.core) {
    parts.push(`## Identity\n${persona.core}`);
  }
  if (persona.traits && persona.traits.length > 0) {
    parts.push(`## Traits\n${persona.traits.map(t => `- ${t}`).join('\n')}`);
  }
  if (persona.style) {
    parts.push(`## Communication Style\n${persona.style}`);
  }
  if (persona.expertise && persona.expertise.length > 0) {
    parts.push(`## Domain Expertise\n${persona.expertise.map(e => `- ${e}`).join('\n')}`);
  }
  if (persona.guidelines) {
    parts.push(`## Guidelines\n${persona.guidelines}`);
  }

  if (options.additionalContext) {
    parts.push(options.additionalContext);
  }

  return parts.join('\n\n');
}

/**
 * List all available persona keys.
 */
export function listPersonaKeys() {
  return Object.keys(PERSONAS);
}

export default {
  init,
  route,
  getPersona,
  getAllPersonas,
  loadPersonaContent,
  buildSystemPrompt,
  listPersonaKeys,
  PERSONAS,
};
