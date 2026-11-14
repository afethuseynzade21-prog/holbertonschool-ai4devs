# Risk Assessment - COBOL Banking Transaction System (ACCT-TRANSACTION)

Risks found in the provided COBOL program and in the proposed Java Spring modernization. Severity: Low, Medium or High.

| Risk | Severity | Notes |
|---|---|---|
| Incomplete business logic in the analyzed code | High | 6 paragraphs are called but not shown: `UPDATE-ACCOUNT-BALANCE`, `LOG-TRANSACTION`, `REJECT-TRANSACTION`, `REJECT-INVALID-ACCOUNT`, `CHECK-TRANSFER-LIMITS`, `CLEANUP-PROGRAM`. Rules cannot be fully extracted or migrated without them. |
| No visible concurrency control on balance updates | High | The account `SELECT` has no row lock, and the update code is not shown. With about 50 million transactions per day, two simultaneous withdrawals could both pass the balance check. The Java entity in the sample has no version field either. |
| Transfer rules and data are missing | High | Transfers (`TR`) exist, but the transaction record has no destination account and `CHECK-TRANSFER-LIMITS` is not shown. The Java sample also does not show `processTransfer` and `validateTransfer`. |
| Data synchronization can overwrite newer data | High | The scheduled job copies legacy account data into the modern database every 5 minutes for migrated accounts. If the modern service changes a balance first, the next sync can replace it with older legacy data. |
| Rejection reasons are mixed together | Medium | In `VALIDATE-ACCOUNT`, any `SQLCODE` other than 0 and any status other than `A` lead to the same invalid-account rejection. Database errors are not separated from inactive or missing accounts. |
| Business-rule changes in the Java version | Medium | The COBOL withdrawal rule is balance >= amount and amount <= 5000.00. The Java sample adds a daily withdrawal limit and per-account-type limits, which are not in the COBOL code. Some helper methods (for example, `getDailyWithdrawalTotal`) are also not shown. |
| Unhandled inactive-account exception in the Java service | Medium | `InactiveAccountException` is thrown but only `AccountNotFoundException`, `InsufficientFundsException` and a generic `Exception` are caught. An inactive account becomes a generic error instead of a normal rejection like `REJECT-INVALID-ACCOUNT`. |
| Hardcoded withdrawal limit | Medium | `5000.00` is written directly in `CHECK-WITHDRAWAL-LIMITS` for every account type. Changing it needs a code change and a release. |
| Unsigned balance and amount fields | Medium | `PIC 9(10)V99` and `PIC 9(8)V99` cannot store negative values. The Java sample has a `CREDIT` account type, which may need negative balances. |
| Data type differences between COBOL and Java | Medium | Account number is numeric in COBOL and a `String` in Java (leading zeros), and the timestamp is a 14-character text field in COBOL but a `LocalDateTime` in Java. Conversion mistakes can cause lookup or reporting errors. |
| No tests or documentation for the legacy program | Medium | The material includes tests only for the new Java service. There is no way to prove that the COBOL behavior is preserved without characterization tests. |
| Unknown transaction type is rejected silently | Low | `EVALUATE` has no `WHEN OTHER`. The default result is "not authorized" because the flag starts as `N`, but no reason is recorded. |
| Unused flag `WS-BALANCE-SUFFICIENT` | Low | The flag is initialized to `N` and never used. It is dead code that can confuse maintainers. |
