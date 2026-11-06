# Prompt Use Cases

This document identifies common situations where reusable prompt patterns can improve AI-assisted software development workflows.

## 1. Code Quality

### Refactoring
- **Goal:** Improve code readability, maintainability, and efficiency without changing existing functionality.
- **Input:** Source code in [LANGUAGE].
- **Output:** Refactored code with an explanation of the improvements.
- **Validation:** Verify that the refactored code preserves the original behavior.

### Style and Convention Enforcement
- **Goal:** Ensure that code follows consistent naming conventions, formatting rules, and language-specific best practices.
- **Input:** Source code and the applicable style guidelines.
- **Output:** Revised code that follows the specified conventions.
- **Validation:** Check the code against the project's style guidelines or linter.

### Performance Review
- **Goal:** Identify inefficient operations and suggest performance improvements.
- **Input:** Source code, expected workload, and performance requirements.
- **Output:** Performance findings and optimized code suggestions.
- **Validation:** Compare execution time and resource usage before and after optimization.

## 2. Debugging and Troubleshooting

### Error Diagnosis
- **Goal:** Identify the root cause of an error and recommend a reliable solution.
- **Input:** Error message, stack trace, and relevant source code.
- **Output:** Explanation of the error and corrected code.
- **Validation:** Run the corrected code and confirm that the error is resolved.

### Bug Reproduction and Isolation
- **Goal:** Reproduce a reported bug and identify the smallest code section responsible for it.
- **Input:** Bug description, steps to reproduce, expected behavior, and actual behavior.
- **Output:** Reproduction steps and an isolated explanation of the problem.
- **Validation:** Confirm that the issue can be reproduced consistently.

### Regression Analysis
- **Goal:** Determine whether a recent code change introduced a new defect.
- **Input:** Previous and current code versions, test results, and bug description.
- **Output:** Potential regression source and recommended corrective actions.
- **Validation:** Run relevant tests against the updated code.

## 3. Documentation

### API Documentation
- **Goal:** Generate clear and structured documentation for API endpoints.
- **Input:** API source code, endpoint definitions, parameters, and response examples.
- **Output:** API documentation describing methods, parameters, responses, and possible errors.
- **Validation:** Verify that documented endpoints and parameters match the implementation.

### README Generation
- **Goal:** Create a useful README file that explains how to understand, install, configure, and run a project.
- **Input:** Project structure, dependencies, configuration details, and execution instructions.
- **Output:** A structured README.md file.
- **Validation:** Follow the installation and execution instructions in a clean environment.

### Code Explanation
- **Goal:** Explain complex code in a way that developers with different experience levels can understand.
- **Input:** Source code and target audience experience level.
- **Output:** A step-by-step explanation of the code's purpose, logic, and important components.
- **Validation:** Check that the explanation accurately represents the implementation.

## 4. Testing

### Unit Test Generation
- **Goal:** Generate unit tests for individual functions or modules.
- **Input:** Source code, expected behavior, and testing framework.
- **Output:** Unit tests covering normal cases, edge cases, and error conditions.
- **Validation:** Execute the tests and verify that they pass.

### Test Case Design
- **Goal:** Identify test scenarios that provide meaningful coverage of functional requirements.
- **Input:** Feature description, requirements, and acceptance criteria.
- **Output:** A structured list of positive, negative, boundary, and edge-case test scenarios.
- **Validation:** Confirm that each important requirement is covered by at least one test case.

### Test Failure Analysis
- **Goal:** Analyze failing tests and identify whether the cause is in the implementation, test logic, or environment.
- **Input:** Test code, failure output, stack trace, and relevant application code.
- **Output:** Failure analysis and recommended fixes.
- **Validation:** Re-run the affected tests and confirm that the failure is resolved.

## Reusable Prompt Design Principles

- Define the task and expected outcome clearly.
- Provide relevant context and input data.
- Use explicit placeholders for project-specific information.
- Specify the required output format.
- Include constraints and validation criteria.
- Ask the AI assistant to identify assumptions instead of inventing missing information.
