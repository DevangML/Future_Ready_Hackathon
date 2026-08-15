---
name: bmad-testarch-trace
description: 'Generates and validates Requirements-to-Test Traceability Matrices across PRDs, epics, and test suites.'
---

# TestArch Traceability Matrix

## Purpose
Maps every requirement and acceptance criterion from PRDs and stories to automated test cases.

## Workflow
1. **Extract Requirements**: Parse acceptance criteria and business rules from the specification.
2. **Scan Test Suites**: Identify corresponding `@pytest.mark` or test function signatures.
3. **Generate Matrix**: Produce a Markdown table matching Requirement ID -> Story -> Test Path -> Status.
4. **Report Gaps**: Highlight untested requirements, partial verifications, or orphan tests.
