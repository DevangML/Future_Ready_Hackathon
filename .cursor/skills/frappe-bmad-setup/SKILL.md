---
name: frappe-bmad-setup
description: 'Configures and orchestrates BMad AI OS and Liberoid agents within Frappe applications.'
---

# Frappe BMad Setup

## Purpose
Integrates BMad autonomous agent framework and Liberoids orchestration inside Frappe apps.

## Setup Steps
1. **Install Module**: Ensure `liberoids` and `bmad` apps are installed on the site.
2. **Register Orchestrators**: Seed standard orchestrator records in `Liberoid Agents Orchestrator`.
3. **Tool Mapping**: Bind Frappe whitelisted methods to Liberoid agent tools.
4. **Run Verification**: Execute automated test cases via `api_run_test_case` to confirm agent operation.
