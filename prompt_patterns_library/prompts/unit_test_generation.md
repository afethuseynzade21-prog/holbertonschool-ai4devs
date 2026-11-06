# Unit Test Generation Prompt Template

**Role**: Act as a senior software test engineer with experience in [TEST_FRAMEWORK] and software testing best practices.

**Task**: Generate meaningful unit tests for the provided function, class, or module. Cover normal execution paths, boundary conditions, and relevant error cases. Follow the specified testing framework and avoid assuming behavior that is not defined.

**Input Placeholder**:
- Programming language: [LANGUAGE]
- Source code: [CODE_BLOCK]
- Testing framework: [TEST_FRAMEWORK]
- Expected behavior: [EXPECTED_BEHAVIOR]
- Dependencies or required mocks: [DEPENDENCIES_AND_MOCKS]

**Expected Output Format**:
1. Complete unit test code in a fenced code block.
2. Brief explanation of each test case.
3. Coverage of normal, boundary, and error scenarios.
4. Instructions for running the tests.
5. Any assumptions or requirements that need clarification.
