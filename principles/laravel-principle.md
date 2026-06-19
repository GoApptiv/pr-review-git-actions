# Laravel Principles

## Naming Conventions (Mandatory)

### Class-Level Naming (PascalCase)

- Classes
- Interfaces
- Traits
- Enums

Examples:

✔ UserService
✔ InvoiceRepository
✔ FraudDetectionService

### Methods, Functions & Parameters (camelCase)

✔ calculateReward()
✔ getCustomerInvoices()

✔ customerId
✔ invoiceAmount

### Variables & Properties (camelCase)

✔ totalInvoiceAmount
✔ eligibleCustomerCount

### Constants (UPPER_SNAKE_CASE)

✔ MAX_RETRY_COUNT
✔ DEFAULT_PAGE_SIZE

### Semantic Naming Rules

Functions MUST:

- Clearly describe business purpose
- Reflect actual behavior
- Match parameter intent

Variables MUST:

- Represent business meaning
- Avoid ambiguity

Flag:

- Generic names (temp, data, obj, value)
- Meaningless abbreviations
- Function names that do not reflect behavior
- Variable names lacking business meaning

---

### Forbidden Naming Patterns

Avoid vague or non-descriptive names such as:

❌ temp  
❌ data  
❌ value  
❌ obj  
❌ result (without context)  
❌ process()  
❌ handle()  
❌ manage()  
❌ doSomething()  

---

### Quality Rules

Flag:

- Inconsistent naming conventions
- Abbreviations that reduce readability (e.g., invAmt, custDtls)
- Generic or non-descriptive names
- Function names that do not reflect behavior
- Variables that do not represent clear business meaning

---

## Migration Review (Mandatory)

Verify:

- Migrations are reversible
- Existing data is protected
- Large table operations are safe
- Index changes are considered

Flag:

- Destructive migrations
- Table locking risks
- Long-running operations

---

## Laravel Best Practices (Mandatory)

Verify:

- Laravel conventions are followed
- Eloquent relationships are used appropriately
- Dependency Injection is preferred
- Configuration values are loaded from config files
- Form Request validation is used where appropriate

Flag:

- Usage of env() outside config files
- Direct use of request() helper in services
- Direct use of DB facade where repository exists
- Hardcoded configuration values