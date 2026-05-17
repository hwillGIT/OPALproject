/**
 * The MEMORY EMIT PROTOCOL preamble text — injected into every
 * persona's system prompt so the LLM knows when and how to author
 * memory-emit blocks.
 *
 * MUST stay in sync with the Python preamble in
 * orchestrator/persona.py (_PREAMBLE). Both describe the same
 * YAML contract; both are consumed by the same parser shape.
 */
export const MEMORY_EMIT_PREAMBLE = `\
MEMORY EMIT PROTOCOL (important — read carefully)
=================================================
You — not an external classifier — decide when something you say is
worth recording in the team's shared memory. If, and ONLY if, your
reply contains a moment that future-you (or another teammate) would
need to know about later, append a fenced YAML block at the end of
your reply. NEVER emit just to be thorough; emit only when there is
real signal.

Allowed event types:

  DECISION         a call you (or the team) just made
  ACTION           something concrete you (or someone) will now do
  INSIGHT          a non-obvious observation worth keeping
  PREDICTION       a forward-looking claim (REQUIRES \`confidence:\` in [0,1])
  OUTCOME          a result that verifies or refutes an earlier event
  DEBATE           an unresolved tension worth re-visiting
  CONTEXT_CHANGE   the situation shifted in a way that invalidates
                   prior assumptions
  ARTIFACT         a deliverable produced (spec, diagram, doc)

Format (must be a fenced block tagged \`memory-emit\`):

\`\`\`memory-emit
- type: DECISION
  title: One short headline (~80 chars)
  content: |
    Optional longer body. Defaults to the surrounding prose if omitted.
  confidence: 0.8           # PREDICTIONs MUST set this in [0,1]
  related: [evt-9f3a...]    # optional list of prior event ids
  tags: [esp32, hardware]   # optional extra tags
- type: ACTION
  title: Order 10 ESP32-S3 dev boards for the prototype rig
\`\`\`

Multiple events in one block are fine; each list entry is one event.
If you have nothing memory-worthy, OMIT the block entirely — an empty
block or no block at all is the correct answer for routine prose.

The user does NOT see the fenced block; it is stripped before your
reply is posted to the channel.
`;
