# Benchmark Tasks

## Project: Copilot Productivity Sprint

### Purpose

These benchmark tasks will be completed twice:

- **Series A:** Without AI assistance.
- **Series B:** With AI assistance using Cursor's built-in AI assistant.

The same tasks, requirements, and acceptance criteria will be used in both series to compare development time, code quality, and productivity.

**Technology:** JavaScript and Node.js

---

## Task 1: User Input Validation

**Estimated time:** 15–20 minutes

### Requirements
Create a JavaScript function that validates user registration information.

The function must:
- Check that the user's name is not empty.
- Check that the email has a valid format.
- Check that the password contains at least 8 characters.
- Return validation errors when one or more fields are invalid.

### Inputs
An object containing:
- `name`
- `email`
- `password`

### Outputs
An object containing:
- `isValid` — a boolean indicating whether the input is valid.
- `errors` — an array of validation error messages.

### Acceptance Criteria
- Valid input returns `isValid: true`.
- Invalid input returns `isValid: false`.
- All applicable validation errors are returned.
- The function handles missing or empty fields without crashing.

---

## Task 2: User Management API

**Estimated time:** 20–30 minutes

### Requirements
Create a simple Express.js API endpoint for registering a new user.

The endpoint must:
- Accept a POST request at `/users`.
- Receive a user's name and email.
- Validate that both fields are provided.
- Return an appropriate HTTP status code.
- Return the created user's information in the response.

### Inputs
A JSON request body containing:
- `name`
- `email`

### Outputs
- `201 Created` when the user is successfully created.
- `400 Bad Request` when required fields are missing.
- A JSON response containing the created user's information or an error message.

### Acceptance Criteria
- The endpoint accepts valid user data.
- The endpoint rejects requests with missing fields.
- The response uses the correct HTTP status code.
- The response is returned in JSON format.

---

## Task 3: Bug Fixing and Unit Testing

**Estimated time:** 15–25 minutes

### Requirements
Fix a JavaScript function that calculates the average of an array of numbers.

The function must:
- Calculate the correct average.
- Handle an empty array.
- Handle arrays containing positive and negative numbers.
- Include unit tests for normal and edge cases.

### Inputs
An array of numbers, for example:

`[10, 20, 30]`

### Outputs
The calculated average.

For an empty array, the function must return `0`.

### Acceptance Criteria
- `[10, 20, 30]` returns `20`.
- `[5, -5]` returns `0`.
- An empty array returns `0`.
- Unit tests cover normal and edge cases.
- All tests pass.

---

## Benchmark Comparison

Each task will be completed in both development series using the same requirements.

The following metrics will be recorded:

- Completion time.
- Lines of code.
- Number of errors or failed tests.
- Code quality and readability.

The results will be compared to evaluate the impact of AI assistance on development productivity.
