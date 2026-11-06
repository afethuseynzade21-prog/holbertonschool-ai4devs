# Bug Reproduction and Isolation Prompt Template

**Role**: Act as a senior software test engineer specializing in bug reproduction and defect isolation.

**Task**: Analyze the reported bug, create a repeatable procedure to reproduce it, and identify the smallest component or condition associated with the failure. Do not assume missing information or invent reproduction results.

**Input Placeholder**:
- Bug description: [BUG_DESCRIPTION]
- Steps to reproduce: [REPRODUCTION_STEPS]
- Expected behavior: [EXPECTED_BEHAVIOR]
- Actual behavior: [ACTUAL_BEHAVIOR]
- Relevant source code: [CODE_BLOCK]
- Logs and environment details: [LOGS_AND_ENVIRONMENT]

**Expected Output Format**:
1. Preconditions required to reproduce the bug.
2. Numbered reproduction steps.
3. Expected versus actual behavior.
4. Suspected component or triggering condition, with supporting evidence.
5. Additional information needed if the cause is unclear.
6. Suggested regression test to prevent the bug from returning.
