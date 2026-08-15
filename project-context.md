# Project Context: Future Ready Hackathon AI OS

## 1. System Overview
Future Ready Hackathon AI OS is an autonomous, high-assurance intelligent timetable scheduling and kiosk management system built under the BMad AI OS paradigm.

---

## 2. Core Architecture & Tech Stack
- **Backend**: Python 3, FastAPI, Google GenAI (Gemini VLM form ingestion), Google OR-Tools CP-SAT (constraint-based timetable optimizer).
- **Frontend**: React 18, Vite, TailwindCSS / Vanilla CSS, Lucide icons, Edge Face Tracking (`tracking.js`), Attendance Kiosk.
- **AI OS Framework**: BMad Method (BMM), Creative Intelligence Suite (CIS), Test Engineering Architecture (TEA), BMad Builder (BMB).

---

## 3. The 7 Immutable User Rules & Governance
1. **Reuse First**: Leverage existing libraries and components before writing bespoke logic.
2. **Strict LOC Gate**: Hard cap of <= 200 lines per file across all code and configs.
3. **Small & Meaningful Methods**: Keep functions single-purpose and <= 30 LOC.
4. **Strict TDD (bmad-tea)**: Red -> Green -> Refactor cycle for all backend/frontend features.
5. **Minimal Footprint**: Minimal file count and total LOC footprint.
6. **Learn & Innovate**: Study existing architecture; annotate innovations (`# INNOVATION:`).
7. **Scope Discipline**: Zero unapproved feature creep; CIS module ratifies scope.

---

## 4. Verification Gates & Execution Commands
- **Dynamic Tests**: `pytest tests/ -q` or `python3 -m unittest discover tests`
- **Gate Check**: `bash scripts/ai_session_gate.sh`
- **Platinum Governance Check**: `bash scripts/platinum_governance_check.sh`

---

## 5. Directory Invariants
- `_bmad/`: BMad configuration, routing, agents, and module configs.
- `_bmad-output/`: Planning artifacts, implementation artifacts (sprint status), test artifacts.
- `.specify/memory/`: Supreme Constitution and governance memory.
- `backend/`: FastAPI application, optimization engines, and schemas.
- `frontend/`: UI components, interactive tour deck, and kiosk interface.
- `tests/`: Automated test suites and regression verifications.
