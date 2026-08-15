---
name: bmad-testarch-atdd
description: 'Acceptance Test-Driven Development workflow. Crafts Given-When-Then executable test specifications.'
---

# TestArch ATDD (Acceptance Test-Driven Development)

## Purpose
Transforms business acceptance criteria into executable test skeletons before implementation begins.

## Workflow Steps
1. **Story Elaboration**: Review user story acceptance criteria with product owner lens.
2. **Gherkin Formulation**: Write clear Given-When-Then scenarios covering happy, alternative, and error flows.
3. **Test Skeleton Generation**: Create executable test stubs using `pytest` or Jest with parameter fixtures.
4. **Handoff to Dev**: Pass executable failing tests to the implementation agent.
