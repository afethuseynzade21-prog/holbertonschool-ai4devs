# Codebase Overview - COBOL Banking Transaction System (ACCT-TRANSACTION)

## Source
The provided example "Legacy COBOL System Modernization" (Banking Transaction System Migration). The analysis covers the COBOL program `ACCT-TRANSACTION` shown in the example. The example also contains a proposed Java Spring modernization, which is used here only to understand migration risks.

## Age
Not stated in the source material. The example describes a COBOL mainframe application but gives no release date or last-update date, so the age is documented as unknown instead of being guessed. The planned modernization timeline is 18 months (phased migration).

## Size
- **Production scale (stated):** about 50 million transactions per day.
- **Analyzed COBOL excerpt:** 80 lines (69 non-blank) in one program, `ACCT-TRANSACTION`.
  - 6 paragraphs are defined: `MAIN-PROCESS`, `INITIALIZE-PROGRAM`, `PROCESS-TRANSACTION`, `VALIDATE-ACCOUNT`, `VALIDATE-TRANSACTION`, `CHECK-WITHDRAWAL-LIMITS`.
  - 6 more paragraphs are called with `PERFORM` but their code is not included: `UPDATE-ACCOUNT-BALANCE`, `LOG-TRANSACTION`, `REJECT-TRANSACTION`, `REJECT-INVALID-ACCOUNT`, `CHECK-TRANSFER-LIMITS`, `CLEANUP-PROGRAM`.
- **Total size of the real system:** not stated.
- **Proposed Java Spring sample (target):** about 294 non-blank lines (entities, services, validator, controller, migration job and tests, including section headings).

## Structure
- **Data division:** three records - the account record (number, balance, status, type), the transaction record (ID, type, amount, timestamp) and three Y/N validation flags.
- **Procedure division:** `MAIN-PROCESS` initializes the flags, processes one transaction and stops. `PROCESS-TRANSACTION` validates the account, validates the transaction, then updates the balance and logs it, or rejects it.

## Dependencies
- COBOL program running on a mainframe.
- Embedded SQL (`EXEC SQL`) reading the `ACCOUNTS` table. The migration code in the example refers to the legacy database as DB2.
- Not visible in the excerpt: how the transaction input arrives, where the log is written, and which other programs call this one.
- Planned target stack: Java, Spring (REST controller, transactional services, scheduled jobs), JPA entities, a feature-toggle service for the gradual migration and a legacy adapter.

## Business rules found in the code
- An account is valid only if it exists (`SQLCODE = 0`) and its status is `A`.
- Three transaction types: `WD` (withdrawal), `DP` (deposit) and `TR` (transfer).
- Withdrawal is authorized only if the balance is at least the amount and the amount is at most 5000.00.
- Deposit is always authorized.
- Transfer rules are delegated to `CHECK-TRANSFER-LIMITS`, which is not included.

## Issues
- Business logic is incomplete in the excerpt (6 called paragraphs are missing), including balance update, logging, rejection and transfer rules.
- Withdrawal limit (5000.00) is hardcoded and does not depend on the account type.
- No visible locking or concurrency control around reading and updating the balance.
- Rejection reasons are not distinguished (missing account, inactive account and database errors are treated the same way).
- The balance field is unsigned, so negative balances cannot be represented.
- The transaction record has no destination account, although transfers (`TR`) exist.
- The flag `WS-BALANCE-SUFFICIENT` is declared and initialized but never set to `Y` or used.
- No tests or documentation for the COBOL program are included in the material.
