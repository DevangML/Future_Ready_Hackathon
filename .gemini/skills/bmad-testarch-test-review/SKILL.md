---
name: bmad-testarch-test-review
description: 'Adversarial review of test suites to identify flaky tests, coverage gaps, and test smells.'
---

# TestArch Test Review

## Purpose
Performs critical evaluation of existing test suites to ensure test efficacy and maintainability.

## Review Checklist
1. **Assertion Strength**: Check for weak assertions (`assert result is not None`) vs exact state validation.
2. **Flakiness Vectors**: Detect sleep timers, unpinned dates/times, shared mutable state, network leaks.
3. **Negative Test Coverage**: Verify error branches, exception types, and status codes are asserted.
4. **Execution Speed**: Identify bottlenecks in test suite runtime and optimize fixture scopes.
