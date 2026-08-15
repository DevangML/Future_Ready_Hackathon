---
name: bmad-graphify-path
description: 'Traces shortest dependency and call paths between two symbols or files in the knowledge graph.'
---

# BMad Graphify Path

## Purpose
Finds the connection path between two nodes in the codebase graph.

## Usage
```bash
uvx --from graphifyy graphify path "<source_symbol>" "<target_symbol>"
```

## Insights Provided
- Call stack chains from entry point to database queries.
- Hidden transitive dependencies across modules.
