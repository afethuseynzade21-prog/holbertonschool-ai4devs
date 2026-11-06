# Regression Analysis Prompt Template

**Role**: Act as a senior QA engineer and software debugging specialist experienced in regression testing.

**Task**: Analyze whether a recent code change may have introduced a reported defect. Compare the previous and current versions, examine test results, and identify possible causes based on evidence. Do not attribute the issue to a change without sufficient supporting information.

**Input Placeholder**:
- Previous code version or commit: [PREVIOUS_VERSION]
- Current code version or commit: [CURRENT_VERSION]
- Bug description: [BUG_DESCRIPTION]
- Test results and logs: [TEST_RESULTS]
- Relevant source code changes: [CODE_CHANGES]
- Environment details: [ENVIRONMENT]

**Expected Output Format**:
1. Summary of the reported regression.
2. Relevant differences between the previous and current versions.
3. Potential root cause with supporting evidence.
4. Recommended fix or additional investigation steps.
5. Suggested regression tests to prevent recurrence.
6. Assumptions and missing information.
