#!/usr/bin/env node
/**
 * Workflow validator (PR 2 of the agent-topology epic).
 *
 * Validates the business workflow YAML files in
 * `bots/shared/workflows/business/`. Each file must follow the schema
 * documented in `../README.md`.
 *
 * Cross-references:
 *   - Persona keys → `bots/gtm/persona-metadata.js` (existing personas)
 *                  OR `bots/shared/personas/DEPARTMENTS.md`
 *                  (personas marked "new (PR 3)" are accepted as
 *                  known-future references)
 *   - Tension pairs → `bots/shared/personas/TENSIONS.md`
 *   - Event types in `emits:` → fixed vocabulary (see MEMORY_EVENT_TYPES)
 *   - Optional `pattern:` → an existing pattern YAML in the parent dir
 *
 * Exits 0 on success, 1 on validation failure, 2 on unexpected error.
 *
 * Zero external dependencies — bundles a tiny YAML-subset parser
 * sufficient for the controlled schema. If we ever need full YAML,
 * swap in js-yaml and require `npm install`.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

import {
  PERSONAS as PERSONA_METADATA,
} from '../../gtm/persona-metadata.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PERSONAS_DIR = path.resolve(__dirname, '..', 'personas');
const DEPARTMENTS_MD = path.join(PERSONAS_DIR, 'DEPARTMENTS.md');
const TENSIONS_MD = path.join(PERSONAS_DIR, 'TENSIONS.md');
const BUSINESS_DIR = path.join(__dirname, 'business');

const MEMORY_EVENT_TYPES = new Set([
  'DECISION', 'ACTION', 'INSIGHT', 'PREDICTION',
  'OUTCOME', 'DEBATE', 'CONTEXT_CHANGE', 'ARTIFACT',
]);

const REQUIRED_PHASE_KEYS = new Set(['id', 'lead', 'questions', 'output']);
const REQUIRED_TOP_KEYS = new Set([
  'name', 'category', 'domain', 'version',
  'description', 'backpressure', 'phases', 'emits',
]);

// --------------------------------------------------------------------------
// Minimal YAML-subset parser
// Handles ONLY the schema in bots/shared/workflows/business/*.yaml:
//   - scalar: `key: value`
//   - quoted scalar: `key: "value"` (quotes stripped)
//   - block scalar: `key: >\n  multi\n  line` (joined with spaces)
//   - list of scalars: `key:\n  - item`
//   - list of objects: `key:\n  - subkey: val\n    subkey2: val`
//   - inline list: `key: [a, b, c]`
//   - comments (#) and blank lines ignored
// --------------------------------------------------------------------------

function parseYamlSubset(text) {
  const lines = text.split(/\r?\n/);
  // Strip comments + trailing whitespace
  const cleaned = lines.map((l) => {
    const hashIdx = findUnquotedHash(l);
    const noComment = hashIdx >= 0 ? l.slice(0, hashIdx) : l;
    return noComment.replace(/\s+$/, '');
  });

  const root = {};
  let i = 0;
  while (i < cleaned.length) {
    const line = cleaned[i];
    if (!line.trim()) { i++; continue; }
    if (countIndent(line) !== 0) {
      throw new Error(`unexpected indented line at top level: line ${i + 1}: ${line}`);
    }
    const m = line.match(/^([A-Za-z_][\w-]*)\s*:\s*(.*)$/);
    if (!m) throw new Error(`malformed top-level line ${i + 1}: ${line}`);
    const key = m[1];
    const rest = m[2];
    const { value, consumed } = readValue(cleaned, i, rest, 0);
    root[key] = value;
    i += consumed;
  }
  return root;
}

function findUnquotedHash(s) {
  let inQuote = false;
  for (let j = 0; j < s.length; j++) {
    const c = s[j];
    if (c === '"' || c === "'") inQuote = !inQuote;
    else if (c === '#' && !inQuote) return j;
  }
  return -1;
}

function countIndent(s) {
  let n = 0;
  while (n < s.length && s[n] === ' ') n++;
  return n;
}

function stripQuotes(v) {
  v = v.trim();
  if ((v.startsWith('"') && v.endsWith('"')) ||
      (v.startsWith("'") && v.endsWith("'"))) {
    return v.slice(1, -1);
  }
  return v;
}

function readValue(lines, startIdx, restOfKeyLine, parentIndent) {
  // restOfKeyLine is what came after `key:` on the same line.
  if (restOfKeyLine === '>' || restOfKeyLine === '|') {
    // Block scalar
    const out = [];
    let j = startIdx + 1;
    let blockIndent = -1;
    while (j < lines.length) {
      const l = lines[j];
      if (!l.trim()) { out.push(''); j++; continue; }
      const ind = countIndent(l);
      if (blockIndent < 0) {
        if (ind <= parentIndent) break;
        blockIndent = ind;
      }
      if (ind < blockIndent) break;
      out.push(l.slice(blockIndent));
      j++;
    }
    const joiner = restOfKeyLine === '>' ? ' ' : '\n';
    return { value: out.join(joiner).trim(), consumed: j - startIdx };
  }
  if (restOfKeyLine !== '') {
    // Inline scalar OR inline list `[a, b, c]`
    if (restOfKeyLine.startsWith('[') && restOfKeyLine.endsWith(']')) {
      const inner = restOfKeyLine.slice(1, -1).trim();
      const items = inner === '' ? [] :
        inner.split(',').map((s) => stripQuotes(s.trim())).filter((s) => s !== '');
      return { value: items, consumed: 1 };
    }
    return { value: stripQuotes(restOfKeyLine), consumed: 1 };
  }
  // Multi-line: either a list or a map at greater indent.
  let j = startIdx + 1;
  while (j < lines.length && !lines[j].trim()) j++;
  if (j >= lines.length) return { value: null, consumed: j - startIdx };
  const firstChildIndent = countIndent(lines[j]);
  if (firstChildIndent <= parentIndent) {
    return { value: null, consumed: j - startIdx };
  }
  // List?
  if (lines[j].slice(firstChildIndent).startsWith('- ') ||
      lines[j].slice(firstChildIndent) === '-') {
    return readList(lines, startIdx, firstChildIndent);
  }
  // Map.
  return readMap(lines, startIdx, firstChildIndent);
}

function readList(lines, startIdx, listIndent) {
  const items = [];
  let j = startIdx + 1;
  while (j < lines.length) {
    const l = lines[j];
    if (!l.trim()) { j++; continue; }
    const ind = countIndent(l);
    if (ind < listIndent) break;
    if (ind > listIndent) {
      throw new Error(`unexpected indent in list at line ${j + 1}: ${l}`);
    }
    const stripped = l.slice(listIndent);
    if (!stripped.startsWith('- ') && stripped !== '-') {
      // sibling that isn't a list item -> list ends here
      break;
    }
    const after = stripped === '-' ? '' : stripped.slice(2);
    // List item: scalar?
    if (!/^[A-Za-z_][\w-]*\s*:/.test(after) && after !== '') {
      items.push(stripQuotes(after));
      j++;
      continue;
    }
    // List item: object. Parse a map starting from this line.
    const obj = {};
    // First key from the rest of the same line
    if (after !== '') {
      const m = after.match(/^([A-Za-z_][\w-]*)\s*:\s*(.*)$/);
      if (!m) throw new Error(`malformed list-of-object key at line ${j + 1}: ${l}`);
      const k = m[1];
      const objKeyIndent = listIndent + 2;
      const { value, consumed } = readValue(lines, j, m[2], objKeyIndent);
      obj[k] = value;
      j += consumed;
    } else {
      j++;
    }
    // Continuation keys at deeper indent
    while (j < lines.length) {
      const ll = lines[j];
      if (!ll.trim()) { j++; continue; }
      const ind2 = countIndent(ll);
      if (ind2 <= listIndent) break;
      const stripped2 = ll.slice(ind2);
      if (stripped2.startsWith('- ')) break;
      const mm = stripped2.match(/^([A-Za-z_][\w-]*)\s*:\s*(.*)$/);
      if (!mm) {
        throw new Error(`malformed object key inside list at line ${j + 1}: ${ll}`);
      }
      const k = mm[1];
      const { value, consumed } = readValue(lines, j, mm[2], ind2);
      obj[k] = value;
      j += consumed;
    }
    items.push(obj);
  }
  return { value: items, consumed: j - startIdx };
}

function readMap(lines, startIdx, mapIndent) {
  const obj = {};
  let j = startIdx + 1;
  while (j < lines.length) {
    const l = lines[j];
    if (!l.trim()) { j++; continue; }
    const ind = countIndent(l);
    if (ind < mapIndent) break;
    if (ind > mapIndent) {
      throw new Error(`unexpected indent in map at line ${j + 1}: ${l}`);
    }
    const m = l.slice(mapIndent).match(/^([A-Za-z_][\w-]*)\s*:\s*(.*)$/);
    if (!m) throw new Error(`malformed map key at line ${j + 1}: ${l}`);
    const { value, consumed } = readValue(lines, j, m[2], mapIndent);
    obj[m[1]] = value;
    j += consumed;
  }
  return { value: obj, consumed: j - startIdx };
}

// --------------------------------------------------------------------------
// Cross-reference helpers
// --------------------------------------------------------------------------

function parseDepartmentsForPlannedPersonas(mdText) {
  // Find personas marked "new (PR 3)" in the status column. Their role
  // label appears as the first **bold** in a table row. The router key
  // is derived from the role via kebab-case.
  //
  // Returns a Map(displayName -> personaKey) registering BOTH the full
  // label and the slash-prefix short form, e.g.
  //   "Hardware Lead"                  -> "hardware-lead"
  //   "Clinical Ops / Pilot Manager"   -> "clinical-ops"
  //   "Clinical Ops"                   -> "clinical-ops"  (short form)
  //
  // The dual registration lets TENSIONS.md use the short form
  // ("Clinical Ops ↔ Suki") even when DEPARTMENTS.md uses the long
  // form for the same persona.
  const planned = new Map();
  const lines = mdText.split(/\r?\n/);
  for (const line of lines) {
    if (!/new \(PR 3\)/i.test(line)) continue;
    const m = line.match(/^\|\s*\*\*([^*]+)\*\*/);
    if (!m) continue;
    const fullName = m[1].trim();
    const key = plannedRoleToKey(fullName);
    planned.set(fullName, key);
    const shortName = fullName.split(/\s+\/\s+/, 1)[0].trim();
    if (shortName && shortName !== fullName) {
      planned.set(shortName, key);
    }
  }
  return planned;
}

