---
name: bmad-graphify
description: 'Builds and updates the codebase knowledge graph for structural awareness and dependency tracing.'
---

# BMad Graphify

## Purpose
Builds and maintains the codebase knowledge graph, extracting AST nodes, dependencies, and call hierarchies.

## Outputs Produced
- `graphify-out/GRAPH_REPORT.md`: Architectural clusters, god nodes, and unexpected couplings.
- `graphify-out/graph.json`: Machine-readable graph for automated querying and path tracing.

## Usage
```bash
uvx --from graphifyy graphify update .
```
Workflows like `bmad-dev-story` and `bmad-code-review` read this graph to navigate code safely.
