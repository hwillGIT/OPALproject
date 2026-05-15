#!/usr/bin/env node
/**
 * Persona metadata validator (PR 1 of the agent-topology epic).
 *
 * Checks that bots/gtm/persona-router.js carries valid `tier` and
 * `department` metadata for every persona, and that the assignments
 * line up with bots/shared/personas/DEPARTMENTS.md.
 *
 * Usage:
 *   node bots/gtm/scripts/validate-personas.js
 *
 * Exits 0 on success, 1 on any check failure. Prints a summary plus
 * any specific failures with file:line context.
 *
 * Why a script and not Jest/Vitest: the bots workspace has no test
 * framework today. This file acts as the test harness for now and
 * can be wired into CI as a single npm/node command. PR 2 may
 * introduce a real test runner if multiple scripts accumulate.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// Imports go to persona-metadata.js (zero external deps) so this
// script runs as plain Node without `npm install` in the workspace.
import {
  TIERS,
  DEPARTMENTS,
  getAllPersonaMetadata,
} from '../persona-metadata.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const REPO_ROOT = path.resolve(__dirname, '..', '..', '..');
const DEPARTMENTS_MD = path.join(
  REPO_ROOT, 'bots', 'shared', 'personas', 'DEPARTMENTS.md',
);

// --------------------------------------------------------------------------
// Pure check helpers
// --------------------------------------------------------------------------

/**
 * Validate that every persona has a non-empty `name`, `key`, `label`,
 * `tier`, and (for core-team) `department`. Returns an array of
 * human-readable failure strings.
 */
export function checkPersonaShape(personas) {
  const failures = [];
  for (const [key, p] of Object.entries(personas)) {
    if (!p.key) failures.push(`persona '${key}': missing 'key'`);
    if (!p.name) failures.push(`persona '${key}': missing 'name'`);
    if (!p.label) failures.push(`persona '${key}': missing 'label'`);
    if (!p.tier) {
      failures.push(`persona '${key}': missing 'tier'`);
      continue;
    }
    if (!TIERS.includes(p.tier)) {
      failures.push(
        `persona '${key}': invalid tier '${p.tier}' ` +
        `(allowed: ${TIERS.join(', ')})`,
      );
    }
    if (p.tier === 'board-of-advisors') {
      if (p.department !== null && p.department !== undefined) {
        failures.push(
          `persona '${key}' (advisor): expected department=null, ` +
          `got '${p.department}'`,
        );
      }
    } else {
      if (!p.department) {
        failures.push(
          `persona '${key}' (${p.tier}): missing 'department'`,
        );
      } else if (!DEPARTMENTS.includes(p.department)) {
        failures.push(
          `persona '${key}': invalid department '${p.department}' ` +
          `(allowed: ${DEPARTMENTS.join(', ')})`,
        );
      }
    }
  }
  return failures;
}

/**
 * Extract persona names that are listed under each department in
 * DEPARTMENTS.md. Returns { advisorNames: Set<string>,
 * deptToNames: Map<string, Set<string>> }.
 *
 * Parsing strategy: walk the markdown line-by-line, track the
 * current department/tier from `## Tier N` and `### N. Name`
 * headings, and pull `**Name**` from each table row.
 */