function plannedRoleToKey(role) {
  // For planned roles, "Clinical Ops / Pilot Manager" -> "clinical-ops"
  // (take the alternative-slash-prefix portion as the canonical key).
  // Splits only on " / " WITH spaces so compound names like "UI/UX
  // Expert" stay intact -> "ui-ux-expert".
  const head = role.split(/\s+\/\s+/, 1)[0];
  return head
    .toLowerCase()
    .replace(/\s+&\s+/g, '-')
    .replace(/\s+/g, '-')
    .replace(/\//g, '-')
    .replace(/[^a-z0-9-]/g, '')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');
}

function nameToKey(name) {
  // Generic kebab-case for raw display strings.
  return name
    .toLowerCase()
    .replace(/\s+&\s+/g, '-')
    .replace(/\s+\/\s+/g, '-')
    .replace(/[\s/]+/g, '-')
    .replace(/[^a-z0-9-]/g, '')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');
}

/**
 * Build a name -> persona-key map covering both existing personas
 * (from PERSONA_METADATA) and planned personas (from DEPARTMENTS.md).
 *
 * For existing personas: "Athena" -> "strategist".
 * For planned personas:  "Hardware Lead" -> "hardware-lead".
 */
function buildNameToKey(personaMetadata, plannedMap) {
  const m = new Map();
  for (const [key, p] of Object.entries(personaMetadata)) {
    if (p.name) m.set(p.name, key);
  }
  for (const [name, key] of plannedMap) {
    m.set(name, key);
  }
  return m;
}

function parseTensionsPairs(mdText, nameToKeyMap) {
  // Each tension pair appears in a table row as `**A ↔ B**`. We
  // resolve A and B to canonical persona-keys via nameToKeyMap.
  // Unresolvable names are skipped (they will surface as missing
  // tensions when a workflow references them).
  const pairs = new Set();
  const lines = mdText.split(/\r?\n/);
  for (const line of lines) {
    const m = line.match(/^\|\s*\*\*([^|*]+?)\s*↔\s*([^|*]+?)\*\*/);
    if (!m) continue;
    const aName = m[1].trim();
    const bName = m[2].trim();
    const aKey = nameToKeyMap.get(aName);
    const bKey = nameToKeyMap.get(bName);
    if (!aKey || !bKey) continue;
    pairs.add(`${aKey}<>${bKey}`);
    pairs.add(`${bKey}<>${aKey}`);
  }
  return pairs;
}

// --------------------------------------------------------------------------
// Workflow validation
// --------------------------------------------------------------------------

function validateWorkflow(wf, fileName, knownPersonaKeys, plannedPersonaKeys,
                          knownTensions, patternNames) {
  const fails = [];

  for (const k of REQUIRED_TOP_KEYS) {
    if (!(k in wf)) fails.push(`${fileName}: missing top-level key '${k}'`);
  }
  if (wf.category && wf.category !== 'business') {
    fails.push(`${fileName}: category must be 'business' (got '${wf.category}')`);
  }
  if (wf.name && wf.name !== path.basename(fileName, '.yaml')) {
    fails.push(
      `${fileName}: name '${wf.name}' must match filename stem`,
    );
  }
  if (!Array.isArray(wf.backpressure) || wf.backpressure.length === 0) {
    fails.push(`${fileName}: backpressure must be a non-empty list`);
  }
  if (!Array.isArray(wf.phases) || wf.phases.length === 0) {
    fails.push(`${fileName}: phases must be a non-empty list`);
  }
  if (!Array.isArray(wf.emits) || wf.emits.length === 0) {
    fails.push(`${fileName}: emits must be a non-empty list`);
  } else {
    for (const e of wf.emits) {
      if (!MEMORY_EVENT_TYPES.has(e)) {
        fails.push(
          `${fileName}: emit '${e}' not in vocabulary ` +
          `(${[...MEMORY_EVENT_TYPES].sort().join(', ')})`,
        );
      }
    }
  }

  if (Array.isArray(wf.phases)) {
    const seenPhaseIds = new Set();
    for (const phase of wf.phases) {
      if (typeof phase !== 'object' || phase === null) {
        fails.push(`${fileName}: phase entries must be objects`);
        continue;
      }
      for (const k of REQUIRED_PHASE_KEYS) {
        if (!(k in phase)) {
          fails.push(`${fileName}: phase missing required key '${k}'`);
        }
      }
      if (phase.id) {
        if (seenPhaseIds.has(phase.id)) {
          fails.push(`${fileName}: duplicate phase id '${phase.id}'`);
        }
        seenPhaseIds.add(phase.id);
      }
      if (phase.lead) {
        if (!knownPersonaKeys.has(phase.lead) &&
            !plannedPersonaKeys.has(phase.lead)) {
          fails.push(
            `${fileName}: phase '${phase.id}' lead '${phase.lead}' ` +
            `is not a known or planned persona key`,
          );
        }
      }
      if (Array.isArray(phase.supporting)) {
        for (const s of phase.supporting) {
          if (!knownPersonaKeys.has(s) && !plannedPersonaKeys.has(s)) {
            fails.push(
              `${fileName}: phase '${phase.id}' supporting '${s}' ` +
              `is not a known or planned persona key`,
            );
          }
        }
      }
      if (Array.isArray(phase.tensions)) {
        for (const t of phase.tensions) {
          if (!knownTensions.has(t)) {
            fails.push(
              `${fileName}: phase '${phase.id}' tension '${t}' ` +
              `is not in TENSIONS.md`,
            );
          }
        }
      }
      if (phase.pattern && !patternNames.has(phase.pattern)) {
        fails.push(
          `${fileName}: phase '${phase.id}' references pattern ` +
          `'${phase.pattern}' which is not an existing pattern YAML`,
        );
      }
      if (!Array.isArray(phase.questions) || phase.questions.length === 0) {
        fails.push(
          `${fileName}: phase '${phase.id}' must have a non-empty questions list`,
        );
      }
    }
  }

  return fails;
}

// --------------------------------------------------------------------------
// Entry point
// --------------------------------------------------------------------------

async function main() {
  // Persona keys from router metadata
  const knownPersonaKeys = new Set(Object.keys(PERSONA_METADATA));

  // Planned (PR 3) persona keys from DEPARTMENTS.md
  if (!fs.existsSync(DEPARTMENTS_MD)) {
    console.error(`validate: DEPARTMENTS.md not found at ${DEPARTMENTS_MD}`);
    process.exit(2);
  }
  const departmentsMd = fs.readFileSync(DEPARTMENTS_MD, 'utf-8');
  const plannedMap = parseDepartmentsForPlannedPersonas(departmentsMd);
  const plannedPersonaKeys = new Set(plannedMap.values());
  const nameToKeyMap = buildNameToKey(PERSONA_METADATA, plannedMap);

  // Tension pairs from TENSIONS.md (display names resolved to keys)
  if (!fs.existsSync(TENSIONS_MD)) {
    console.error(`validate: TENSIONS.md not found at ${TENSIONS_MD}`);
    process.exit(2);
  }
  const tensionsMd = fs.readFileSync(TENSIONS_MD, 'utf-8');
  const knownTensions = parseTensionsPairs(tensionsMd, nameToKeyMap);

  // Pattern names from sibling files
  const patternFiles = fs.readdirSync(__dirname)
    .filter((f) => f.endsWith('.yaml'));
  const patternNames = new Set(patternFiles.map((f) => path.basename(f, '.yaml')));

  // Business workflows
  if (!fs.existsSync(BUSINESS_DIR)) {
    console.error(`validate: business/ dir not found at ${BUSINESS_DIR}`);
    process.exit(2);
  }
  const wfFiles = fs.readdirSync(BUSINESS_DIR)
    .filter((f) => f.endsWith('.yaml'))
    .sort();

  console.log(`# validate-workflows - ${wfFiles.length} business workflow(s)`);
  console.log(`  known personas: ${knownPersonaKeys.size}`);
  console.log(`  planned personas (PR 3): ${plannedPersonaKeys.size}`);
  console.log(`  tension pairs: ${knownTensions.size / 2} (${knownTensions.size} directed)`);
  console.log(`  orchestration patterns: ${patternNames.size}`);
  console.log();

  let allFails = [];
  for (const f of wfFiles) {
    const fullPath = path.join(BUSINESS_DIR, f);
    let wf;
    try {
      const text = fs.readFileSync(fullPath, 'utf-8');
      wf = parseYamlSubset(text);
    } catch (e) {
      allFails.push(`${f}: parse error - ${e.message}`);
      console.log(`  ${f}: PARSE FAIL (${e.message})`);
      continue;
    }
    const fails = validateWorkflow(
      wf, f, knownPersonaKeys, plannedPersonaKeys, knownTensions, patternNames,
    );
    if (fails.length === 0) {
      console.log(`  ${f}: OK (${(wf.phases || []).length} phases, emits ${(wf.emits || []).join(', ')})`);
    } else {
      console.log(`  ${f}: FAIL (${fails.length} issue(s))`);
    }
    allFails = allFails.concat(fails);
  }

  if (allFails.length > 0) {
    console.log(`\n${allFails.length} failure(s):`);
    for (const f of allFails) console.log(`  - ${f}`);
    process.exit(1);
  }
  console.log('\nall workflow checks passed');
  process.exit(0);
}

if (process.argv[1].endsWith('validate.js')) {
  main().catch((err) => {
    console.error('validate: unexpected error');
    console.error(err);
    process.exit(2);
  });
}
