# Test Failure Analysis Prompt Template

**Role**: Act as a senior test automation engineer experienced in debugging automated tests and analyzing software failures.

**Task**: Analyze the provided failing test and determine whether the failure is likely caused by an application defect, a test defect, or an environment/configuration issue. Separate confirmed facts from hypotheses. Do not claim a root cause without supporting evidence.

**Input Placeholder**:
- Test code: [TEST_CODE]
- Failure log or error message: [FAILURE_LOG]
- Application source code: [APPLICATION_CODE]
- Test environment: [ENVIRONMENT]
- Recent code or configuration changes: [RECENT_CHANGES]

**Expected Output Format**:
1. Brief failure summary.
2. Relevant evidence from the test code, logs, and application code.
3. Likely failure category: application defect, test defect, or environment issue, with confidence level and reasoning.
4. Step-by-step investigation plan.
5. Minimal suggested fix, if supported by the evidence.
6. Verification steps and commands for confirming the fix.
7. Any missing information or assumptions requiring clarification.
