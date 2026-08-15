# ⚡ EduFlow OS: Autonomous School Operations Engine

> **Future Ready Hackathon 2026 Submission — Team Ragnarok (VIT Pune)**  
> *Transforming physical paperwork, static spreadsheets, and manual attendance into a real-time, self-orchestrating school engine.*

---

## 📌 Problem Statement & Vision

Schools suffer from daily operational friction:
- When a teacher calls in sick at 7:30 AM, administrators spend hours scrambling while students lose class time.
- Physical admission forms and medical slips pile up unread in paper trays for weeks.
- Attendance systems suffer from proxy fraud ("buddy-punching"), where students swap ID cards.

**EduFlow OS** operates as an **Autonomous School Operating System**. Powered by Google Gemini 1.5 Vision VLMs, Google OR-Tools CP-SAT Solvers, and Edge Computer Vision, EduFlow replaces fragmented tools with a self-resolving, real-time operating layer.

---

## 📁 Modular Directory Structure

```text
Future_Ready_Hackathon/
├── backend/                  # Python FastAPI Backend & Optimization Engine
│   ├── app/
│   │   ├── main.py           # REST API routes & controllers
│   │   ├── state.py          # Centralized in-memory campus state DB
│   │   ├── solver.py         # Google OR-Tools CP-SAT Timetable Engine
│   │   ├── parser.py         # Gemini 1.5 Vision VLM Document Reader
│   │   └── mock_data.py      # Seed data (CBSE Class 10 roster & timetable)
├── frontend/                 # React 19 + Tailwind CSS v4 Dashboard
│   ├── src/components/       # Modular UI components (Bento Grid, Kiosk, Timetable)
├── tests/                    # 60+ Hardcore Chaos, Adversarial, & Unit Tests
├── docs/                     # Specifications, SRS, Architecture, PRD, & Research
└── scripts/                  # Automated Quality Gates & Platinum Governance
```

---

## ✨ Core Features & Technical Highlights

### 1. 🪄 Magic Dropzone (Vision-Language Model Ingestion)
* **Zero-Shot VLM Parsing**: Uses Google Gemini 1.5 Vision to parse handwritten forms without pre-defined templates.
* **Human-in-the-Loop Safety**: Low-confidence extractions (< 0.80) are automatically routed to the **Human Review Inbox**.

### 2. ⚡ Reactive Timetable Engine & Live Disruption Solver
* **Google OR-Tools (CP-SAT Solver)**: Solves hard constraints (teacher specialization, room capacities, zero double-booking) in **< 0.05 seconds**.
* **Real-Time Reallocation**: When a teacher is marked absent, the solver instantly reassigns coverage across available staff.

### 3. 🛡️ Smart Kiosk Attendance (Anti-Buddy Punching)
* **100% Software ($0 Hardware Overhead)**: Operates on standard webcams—eliminates expensive RFID gate costs.
* **Dual-Modal Edge CV Security**: Scans student QR codes while detecting live human faces, blocking proxy attendance.

### 4. 📊 Academic Risk & Predictive Analytics
* Evaluates scan frequency, truancy patterns, and missing documents to highlight students at academic risk proactively.

---

## 🛠️ Technology Stack

| Layer | Technology Used | Purpose |
|---|---|---|
| **Perception Layer** | Google Gemini 1.5 Vision VLM | Zero-shot handwritten document reading |
| **Edge Vision Layer** | Google MediaPipe / Edge CV | Real-time 60 FPS face detection in browser |
| **Optimization Engine** | Google OR-Tools (CP-SAT) | Combinatorial constraint solver for timetabling |
| **Backend API** | Python 3.10+, FastAPI, Uvicorn | High-performance asynchronous REST API |
| **Frontend UI** | React 19, Vite, Tailwind CSS v4 | Bento Grid layout & 3D CSS animations |

---

## 🚦 Quickstart Guide

### 1. Start FastAPI Backend
```bash
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 2. Start React Frontend
```bash
cd frontend
npm install
npm run dev
```

### 3. Run Quality Gates & Tests
```bash
python3 -m unittest discover tests
bash scripts/ai_session_gate.sh
bash scripts/platinum_governance_check.sh
```

---

## 🏆 Hackathon Demo Flow (Live Showcase Script)

1. **Step 1: Explore Dashboard**: View the Bento Grid KPIs, student enrollment, and active attendance status.
2. **Step 2: Simulate Disruption**: Trigger "Teacher Absent" on Monday. Watch the OR-Tools engine reallocate staff in < 50ms.
3. **Step 3: Magic Dropzone**: Drop a messy/smudged handwritten form. Observe zero-shot VLM parsing and HITL routing.
4. **Step 4: Smart Kiosk**: Scan student QR cards with edge face tracking. Watch proxy scans get rejected and valid scans flash green.
