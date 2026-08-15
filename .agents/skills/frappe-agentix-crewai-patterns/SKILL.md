---
name: frappe-agentix-crewai-patterns
description: 'Multi-agent orchestration and tool integration using Agentix and CrewAI inside Frappe apps.'
---

# Frappe Agentix & CrewAI Patterns

## Purpose
Integrates multi-agent workflows into Frappe, exposing Frappe DocTypes and methods as AI tools.

## Architecture
1. **Tool Definition**: Wrap Frappe ORM functions into structured Pydantic schemas.
2. **Task Queueing**: Dispatch agent tasks via `frappe.enqueue` with execution logs saved in `Agent Run Log`.
3. **State Storage**: Persist intermediate conversation memory in custom Frappe DocTypes.
4. **Guardrails**: Apply rate limiting and parameter verification on all AI tool calls.