export function parseDepartmentsMd(text) {
  const advisorNames = new Set();
  const deptToNames = new Map();

  let inAdvisorSection = false;
  let currentDept = null;

  const lines = text.split(/\r?\n/);
  for (const line of lines) {
    const tier1 = line.match(/^## Tier 1: Board of Advisors\s*$/);
    const tier2 = line.match(/^## Tier 2: Core Team/);
    const cross = line.match(/^## Cross-Functional Bots/);
    if (tier1) {
      inAdvisorSection = true;
      currentDept = null;
      continue;
    }
    if (tier2 || cross) {
      inAdvisorSection = false;
      currentDept = null;
      continue;
    }

    // ### N. Department Name
    const deptHeader = line.match(/^### \d+\.\s+(.+?)\s*$/);
    if (deptHeader) {
      currentDept = deptHeader[1].trim();
      if (!deptToNames.has(currentDept)) {
        deptToNames.set(currentDept, new Set());
      }
      continue;
    }

    // | **Name** | Role | Status |
    const row = line.match(/^\|\s*\*\*([^*]+)\*\*\s*\|/);
    if (!row) continue;
    const name = row[1].trim();
    if (inAdvisorSection) {
      advisorNames.add(name);
    } else if (currentDept) {
      deptToNames.get(currentDept).add(name);
    }
  }
  return { advisorNames, deptToNames };
}

/**
 * Cross-check: every persona name in the router must appear in
 * DEPARTMENTS.md under the same tier+department. The Markdown roster
 * MAY include not-yet-implemented personas (marked with
 * "**new (PR 3)**" in the Status column) — those are allowed to
 * appear in the doc without a router entry.
 */
export function checkRouterDocConsistency(personas, mdText) {
  const failures = [];
  const { advisorNames, deptToNames } = parseDepartmentsMd(mdText);

  for (const [key, p] of Object.entries(personas)) {
    if (p.tier === 'board-of-advisors') {
      if (!advisorNames.has(p.name)) {
        failures.push(
          `router lists '${p.name}' (${key}) as advisor, ` +
          `but DEPARTMENTS.md has no advisor entry for that name`,
        );
      }
      continue;
    }
    const inDept = deptToNames.get(p.department);
    if (!inDept) {
      failures.push(
        `router lists '${p.name}' (${key}) in department ` +
        `'${p.department}', which DEPARTMENTS.md does not define`,
      );
      continue;
    }
    if (!inDept.has(p.name)) {
      failures.push(
        `router lists '${p.name}' (${key}) in '${p.department}', ` +
        `but DEPARTMENTS.md has no entry for that name in that department`,
      );
    }
  }
  return failures;
}

// --------------------------------------------------------------------------
// Entry point
// --------------------------------------------------------------------------

function summarize(personas) {
  const byTier = {};
  const byDept = {};
  for (const p of Object.values(personas)) {
    byTier[p.tier] = (byTier[p.tier] || 0) + 1;
    if (p.department) {
      byDept[p.department] = (byDept[p.department] || 0) + 1;
    }
  }
  return { byTier, byDept };
}

async function main() {
  const personas = getAllPersonaMetadata();
  const personaCount = Object.keys(personas).length;

  console.log(`# validate-personas — ${personaCount} personas in router`);

  let allFailures = [];

  // 1. Shape check
  const shapeFails = checkPersonaShape(personas);
  if (shapeFails.length === 0) {
    console.log('  shape: OK');
  } else {
    console.log(`  shape: FAIL (${shapeFails.length} issue(s))`);
  }
  allFailures = allFailures.concat(shapeFails);

  // 2. DEPARTMENTS.md cross-check
  if (!fs.existsSync(DEPARTMENTS_MD)) {
    allFailures.push(`DEPARTMENTS.md not found at ${DEPARTMENTS_MD}`);
    console.log('  consistency: FAIL (DEPARTMENTS.md missing)');
  } else {
    const mdText = fs.readFileSync(DEPARTMENTS_MD, 'utf-8');
    const consistencyFails = checkRouterDocConsistency(personas, mdText);
    if (consistencyFails.length === 0) {
      console.log('  consistency: OK (router <-> DEPARTMENTS.md)');
    } else {
      console.log(
        `  consistency: FAIL (${consistencyFails.length} issue(s))`,
      );
    }
    allFailures = allFailures.concat(consistencyFails);
  }

  // 3. Summary table
  const { byTier, byDept } = summarize(personas);
  console.log('\nBy tier:');
  for (const [tier, n] of Object.entries(byTier).sort()) {
    console.log(`  ${tier}: ${n}`);
  }
  console.log('\nBy department:');
  for (const [dept, n] of Object.entries(byDept).sort()) {
    console.log(`  ${dept}: ${n}`);
  }

  if (allFailures.length > 0) {
    console.log(`\n${allFailures.length} failure(s):`);
    for (const f of allFailures) console.log(`  - ${f}`);
    process.exit(1);
  }
  console.log('\nall checks passed');
  process.exit(0);
}

if (import.meta.url === `file://${process.argv[1]}` ||
    process.argv[1].endsWith('validate-personas.js')) {
  main().catch((err) => {
    console.error('validate-personas: unexpected error');
    console.error(err);
    process.exit(2);
  });
}
