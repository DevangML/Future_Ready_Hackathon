# AST Graph Summary (Token-Optimized)

- **Total Indexed Nodes**: 515
- **Indexed Files**: 54
- **Endpoints**: 14
- **UI Components**: 26
- **Estimated Context Token Savings**: ~91.4% vs full raw file ingestion

## Endpoints
- `GET /` (backend/app/main.py)
- `GET /api/dashboard/stats` (backend/app/main.py)
- `GET /api/timetable/generate` (backend/app/main.py)
- `POST /api/timetable/disruption` (backend/app/main.py)
- `POST /api/demo/reset` (backend/app/main.py)
- `POST /api/demo/mass-absence` (backend/app/main.py)
- `POST /api/document/process` (backend/app/main.py)
- `POST /api/document/parse` (backend/app/main.py)
- `GET /api/document/unreviewed` (backend/app/main.py)
- `POST /api/document/verify` (backend/app/main.py)
- `POST /api/kiosk/attendance` (backend/app/main.py)
- `GET /api/students` (backend/app/main.py)
- `GET /api/staffing/predict` (backend/app/main.py)
- `GET /api/students/predict-risk` (backend/app/main.py)

## Key Components
- `<App />` in `frontend/src/App.jsx`
- `<ArchitectureDrawer />` in `frontend/src/components/ArchitectureDrawer.jsx`
- `<DashboardOverview />` in `frontend/src/components/DashboardOverview.jsx`
- `<Header />` in `frontend/src/components/Header.jsx`
- `<HumanReviewInbox />` in `frontend/src/components/HumanReviewInbox.jsx`
- `<IntroScreen />` in `frontend/src/components/IntroScreen.jsx`
- `<MagicDropzone />` in `frontend/src/components/MagicDropzone.jsx`
- `<ReactiveTimetable />` in `frontend/src/components/ReactiveTimetable.jsx`
- `<Sidebar />` in `frontend/src/components/Sidebar.jsx`
- `<Icon />` in `frontend/src/components/Sidebar.jsx`
- `<SmartKiosk />` in `frontend/src/components/SmartKiosk.jsx`
- `<SmartStaffing />` in `frontend/src/components/SmartStaffing.jsx`
- `<DEBUG />` in `dont-b-mad/hooks/post-skill/lib/dispatch.js`
- `<ENV_FILE />` in `dont-b-mad/hooks/post-skill/lib/dispatch.js`
- `<HOOK_FILE_LOG />` in `dont-b-mad/hooks/post-skill/lib/dispatch.js`
- `<PENDING_SKILL_FILENAME />` in `dont-b-mad/hooks/post-skill/lib/dispatch.js`
- `<QUEUE_FILE />` in `dont-b-mad/hooks/post-skill/lib/dispatch.js`
- `<QUEUE_FILE_TMP />` in `dont-b-mad/hooks/post-skill/lib/dispatch.js`
- `<QUEUE_FLUSH_LIMIT />` in `dont-b-mad/hooks/post-skill/lib/dispatch.js`
- `<INGEST_URL />` in `dont-b-mad/hooks/post-skill/lib/dispatch.js`
- `<GITLAB_CREDENTIAL_HOST />` in `dont-b-mad/hooks/post-skill/lib/dispatch.js`
- `<SKILL_EVENT_MAP />` in `dont-b-mad/hooks/post-skill/lib/dispatch.js`
- `<SUBPROCESS_TIMEOUT_MS />` in `dont-b-mad/hooks/post-skill/lib/dispatch.js`
- `<HOOK_MAX_RUNTIME_MS />` in `dont-b-mad/hooks/post-skill/lib/dispatch.js`
- `<QUEUE_FLUSH_LIMIT />` in `dont-b-mad/hooks/post-skill/lib/dispatch.queue.test.js`
- `<SKILL_EVENT_MAP />` in `dont-b-mad/hooks/post-skill/lib/dispatch.test.js`
