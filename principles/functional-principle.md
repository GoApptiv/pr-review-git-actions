# Functional Review Standards

The PR Description is mandatory and is the primary source of truth for functional review.

The PR Description should ideally contain:

- Business Requirement
- Functional Changes
- Acceptance Criteria

If the PR Description does not follow the recommended format, attempt to infer and extract requirements from the available content.

Do not fail the review solely because the format is different.

Functional review may proceed if sufficient requirement context is available.

Requirements may be defined in:

- Business Requirement
- Functional Changes
- Acceptance Criteria
- Other clearly stated functional expectations in the PR Description

All identified requirements must be validated against the implementation.

---

## PR Description Quality Assessment

Before performing functional review, assess the quality of the PR Description.

### High Quality

Contains:

- Business Requirement
- Functional Changes
- Acceptance Criteria

Functional Review Confidence: High

---

### Medium Quality

Contains:

- Partial requirements
- Functional expectations
- Missing or incomplete Acceptance Criteria

Functional Review Confidence: Medium

Proceed with review and identify missing information.

---

### Low Quality

Contains:

- Technical implementation details only
- Generic statements such as:
  - Bug Fix
  - API Changes
  - Refactoring
  - Minor Improvements

Functional Review Confidence: Low

Requirement validation is limited.

---

## If PR Description Is Missing or Insufficient

If no meaningful business or functional context can be extracted:

- Do NOT perform requirement validation.
- Do NOT assume business logic.
- Perform only technical review.
- State that functional review could not be completed due to insufficient requirement context.

Add comment:

> Insufficient functional context found in the PR description. Please provide Business Requirement, Functional Changes, and Acceptance Criteria and request a re-review.

Also mention:

- Requirement validation skipped.
- Acceptance Criteria validation skipped.
- Business logic validation skipped.
- Functional review confidence is low.

---

## Requirement Extraction

Extract all requirements from:

- Business Requirement
- Functional Changes
- Acceptance Criteria

Create a consolidated list of functional requirements.

Verify implementation against the complete requirement set.

Do not assume all requirements are explicitly listed as Acceptance Criteria.

---

## Acceptance Criteria Validation (Mandatory)

Acceptance Criteria are mandatory verification points and must be reviewed independently.

For every Acceptance Criteria:

1. Extract the Acceptance Criteria.
2. Identify the implementation responsible for satisfying it.
3. Verify the implementation fully satisfies the Acceptance Criteria.
4. Verify validations required by the Acceptance Criteria exist.
5. Verify error handling exists where applicable.
6. Verify edge cases related to the Acceptance Criteria are handled.
7. Verify test coverage exists for the Acceptance Criteria.
8. Report any missing, partial, or incorrect implementation.

Do not assume implementation satisfies the Acceptance Criteria.

Provide explicit evidence from code.

---

For every Acceptance Criteria provide:

### Acceptance Criteria

<Acceptance Criteria>

### Status

- Implemented
- Partially Implemented
- Not Implemented
- Not Verifiable

### Implementation Evidence

Identify:

- Validation Layer
- Controller / API
- Service Layer
- Repository Layer (if applicable)

### Test Coverage

Identify:

- Unit Tests
- Feature Tests
- Integration Tests

### Gaps

List:

- Missing validations
- Missing logic
- Missing tests
- Missing edge case handling

If an Acceptance Criteria cannot be mapped to implementation:

Status: Not Implemented

or

Status: Not Verifiable

Reason:
Implementation evidence could not be found.

---

## Requirement Validation

For every identified requirement:

- Verify implementation exists.
- Verify validation rules exist.
- Verify business logic exists.
- Verify error handling exists.
- Verify edge cases are considered.
- Verify tests exist where applicable.

Identify:

- Missing requirements
- Partially implemented requirements
- Incorrect implementations
- Incorrect interpretation of requirements

---

## Requirement Traceability (Mandatory)

For every requirement establish traceability:

Requirement
→ Validation Layer
→ Controller / API
→ Service Layer
→ Repository Layer (if applicable)
→ Test Coverage

Provide implementation evidence.

If traceability cannot be established:

Status: Not Implemented

or

Status: Not Verifiable

Reason:
Implementation cannot be mapped to the requirement.

---

## Requirement & Acceptance Criteria Coverage Matrix

Provide a summary table:

| Item | Type | Status | Validation | Logic | Tests |
|--------|--------|--------|--------|--------|--------|

### Type

- Business Requirement
- Functional Change
- Acceptance Criteria

### Status

- Implemented
- Partially Implemented
- Not Implemented
- Not Verifiable

---

## Requirement Coverage

Verify:

- All requirements are implemented.
- All acceptance criteria are satisfied.
- No requirement is missed.
- No requirement is partially implemented.
- No functionality described in the PR description is ignored.

Identify:

- Missing functionality.
- Partial implementations.
- Incorrect interpretations.
- Unimplemented requirements.

---

## Business Logic Validation

Verify:

- Logic matches stated requirements.
- Calculations are accurate.
- Validation rules are correct.
- Status transitions are correct.
- Workflow rules are correct.
- Authorization rules match requirements.
- Eligibility conditions match requirements.
- Business constraints are enforced correctly.

Flag:

- Logic defects.
- Incorrect calculations.
- Business rule violations.
- Missing validations.
- Missing workflow enforcement.

---

## Edge Case Validation

For every requirement verify handling of:

- Null inputs
- Empty inputs
- Invalid inputs
- Existing records
- Duplicate requests
- Concurrent requests
- Boundary values
- Large datasets
- Failure scenarios
- Retry scenarios

Identify:

### Covered Edge Cases

- ...

### Missing Edge Cases

- ...

---

## Test Coverage Validation

Verify test coverage exists for:

- Happy Path scenarios
- Validation failures
- Business rule failures
- Edge cases
- Authorization scenarios
- Permission scenarios
- Negative scenarios
- Failure scenarios
- Regression scenarios

Suggest missing test cases.

---

## Regression Risk Assessment

Identify:

- Existing functionality impacted
- Integration risks
- Deployment risks
- Data migration risks
- API contract risks
- Backward compatibility risks

Provide:

### Risk Level

- Low
- Medium
- High

### Reason

...

### Potential Impact

...

### Rollback Complexity

...

---

## Additional Functional Review Rules

- Do not mark a requirement as Implemented unless implementation evidence is identified.
- Do not mark an Acceptance Criteria as Implemented unless implementation evidence is identified.
- If implementation evidence, validation evidence, or test evidence is missing, clearly report the gap.
- Missing tests should reduce confidence but should not automatically mark a requirement as unimplemented.
- Missing business logic or missing validation should result in Partially Implemented or Not Implemented status.
- Explicitly call out assumptions made during review.
- Prefer evidence-based findings over assumptions.