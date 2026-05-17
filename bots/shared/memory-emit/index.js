/**
 * bots/shared/memory-emit — JS-side persona memory-emit protocol.
 *
 * Sibling of the Python implementation in orchestrator/emit_parser.py +
 * orchestrator/persona.py. Both consume the same YAML contract so
 * Mattermost bot replies and orchestrator-driven workflow runs land
 * structurally-identical typed events in shared memory.
 */
export { MEMORY_EVENT_TYPES, parseEmits } from './parser.js';
export { MEMORY_EMIT_PREAMBLE } from './preamble.js';
