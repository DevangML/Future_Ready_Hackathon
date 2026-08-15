---
name: platform-quality-guidelines
description: 'Enterprise engineering quality standards, clean code rules, LOC limits, and review gates.'
---

# Platform Quality Guidelines

## Purpose
Defines mandatory engineering and quality guidelines across the entire platform ecosystem.

## Core Rules
1. **File Size Cap**: Strict hard limit of <= 200 LOC per file. If a file grows, split into cohesive sub-modules.
2. **Clean Architecture**: Separation of concerns between Data, Business Logic, and UI presentation.
3. **Zero Lint Errors**: Code must pass flake8, ESLint, and Semgrep with zero errors or warnings.
4. **Test Coverage**: Minimum 90% branch test coverage for core business logic.
5. **Documentation**: Every public function and class must include type annotations and clear docstrings.
