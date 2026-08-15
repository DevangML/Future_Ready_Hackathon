# Rock Platinum Session Checkpoint Template

## Session Metadata
- **Date**: YYYY-MM-DD HH:MM
- **Lead Agent / Persona**: Rock (Platinum Delivery Lead)
- **Sprint / Story ID**: `story-X.Y`
- **Execution Status**: `PASSED` | `IN_PROGRESS` | `FAILED`

---

## 1. Objective & Scope
- **Story Goal**: [Concise statement of story objective]
- **Target Components**: [Backend / Frontend / Optimizers / Contracts]
- **CIS Ratified**: Yes / No

---

## 2. Sentrux & Constitutional Verification Gate
| Gate Check | Standard | Result | Notes |
|:---|:---|:---|:---|
| Constitution Art. VI-A | AST Boundary Check | PASS | No unauthorized cross-domain imports |
| LOC Gate | <= 200 LOC per file | PASS | All newly created & modified files verified |
| Function Complexity | <= 30 LOC per function | PASS | Single-purpose methods maintained |
| TDD Enforcement | Red -> Green -> Refactor | PASS | Unit/contract tests authored before logic |
| Semgrep Rule Packs | platform-baseline / safety | PASS | 0 blocking issues |
| Dynamic Test Suite | pytest / frontend test | PASS | 100% tests green |

---

## 3. Implemented Changes (Delta)
- **Created Files**:
  - `path/to/file1.py` - Description (LOC: X)
  - `path/to/file2.jsx` - Description (LOC: Y)
- **Modified Files**:
  - `path/to/existing.py` - Description (LOC: Z)

---

## 4. Test & Verification Evidence
```bash
# Test execution output summary
pytest tests/ -q
# Result: X passed in Y.YYs
```

---

## 5. Artifact Handoff & Next Steps
- **Updated Sprint Status**: `_bmad-output/implementation-artifacts/sprint-status.yaml`
- **Next Story**: `story-X.Z`
- **Sign-off**: `Rock - Platinum Delivery Lead`
