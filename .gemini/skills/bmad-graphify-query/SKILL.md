---
name: bmad-graphify-query
description: 'Queries the codebase knowledge graph to find symbol callers, callees, dependencies, and clusters.'
---

# BMad Graphify Query

## Purpose
Executes graph queries against `graphify-out/graph.json` to find relevant modules and relationships.

## Usage
```bash
uvx --from graphifyy graphify query "<search-term or question>"
```

## Key Applications
- Blast radius estimation before refactoring.
- Locating handler functions, event listeners, and API endpoints.
- Discovering shared utilities and avoiding duplicate implementations.
