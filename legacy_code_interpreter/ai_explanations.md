# AI Explanations - ACCT-TRANSACTION (COBOL)

Five complex sections of the legacy program, explained in plain English with patterns, issues and improvements. Explanations were generated with an AI assistant and checked against the source code.

## Section 1 - PROCESS-TRANSACTION (main decision flow)

- **Plain English**: First the program checks the account. If the account is valid, it checks the transaction. If the transaction is authorized, it updates the balance and logs the transaction. If the transaction is not authorized, it rejects it. If the account is not valid, it rejects the request as an invalid account.
- **Pattern**: Nested `IF / ELSE` blocks controlled by Y/N flags (`WS-ACCOUNT-VALID`, `WS-TXN-AUTHORIZED`) stored in shared working storage. `PERFORM` works like calling a function without parameters or a return value.
- **Issues**:
  - All steps communicate through global flags, so any paragraph can change them.
  - The rejection path does not say why the request failed.
  - Failure cases are collapsed into one "invalid account" branch.
- **Improvements**: Return a result object with a reason code instead of flags, use early exits (guard clauses) instead of deep nesting, and keep one rejection path per reason. The Java sample moves in this direction with `ValidationResult`.

## Section 2 - VALIDATE-ACCOUNT (embedded SQL)

- **Plain English**: The program reads the account row from the `ACCOUNTS` table. The account is accepted only if the database call succeeded (`SQLCODE = 0`) and the status is `A` (active).
- **Pattern**: Embedded SQL with host variables (`:WS-ACCT-NUMBER` and others) and a success flag set to `Y`.
- **Issues**:
  - The `SELECT ... INTO` writes into the same host variable that is used in the `WHERE` clause, so the input value is overwritten by the result.
  - Any `SQLCODE` other than 0 (account not found, or a real database error) is treated like an inactive account.
  - Every status other than `A` (suspended, closed, and so on) is handled the same way.
  - The query has no row lock, so the balance can change between this read and the later update (the update code is not in the excerpt).
- **Improvements**: Separate "not found", "inactive" and "system error", log database errors, and lock the row or use a version check when the balance is updated. In the Java sample, `orElseThrow` and `isActive()` cover the first two cases.

## Section 3 - VALIDATE-TRANSACTION (EVALUATE on transaction type)

- **Plain English**: The program chooses the rule by transaction type. A withdrawal (`WD`) goes through the withdrawal limit check. A deposit (`DP`) is always authorized. A transfer (`TR`) goes through the transfer limit check.
- **Pattern**: `EVALUATE` is COBOL's `switch`. The default result is "not authorized" because the flag was initialized to `N`.
- **Issues**:
  - There is no `WHEN OTHER`, so an unknown type is rejected silently without a reason.
  - A deposit has no checks at all (for example, a zero amount).
  - Two-letter codes (`WD`, `DP`, `TR`) are repeated as plain text instead of named constants.
- **Improvements**: Use named values (enums) for transaction types, add an explicit default branch with a clear error, and validate that the amount is positive. The Java sample does this with `TransactionType` and the "Amount must be positive" rule.

## Section 4 - CHECK-WITHDRAWAL-LIMITS (business rule)

- **Plain English**: A withdrawal is authorized only when the account balance is at least the requested amount and the amount is not more than 5000.00.
- **Pattern**: Two nested `IF` statements and a hardcoded constant (`5000.00`).
- **Issues**:
  - The limit is hardcoded, so changing it needs a code change and a new release.
  - The limit is the same for every account type, although the account type is loaded from the database.
  - There is no daily limit, and no reason is returned when a check fails.
- **Improvements**: Move limits to configuration per account type and return the failed rule. The Java sample reads limits from `BusinessRulesService` and also adds a daily withdrawal limit, which does not exist in the COBOL code, so this is a behavior change that the business must confirm before migration.

## Section 5 - Data Division (record and flag definitions)

- **Plain English**: The program describes its data in fixed-width fields. The account has a 10-digit number, a balance with up to 10 digits before the decimal point and 2 after, a 1-character status and a 2-character type. The transaction has a 12-digit ID, a 2-character type, an amount with up to 8 digits plus 2 decimals and a 14-character timestamp. Three 1-character flags (`Y` or `N`) hold validation results.
- **Pattern**: Fixed-width `PIC` clauses, decimals stored as exact fixed-point numbers, status and type stored as short codes, flags stored as text.
- **Issues**:
  - The balance and amount are unsigned (`PIC 9`), so a negative balance (for example, an overdraft or credit account) cannot be stored.
  - The timestamp is plain text (`PIC X(14)`) with no validation.
  - The transaction record has no destination account, although transfers exist.
  - `WS-BALANCE-SUFFICIENT` is never set to `Y` and never used.
  - The account number is numeric in COBOL but a `String` in the Java sample, so leading zeros and formatting rules must be handled carefully.
- **Improvements**: Use `BigDecimal` with matching precision (the Java sample uses precision 12, scale 2 for the balance and precision 10, scale 2 for the amount, which matches the COBOL sizes), use enums for status and type, store timestamps as real date-time values, and remove unused fields.
