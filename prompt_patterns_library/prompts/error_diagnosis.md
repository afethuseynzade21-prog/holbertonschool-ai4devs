# Error Diagnosis Prompt Template

**Role**: Act as an experienced software debugging engineer specializing in [LANGUAGE] and [FRAMEWORK].

**Task**: Analyze the reported error using the provided error message, stack trace, source code, and environment details. Identify the most likely root cause, distinguish confirmed facts from assumptions, and recommend a minimal and reliable solution.

**Input Placeholder**:
- Programming language: [LANGUAGE]
- Framework or library: [FRAMEWORK]
- Error message and stack trace: [ERROR_LOG]
- Relevant source code: [CODE_BLOCK]
- Environment and versions: [ENVIRONMENT]
- Troubleshooting steps already attempted: [ATTEMPTED_FIXES]

**Expected Output Format**:
1. Clear explanation of the reported error.
2. Most likely root cause with supporting evidence.
3. Other possible causes, if relevant.
4. Corrected code or commands in a fenced code block.
5. Step-by-step instructions to verify the solution.
6. Any remaining assumptions or missing information.
