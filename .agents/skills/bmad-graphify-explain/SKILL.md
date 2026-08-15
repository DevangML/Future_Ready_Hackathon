---
name: bmad-graphify-explain
description: 'Generates deep architectural explanations of a node, symbol, or community from the knowledge graph.'
---

# BMad Graphify Explain

## Purpose
Provides plain-language structural explanations of a code node and its neighbors in the knowledge graph.

## Usage
```bash
uvx --from graphifyy graphify explain "<node_name>"
```

## Output Highlights
- Node type, file path, and line range.
- Inbound callers and outbound dependencies.
- Centrality score and community membership.
