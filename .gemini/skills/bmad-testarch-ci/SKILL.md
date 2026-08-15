---
name: bmad-testarch-ci
description: 'Integrates test execution, sharding, reporting, and quality gates into CI/CD pipelines.'
---

# TestArch CI Integration

## Purpose
Configures CI/CD workflows for rapid, reliable test execution and automated quality gate enforcement.

## Pipeline Standards
1. **Parallel Sharding**: Distribute tests across matrix workers for sub-5-minute feedback loops.
2. **Test Quarantine**: Isolate newly flaky tests while alerting owners without breaking main builds.
3. **Artifact Reporting**: Publish JUnit XML, HTML coverage reports, and failure screenshots.
4. **Blocking Quality Gates**: Block pull requests failing code coverage or security audit thresholds.
