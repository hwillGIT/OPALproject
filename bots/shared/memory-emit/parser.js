/**
 * JS-side persona memory-emit block parser.
 *
 * Contract-compatible with the Python implementation in
 * orchestrator/emit_parser.py — both consume the same YAML shape
 * the persona is taught to produce by the preamble in
 * bots/shared/memory-emit/preamble.js (mirrors orchestrator/persona.py).
 *
 *     prose...
 *
 *     ```memory-emit
 *     - type: DECISION
 *       title: short headline
 *       content: |
 *         optional body
 *       confidence: 0.8
 *       related: [evt-aaaa, evt-bbbb]
 *       tags: [esp32, hardware]
 *     ```
 *
 * Returns { cleanText, emits, malformed }:
 *   - cleanText: response with fenced blocks stripped + blank-line
 *                runs collapsed; safe to post to Mattermost
 *   - emits: list of { type, title, content, confidence, related,
 *                       tags } objects, validated against the schema
 *   - malformed: list of { raw, reason } objects so the caller can
 *                preserve the persona's intent as a CONTEXT_CHANGE
 *                event — the persona is NEVER silently ignored
 *
 * Zero external dependencies: we walk the constrained emit-block YAML
 * by hand rather than pulling js-yaml. The shape is too narrow to need
 * full YAML, and the workflow validator established the precedent
 * (see bots/shared/workflows/validate.js).
 */

export const MEMORY_EVENT_TYPES = new Set([
  'DECISION',
  'ACTION',
  'INSIGHT',
  'PREDICTION',
  'OUTCOME',
  'DEBATE',
  'CONTEXT_CHANGE',
  'ARTIFACT',
]);

// Matches a fenced code block tagged `memory-emit`. Tolerant of
// fence width (3+ backticks or tildes), CRLFs, and trailing whitespace.
const FENCE_RE = /^([`~]{3,})[ \t]*memory-emit[ \t]*\r?\n([\s\S]*?)^\1[ \t]*$/gm;

/**
 * Parse every memory-emit block in a response.
 *
 * @param {string} responseText
 * @returns {{ cleanText: string, emits: Array, malformed: Array }}
 */
export function parseEmits(responseText) {
  if (!responseText) {
    return { cleanText: '', emits: [], malformed: [] };
  }

  const emits = [];
  const malformed = [];

  const cleanedRaw = responseText.replace(FENCE_RE, (rawBlock, _fence, body) => {
    const { emits: blockEmits, malformed: blockMalformed } = parseOneBlock(body, rawBlock);
    emits.push(...blockEmits);
    malformed.push(...blockMalformed);
    return '';
  });

  // Collapse runs of blank lines a stripped fence leaves behind.
  let cleanText = cleanedRaw.replace(/\n{3,}/g, '\n\n');
  cleanText = cleanText.trim();
  if (cleanText.length > 0) cleanText += '\n';

  return { cleanText, emits, malformed };
}

// ---------------------------------------------------------------------------
// Block + entry parsing
// ---------------------------------------------------------------------------

function parseOneBlock(body, rawBlock) {
  const lines = body.split(/\r?\n/);
  // Strip a fully empty trailing element
  if (lines.length > 0 && lines[lines.length - 1] === '') lines.pop();

  if (lines.every((l) => l.trim() === '')) {
    // Empty block — persona explicitly chose not to emit, which is fine
    return { emits: [], malformed: [] };
  }

  // Tokenize into entries: each entry begins with a line matching `- key: value`.
  const entries = [];
  let current = null;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (line.trim() === '') continue;
    const startsItem = /^-\s+/.test(line);
    if (startsItem) {
      if (current) entries.push(current);
      current = { lineNo: i, lines: [line.replace(/^-\s+/, '  ')] };
    } else {
      if (!current) {
        // Stray non-list content at top level
        return {
          emits: [],
          malformed: [{
            raw: rawBlock,
            reason: `top-level must be a YAML list of emit entries; saw '${line.trim()}' before any '- type: ...'`,
          }],
        };
      }
      current.lines.push(line);
    }
  }
  if (current) entries.push(current);

  if (entries.length === 0) {
    return {
      emits: [],
      malformed: [{
        raw: rawBlock,
        reason: 'top-level must be a YAML list of emit entries; got no list items',
      }],
    };
  }

  const emits = [];
  const malformed = [];
  entries.forEach((entry, idx) => {
    const result = parseEntry(entry.lines, idx);
    if (result.ok) emits.push(result.value);
    else malformed.push({ raw: entry.lines.join('\n'), reason: result.reason });
  });
  return { emits, malformed };
}

function parseEntry(entryLines, index) {
  // entryLines are indented (2 spaces) at the entry level
  // Walk line-by-line collecting key/value pairs. Support inline
  // scalars, inline lists [a, b], and `|` block scalars for content.
  const fields = {};
  let i = 0;
  while (i < entryLines.length) {
    const line = entryLines[i];
    if (line.trim() === '') { i++; continue; }
    const m = line.match(/^(\s+)([A-Za-z_][\w-]*)\s*:\s*(.*)$/);
    if (!m) {
      return { ok: false, reason: `entry #${index}: malformed line ${JSON.stringify(line)}` };
    }
    const baseIndent = m[1].length;
    const key = m[2];
    const rest = m[3];

    if (rest === '|' || rest === '>') {
      // Block scalar — gather subsequent lines indented deeper than baseIndent
      const buf = [];
      let j = i + 1;
      let blockIndent = -1;
      while (j < entryLines.length) {
        const l = entryLines[j];
        if (l.trim() === '') { buf.push(''); j++; continue; }
        const ind = leadingSpaces(l);
        if (blockIndent < 0) {
          if (ind <= baseIndent) break;
          blockIndent = ind;
        }
        if (ind < blockIndent) break;
        buf.push(l.slice(blockIndent));
        j++;
      }
      const joiner = rest === '>' ? ' ' : '\n';
      fields[key] = buf.join(joiner).replace(/\s+$/, '');
      i = j;
      continue;
    }

    if (rest.startsWith('[') && rest.endsWith(']')) {
      // Inline list [a, b, c]
      const inner = rest.slice(1, -1).trim();
      fields[key] = inner === '' ? []
        : inner.split(',').map((s) => stripQuotes(s.trim())).filter((s) => s !== '');
      i++;
      continue;
    }

    // Inline scalar
    fields[key] = coerceScalar(stripQuotes(rest));
    i++;
  }

  return validateFields(fields, index);
}

