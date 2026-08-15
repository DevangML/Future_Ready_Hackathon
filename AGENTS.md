# AGENTS.md - BMad AI OS Multi-Agent Manifest

## 1. System Overview
This repository operates under the BMad AI OS autonomous agent paradigm. All agents interacting with this codebase must adhere to the roles, boundaries, and validation sequences specified herein.

---

## 2. Agent Roles & Specializations

### A. Governance & Gate Agent (`agent-governance`)
- **Domain**: `.specify/memory/`, `.semgrep/`, `.sentrux/`, `scripts/`
- **Mandate**: Enforces the 7 Immutable User Rules, runs gate scripts, validates LOC limits (<= 200 LOC/file), and monitors AST/security policies.
- **Key Artifacts**: `constitution.md`, `rules.toml`, `ai_session_gate.sh`.

### B. Architecture & Spec Agent (`agent-architect`)
- **Domain**: `docs/`, `.specify/`, PRD & system design
- **Mandate**: Translates user requirements into formal schemas, API contracts, and component boundaries without adding speculative features.
- **Key Artifacts**: `ARCHITECTURE.md`, data contracts, solver models.

### C. Core Backend & Solver Agent (`agent-backend`)
- **Domain**: `backend/`
- **Mandate**: Implements Gemini VLM ingestion, OR-Tools CP-SAT timetable optimizer, and FastAPI endpoints.
- **Rules**: TDD-first, modular sub-200 LOC files, pure functions, zero duplication.

### D. Perception & Frontend Agent (`agent-frontend`)
- **Domain**: `frontend/`, `docs/`
- **Mandate**: Builds reactive UI components, edge face tracking (`tracking.js`), QR scanner, and kiosk attendance interfaces.
- **Rules**: Accessible, responsive, no unnecessary dependencies, <= 200 LOC/file.

### E. Verification & QA Agent (`agent-qa`)
- **Domain**: `tests/`, `scripts/`
- **Mandate**: Executes TDD red-green cycle, unit/integration suites, Semgrep audits, and Playwright browser smoke tests.
- **Key Artifacts**: `pytest` suites, `playwright_browser_qa.sh`.

---

## 3. Rules of Engagement & Token Economy

1. **Graph-First Retrieval**: Always query `graphify-out/` or AST graph before reading raw files to conserve ~90% token bandwidth.
2. **Terse Communication (Caveman Mode)**: Responses between subagents should be concise, structured, and factual.
3. **Strict File Size Cap**: No file may exceed 200 LOC. If a file approaches 180 LOC, refactor into cohesive sub-modules.
4. **Mandatory TDD Cycle**:
   ```
   [PRD Requirement] -> [Failing Test (RED)] -> [Minimal Code (GREEN)] -> [Gate Verification (PASS)]
   ```
5. **No Scope Creep**: Only implement what is explicitly specified by the BMad CIS module.

---

## 4. Quality Gates Execution
Before completing any session, run:
```bash
bash scripts/ai_session_gate.sh
bash scripts/platinum_governance_check.sh
```
Both commands must exit with code 0.
