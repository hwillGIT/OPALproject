/**
 * Tests for the JS memory-emit parser.
 *
 * Run: node --test bots/shared/memory-emit/tests/parser.test.mjs
 *
 * Mirrors orchestrator/tests/test_emit_parser.py so both sides of
 * the contract are exercised by the same shape of inputs.
 */
import test from 'node:test';
import assert from 'node:assert/strict';

import { parseEmits } from '../parser.js';

// ──────────────────────────────────────────────────────────────────────
// Happy path
// ──────────────────────────────────────────────────────────────────────

test('single DECISION emit parses + clean text is stripped', () => {
  const text = `Here is my call.

\`\`\`memory-emit
- type: DECISION
  title: Going with ESP32-S3
\`\`\`
`;
  const r = parseEmits(text);
  assert.equal(r.malformed.length, 0);
  assert.equal(r.emits.length, 1);
  assert.deepEqual(r.emits[0], {
    type: 'DECISION',
    title: 'Going with ESP32-S3',
    content: null,
    confidence: null,
    related: [],
    tags: [],
  });
  assert.ok(!r.cleanText.includes('memory-emit'));
  assert.equal(r.cleanText.trim(), 'Here is my call.');
});

test('no emit block is fine — verbatim text, no events', () => {
  const text = 'Just prose. Nothing memory-worthy here.\n';
  const r = parseEmits(text);
  assert.equal(r.emits.length, 0);
  assert.equal(r.malformed.length, 0);
  assert.equal(r.cleanText.trim(), 'Just prose. Nothing memory-worthy here.');
});

test('empty fenced block is silently allowed', () => {
  const text = `prose

\`\`\`memory-emit

\`\`\`
`;
  const r = parseEmits(text);
  assert.equal(r.emits.length, 0);
  assert.equal(r.malformed.length, 0);
  assert.ok(!r.cleanText.includes('memory-emit'));
});

test('multiple emits in one block', () => {
  const text = `prose

\`\`\`memory-emit
- type: DECISION
  title: pick X
- type: ACTION
  title: order 10 of X
- type: PREDICTION
  title: this ships in 6 weeks
  confidence: 0.7
\`\`\`
`;
  const r = parseEmits(text);
  assert.equal(r.malformed.length, 0);
  assert.deepEqual(r.emits.map((e) => e.type), ['DECISION', 'ACTION', 'PREDICTION']);
  assert.equal(r.emits[2].confidence, 0.7);
});

test('emit carries optional fields (content, related, tags)', () => {
  const text = `prose

\`\`\`memory-emit
- type: INSIGHT
  title: brief headline
  content: |
    A longer body
    spanning lines.
  related: [evt-aaaa, evt-bbbb]
  tags: [esp32, hardware]
\`\`\`
`;
  const r = parseEmits(text);
  assert.equal(r.emits.length, 1);
  const e = r.emits[0];
  assert.ok(e.content.startsWith('A longer body'));
  assert.deepEqual(e.related, ['evt-aaaa', 'evt-bbbb']);
  assert.deepEqual(e.tags, ['esp32', 'hardware']);
});

test('multiple blocks in one response both extracted', () => {
  const text = `first thought

\`\`\`memory-emit
- type: DECISION
  title: first
\`\`\`

then more prose

\`\`\`memory-emit
- type: INSIGHT
  title: second
\`\`\`
`;
  const r = parseEmits(text);
  assert.deepEqual(r.emits.map((e) => e.title), ['first', 'second']);
  assert.ok(!r.cleanText.includes('memory-emit'));
});

// ──────────────────────────────────────────────────────────────────────
// Validation failures
// ──────────────────────────────────────────────────────────────────────

test('unknown type rejected', () => {
  const text = `\`\`\`memory-emit
- type: WIZARDRY
  title: cast spell
\`\`\`
`;
  const r = parseEmits(text);
  assert.equal(r.emits.length, 0);
  assert.equal(r.malformed.length, 1);
  assert.match(r.malformed[0].reason, /not in vocabulary/);
});

test('missing title rejected', () => {
  const text = `\`\`\`memory-emit
- type: DECISION
\`\`\`
`;
  const r = parseEmits(text);
  assert.equal(r.emits.length, 0);
  assert.match(r.malformed[0].reason, /missing required field 'title'/);
});

test('PREDICTION must carry confidence', () => {
  const text = `\`\`\`memory-emit
- type: PREDICTION
  title: it will rain
\`\`\`
`;
  const r = parseEmits(text);
  assert.equal(r.emits.length, 0);
  assert.match(r.malformed[0].reason, /requires 'confidence'/);
});

test('PREDICTION confidence out of range rejected', () => {
  const text = `\`\`\`memory-emit
- type: PREDICTION
  title: x
  confidence: 1.5
\`\`\`
`;
  const r = parseEmits(text);
  assert.match(r.malformed[0].reason, /not in \[0,1\]/);
});

test('top-level non-list rejected', () => {
  const text = `\`\`\`memory-emit
type: DECISION
title: not a list
\`\`\`
`;
  const r = parseEmits(text);
  assert.equal(r.emits.length, 0);
  assert.match(r.malformed[0].reason, /top-level must be a YAML list/);
});

test('mixed valid + malformed in one block: keep valid, record malformed', () => {
  const text = `\`\`\`memory-emit
- type: DECISION
  title: good one
- type: NONSENSE
  title: bad one
- type: INSIGHT
  title: also good
\`\`\`
`;
  const r = parseEmits(text);
  assert.deepEqual(r.emits.map((e) => e.title), ['good one', 'also good']);
  assert.equal(r.malformed.length, 1);
  assert.match(r.malformed[0].reason, /not in vocabulary/);
});

test('related must be a list of strings', () => {
  const text = `\`\`\`memory-emit
- type: DECISION
  title: x
  related: 42
\`\`\`
`;
  const r = parseEmits(text);
  assert.match(r.malformed[0].reason, /related must be a list/);
});

// ──────────────────────────────────────────────────────────────────────
// Edge cases
// ──────────────────────────────────────────────────────────────────────

test('empty string returns empty result', () => {
  const r = parseEmits('');
  assert.equal(r.cleanText, '');
  assert.equal(r.emits.length, 0);
  assert.equal(r.malformed.length, 0);
});

test('fence at end of response without trailing newline', () => {
  const text = 'prose\n\n```memory-emit\n- type: DECISION\n  title: x\n```';
  const r = parseEmits(text);
  assert.equal(r.emits.length, 1);
});

test('unrelated fenced code block is left alone', () => {
  const text = `here's some code:

\`\`\`javascript
console.log('hello');
\`\`\`

and prose.
`;
  const r = parseEmits(text);
  assert.equal(r.emits.length, 0);
  assert.equal(r.malformed.length, 0);
  assert.ok(r.cleanText.includes("console.log('hello');"));
});
