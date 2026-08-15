---
name: bmad-testarch-automate
description: 'Generates robust, maintainable automated tests across unit, integration, and API layers.'
---

# TestArch Automate

## Purpose
Generates high-fidelity automated tests with clean fixtures, parameterization, and robust assertions.

## Best Practices
1. **Fixture Isolation**: Ensure tests are idempotent and independent with clean teardown.
2. **Parameterized Tests**: Use `@pytest.mark.parametrize` or `test.each` for multi-variant testing.
3. **Explicit Assertions**: Use descriptive assertion messages explaining failure context.
4. **Mocking Boundaries**: Mock external network/I/O at system boundaries, never internal pure logic.
