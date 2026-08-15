---
name: bmad-testarch-framework
description: 'Scaffolds and configures enterprise test frameworks, fixtures, runners, and coverage reporting.'
---

# TestArch Framework

## Purpose
Sets up and standardizes testing infrastructure across repositories.

## Standard Configurations
- **Python**: `pytest`, `pytest-asyncio`, `pytest-cov`, `pytest-xdist`, `hypothesis`.
- **Node/TS**: `Vitest` / `Jest`, `Playwright`, `@testing-library`.
- **Configuration Files**: `pytest.ini`, `pyproject.toml`, coverage configuration (`.coveragerc`).
- **Fixtures Directory**: Shared mock servers, database test harnesses, and session factories.
