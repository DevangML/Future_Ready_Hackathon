# BMad AI OS Supreme Constitution

## Preamble
This Constitution defines the immutable operating principles, architecture boundaries, and quality gates for autonomous and human agents working within the BMad AI OS ecosystem.

---

## The 7 Immutable User Rules
1. **Reuse First**: Do not reinvent the wheel; reuse existing libraries, utilities, and components whenever possible.
2. **Strict LOC Gate**: Every file MUST NOT exceed 200 Lines Of Code (LOC). Split modules when approaching limits.
3. **Small & Meaningful Methods**: Keep functions single-purpose, concise, and semantically clear (<30 LOC per function).
4. **Strict TDD (bmad-tea)**: Always start with failing tests derived from the PRD/spec, then write minimal code to pass.
5. **Minimal Footprint**: Implement required features in the least overall code and fewest files possible.
6. **Learn & Innovate**: Study existing architecture and patterns; innovate where appropriate and annotate innovations with inline comments (`# INNOVATION:`).
7. **Scope Discipline**: Do not invent new sub-requirements, unapproved features, or bells/whistles (owned strictly by the BMad CIS module).

---

## Article I: Core Foundation & Purpose
- All development must serve verified user needs specified in approved PRDs and story documents.
- Simplicity and correctness take precedence over speculative abstractions or premature generalizations.

## Article II: Architectural Standards & Modularity
- Maintain clean separation of concerns: Perception, Optimization, CV/Edge Security, and Governance.
- Hard file limit: Maximum 200 lines per file across all languages (Python, JS/JSX, Shell, Configs, Docs).
- Eliminate duplicate logic immediately by extracting shared utility helpers.

## Article III: Test-Driven Development (bmad-tea)
- No feature code may be committed without corresponding automated unit, integration, or contract tests.
- Execution cycle: Red (failing test based on PRD) -> Green (minimal passing code) -> Refactor (clean, optimize, gate check).
- Tests must execute deterministically and run locally without external unmocked dependencies.

## Article IV: Scope Control & CIS Authority
- Changes to requirements, schemas, or scope must originate from or be ratified by the BMad CIS module.
- Unsolicited features or phantom enhancements are considered defects and blocked by gates.

## Article V: Innovation & Pattern Inheritance
- Agents must inspect existing codebase patterns (`dont-b-mad`, `_bmad`, backend/frontend structures) prior to implementation.
- Architectural improvements or innovative optimizations must be tagged with explicit commentary.

## Article VI: Execution Verification & Quality Gates
- Every session must pass all automated verification gates before code merge or task completion.
- Failures in linting, syntax, test execution, or LOC limits trigger immediate rollback.

### Article VI-A: Sentrux Verification Sequence
1. **Pre-Session Check**: Verify active sprint story, PRD alignment, and baseline AST tree integrity.
2. **Boundary Validation**: Check architectural boundaries, forbidden cross-imports, and path permissions via `.sentrux/rules.toml`.
3. **Static Analysis & Safety**: Execute Semgrep rule packs (`platform-baseline`, `python-safety`, `loc-gate`).
4. **Dynamic Verification**: Run targeted test suites (`pytest`, `jest`/`vitest`, browser smoke tests).
5. **Session Certification**: Execute `scripts/ai_session_gate.sh` and ensure exit status 0.

### Article VI-B: Token Economy & Graph-First Retrieval
- **Graph-First Retrieval**: Always retrieve AST/dependency context via `graphify` artifacts (~90% token reduction vs brute-force search).
- **Caveman Mode**: Utilize terse, information-dense communication and responses (`dontbmad-caveman`) to minimize token overhead.
- **Innovation Loop**: Synthesize retrieved graph nodes, generate targeted diffs, and verify in tight iterative cycles.

### Article VI-C: Extensibility & Optional Add-ons
- Modular plugins, headless browser testing (`playwright_browser_qa.sh`), and real-time telemetry may be enabled cleanly as opt-in extensions without violating core constraints.

## Article VII: Governance Enforcement & Platinum Compliance
- This Constitution is the supreme operational law of the repository.
- Violations detected by `scripts/platinum_governance_check.sh` block deployment unconditionally.
