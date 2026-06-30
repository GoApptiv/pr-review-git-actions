# Functional Review Principles

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
7. Report any missing, partial, or incorrect implementation.

Do not assume implementation satisfies the Acceptance Criteria.

Provide explicit evidence from code.

---

## Acceptance Criteria Review

The AI must perform two independent reviews.

### Part A - Developer Acceptance Criteria

Review every Acceptance Criteria explicitly provided in the PR Description.

For every Acceptance Criteria provide:

### Acceptance Criteria

<Acceptance Criteria>

### Type

Developer

### Status

- Implemented
- Partially Implemented
- Not Implemented
- Not Verifiable

### Implementation Evidence

Identify implementation across the application layers:

- Validation Layer
- Controller / API
- Service Layer
- Repository Layer (if applicable)
- Database / Migration (if applicable)

### Functional Test Cases

Generate business-level functional test cases for this Acceptance Criteria.

For each test case provide:

| Test Scenario | Expected Result | Coverage Status |

Coverage Status:

- Covered
- Partially Covered
- Missing

### Gaps

Identify:

- Missing validations
- Missing business logic
- Missing edge case handling
- Missing error handling
- Missing authorization
- Missing automated tests
- Missing functional test coverage

If an Acceptance Criteria cannot be mapped to implementation:

Status: Not Implemented

or

Status: Not Verifiable

Reason:

Implementation evidence could not be found.

---

### Part B - AI Generated Acceptance Criteria

Analyze the Business Requirement and Functional Changes.

Identify important Acceptance Criteria that are reasonably implied by the business requirements but are NOT explicitly listed in the PR Description.

Do NOT invent arbitrary product requirements.

Generate only high-confidence Acceptance Criteria based on:

- Business workflow
- Validation rules
- Data integrity
- Security
- Authorization
- Duplicate processing
- Boundary conditions
- Error handling
- Transaction consistency
- Industry best practices

Every generated Acceptance Criteria MUST be clearly marked as:

Type: AI Generated

For every AI Generated Acceptance Criteria provide:

### Acceptance Criteria

<AI Generated Acceptance Criteria>

### Confidence

- High
- Medium

### Reason

Explain why this Acceptance Criteria is recommended.

### Status

- Already Implemented
- Partially Implemented
- Missing Implementation
- Product Decision Required

### Implementation Evidence

If implementation exists, identify:

- Validation Layer
- Controller / API
- Service Layer
- Repository Layer
- Database / Migration (if applicable)

### Functional Test Cases

Generate business-level functional test cases.

For each test case provide:

| Test Scenario | Expected Result | Coverage Status |

Coverage Status:

- Covered
- Partially Covered
- Missing

### Recommendation

One of:

- Add as Acceptance Criteria
- Discuss with Product Owner
- Optional Enhancement

---

### Requirement Traceability

At the end of the review generate a Requirement Traceability Matrix.

| Type | Requirement / Acceptance Criteria | Implementation Status | Test Coverage | Evidence |

Type:

- Business Requirement
- Developer Acceptance Criteria
- AI Generated Acceptance Criteria

Implementation Status:

- Implemented
- Partially Implemented
- Missing
- Not Verifiable

Test Coverage:

- Covered
- Partially Covered
- Missing

---

## Requirement Validation (Mandatory)

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

Provide implementation evidence.

If traceability cannot be established:

Status: Not Implemented

or

Status: Not Verifiable

Reason:
Implementation cannot be mapped to the requirement.

---

## Requirement & Acceptance Criteria Coverage Matrix (Mandatory)

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

## Requirement Coverage (Mandatory)

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

## Business Logic Validation (Mandatory)

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

## Edge Case Validation (Mandatory)

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