function validateFields(fields, index) {
  const type = fields.type;
  if (!type) return { ok: false, reason: `entry #${index} missing required field 'type'` };
  if (!MEMORY_EVENT_TYPES.has(type)) {
    return {
      ok: false,
      reason: `entry #${index}: type ${JSON.stringify(type)} not in vocabulary (${[...MEMORY_EVENT_TYPES].sort().join(',')})`,
    };
  }
  const title = fields.title;
  if (!title || typeof title !== 'string') {
    return { ok: false, reason: `entry #${index} (${type}) missing required field 'title'` };
  }

  let confidence = fields.confidence;
  if (type === 'PREDICTION') {
    if (confidence === undefined || confidence === null) {
      return { ok: false, reason: `entry #${index}: PREDICTION requires 'confidence' in [0,1]` };
    }
  }
  if (confidence !== undefined && confidence !== null) {
    const n = Number(confidence);
    if (Number.isNaN(n)) {
      return { ok: false, reason: `entry #${index}: confidence must be numeric; got ${JSON.stringify(confidence)}` };
    }
    if (n < 0 || n > 1) {
      return { ok: false, reason: `entry #${index}: confidence ${n} not in [0,1]` };
    }
    confidence = n;
  } else {
    confidence = null;
  }

  let content = fields.content;
  if (content !== undefined && content !== null && typeof content !== 'string') {
    return { ok: false, reason: `entry #${index}: content must be a string` };
  }
  if (content === undefined) content = null;

  let related = fields.related;
  if (related === undefined || related === null) related = [];
  if (!Array.isArray(related) || !related.every((r) => typeof r === 'string')) {
    return { ok: false, reason: `entry #${index}: related must be a list of event-id strings` };
  }

  let tags = fields.tags;
  if (tags === undefined || tags === null) tags = [];
  if (!Array.isArray(tags) || !tags.every((t) => typeof t === 'string')) {
    return { ok: false, reason: `entry #${index}: tags must be a list of strings` };
  }

  return {
    ok: true,
    value: {
      type: String(type),
      title: String(title).trim(),
      content,
      confidence,
      related,
      tags,
    },
  };
}

// ---------------------------------------------------------------------------
// Tiny scalar helpers
// ---------------------------------------------------------------------------

function leadingSpaces(s) {
  let n = 0;
  while (n < s.length && s[n] === ' ') n++;
  return n;
}

function stripQuotes(v) {
  v = v.trim();
  if (v.length >= 2 &&
      ((v.startsWith('"') && v.endsWith('"')) ||
       (v.startsWith("'") && v.endsWith("'")))) {
    return v.slice(1, -1);
  }
  return v;
}

function coerceScalar(v) {
  if (v === '' || v === '~' || v === 'null') return null;
  if (v === 'true') return true;
  if (v === 'false') return false;
  if (/^-?\d+$/.test(v)) return parseInt(v, 10);
  if (/^-?\d*\.\d+$/.test(v)) return parseFloat(v);
  return v;
}
