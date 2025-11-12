# Scripts

This directory contains utility scripts and tools for the OPAL project.

## Directory Structure

### `memory/`
Claude memory and session state management scripts:

- **embed_and_store.py** - Stores session summaries and context by embedding content via Google Gemini API into ChromaDB vector database for Claude's long-term memory
- **query_chroma.py** - Retrieves stored session summaries and context from Claude's memory (ChromaDB session_summaries collection)
- **neo4j_updater.py** - Updates Claude's knowledge graph in Neo4j to maintain relationships and context across sessions
- **session_YYYYMMDD_setup.cypher** - Session-specific Cypher scripts to initialize or update knowledge graph state
- **session_YYYYMMDD_setup.txt** - Human-readable session summaries documenting goals, components, and actions

## Purpose

These scripts enable Claude to maintain conversational memory and state across sessions by:
- Storing important session summaries as vector embeddings for semantic retrieval
- Maintaining a knowledge graph of relationships, entities, and context
- Allowing Claude to recall previous conversations, decisions, and project state

## Usage

Refer to individual script documentation for usage details. Most scripts require environment variables configured in a `.env` file at the project root.

### Required Environment Variables

```bash
# Google Gemini API (for embed_and_store.py)
GOOGLE_API_KEY=your_api_key_here

# Neo4j Knowledge Graph (for neo4j_updater.py)
KNOWLEDGE_GRAPH_URI=bolt://localhost:7687
KNOWLEDGE_GRAPH_USERNAME=neo4j
KNOWLEDGE_GRAPH_PASSWORD=your_password_here
KNOWLEDGE_GRAPH_DATABASE=neo4j
```

### ChromaDB Setup

Scripts assume ChromaDB is running as an HTTP server for Claude's vector memory:
```bash
# Default configuration
Host: localhost
Port: 8000
Collection: session_summaries
```
