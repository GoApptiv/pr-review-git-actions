# Engineering Principles

## Code Hygiene & Maintainability (Mandatory)

Verify:

- No syntax issues
- No breaking changes
- No linting violations
- No unused imports
- No unused variables
- No unused functions/methods
- No unreachable code
- No duplicate code
- No commented-out code left behind
- No unnecessary abstractions

Suggest:

- Simpler implementations
- More reusable code
- Reduced complexity
- Improved readability

Flag:

- Dead code
- Code smells
- Excessive nesting
- Overly complex methods

---

## Architecture & Design (Mandatory)

Verify:

- SOLID principles are followed
- Separation of concerns is maintained
- Low coupling and high cohesion
- Existing project architecture is respected
- New code follows established patterns

Suggest:

- Suitable design patterns where beneficial
- Reusable abstractions
- Better extensibility

Flag:

- Architecture violations
- God classes/services
- Tight coupling
- Business logic spread across multiple layers

---

## Layer Responsibility Validation (Mandatory)

Follow Repository Pattern strictly.

### Controllers

Should:

- Validate requests
- Call services
- Return responses

Should NOT:

- Contain business logic
- Execute queries
- Perform calculations

### Services

Should:

- Contain business logic
- Coordinate workflows
- Handle transactions

Should NOT:

- Execute raw queries
- Access request objects directly

### Repositories

Should:

- Encapsulate query logic
- Handle database access

Should NOT:

- Contain business rules

---

## Null Safety & Defensive Coding (Mandatory)

Verify:

- Null values are handled safely
- Optional values are validated
- Missing data scenarios are considered
- External dependencies are validated

Flag:

- Potential null pointer exceptions
- Unsafe assumptions
- Undefined property/index access

---

## Performance Review (Mandatory)

Verify:

- No unnecessary database calls
- No redundant processing
- No excessive memory usage
- Efficient collection handling
- Efficient loops and iterations

Flag:

- Performance bottlenecks
- Inefficient algorithms
- Scalability concerns

---

## Error Handling & Resilience (Mandatory)

Verify:

- Exceptions are handled appropriately
- Failures are logged
- External service failures are handled gracefully
- Retries are implemented where appropriate
- Timeouts are configured where needed

Flag:

- Unhandled exceptions
- Missing fallback logic
- Reliability risks

---

## API Review (Mandatory)

Verify:

- Request validation exists
- Response structures remain consistent
- Proper HTTP status codes are used
- Error responses are standardized
- API contracts remain backward compatible

Flag:

- Breaking changes
- Missing validations
- Inconsistent response formats

---

## Security (Mandatory)

Verify:

### Authentication

- Protected routes require authentication
- Unauthorized access is prevented

### Authorization

- User permissions are validated
- Role-based access is enforced

### Data Protection

- No hardcoded secrets
- No hardcoded credentials
- No exposed API keys
- Sensitive data is masked

### Error Handling

- Internal implementation details are not exposed
- Stack traces are not returned to users
- Sensitive information is not leaked

### Input Validation

- Requests are validated
- User inputs are sanitized
- Injection risks are mitigated

Flag any security vulnerabilities.

---

## Database Review (Mandatory)

Verify:

### Query Quality

- Queries are optimized
- N+1 issues are avoided
- Proper eager loading is used
- Index usage is considered

### Data Integrity

- Transactions are used where required
- Referential integrity is maintained

### Scalability

- Large datasets are handled efficiently
- Batch processing is used where appropriate

Flag:

- Full table scans
- Repeated queries
- Missing transactions

---

## Observability & Logging (Mandatory)

Verify:

- Critical business events are logged
- Errors are logged with sufficient context
- Logs are actionable
- Sensitive information is not logged

Flag:

- Missing logs
- Excessive logging
- Logging of secrets or personal data

---

## Concurrency & Data Integrity (Mandatory)

Verify:

- Concurrent updates are handled safely
- Duplicate processing is prevented
- Transactions protect critical operations
- Idempotency is maintained where required

Flag:

- Race conditions
- Duplicate processing risks
- Missing transactional boundaries

---

## Backward Compatibility (Mandatory)

Verify:

- Existing APIs remain compatible
- Existing integrations continue to work
- Existing consumers are not impacted
- Schema changes are backward compatible

Flag:

- Breaking API changes
- Contract changes
- Risky schema changes