---
name: bmad-platinum-story-delivery
description: 'Executes platinum-standard autonomous user story delivery with strict TDD, zero-defect verification, and quality gates.'
---

# BMad Platinum Story Delivery

## Purpose
Delivers user stories autonomously to Platinum engineering standards with complete test coverage, zero regressions, and strict adherence to architectural limits.

## Execution Sequence
1. **Story Context Loading**: Read story specification, acceptance criteria, and relevant architecture docs.
2. **Knowledge Graph Grounding**: Inspect `graphify-out/GRAPH_REPORT.md` to trace blast radius and dependencies.
3. **TDD Cycle**:
   - Write failing unit/integration tests covering all acceptance criteria and negative cases (RED).
   - Implement minimal, modular code (<= 200 LOC per file) to satisfy tests (GREEN).
   - Refactor for performance, readability, and clean interfaces (REFACTOR).
4. **Quality Gates Verification**:
   - Run linter, type checker, and security scanner (`semgrep`).
   - Verify LOC limits across all touched files.
   - Execute test suites and browser QA smoke tests.
5. **Engineering Record Update**: Document changes, test results, and file diffs in the story file.
