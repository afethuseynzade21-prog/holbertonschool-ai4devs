# Bug Descriptions — Prompting Debug Assistant (Task 0)

## Purpose

This folder contains five intentionally buggy programs for debugging practice. Each example is between 10 and 40 lines and demonstrates a different error category required by the task.

## Bug inventory

| File | Language | Required error category | Intended behavior |
|---|---|---|---|
| `bug1.py` | Python | Syntax error | Calculate the arithmetic mean of a list of scores; return `0` for an empty list. |
| `bug2.py` | Python | Logical error | Return the largest integer in a list, including when all values are negative. |
| `bug3.py` | Python | Runtime exception | Find an email by username; show a friendly message if the username is not found. |
| `bug4.js` | JavaScript | Off-by-one / loop logic | Return the last `n` array elements in their original order; return the whole array when `n` equals its length. |
| `bug5.c` | C | Data type / library-function misuse | Read a line of up to 99 characters and print the number of entered characters, excluding the newline. |

## Reproduction context and expected outcomes

### 1. `bug1.py` — Syntax error
- **Scenario:** A student runs the score-average script.
- **Expected:** The program starts, calculates the average of `[78, 85, 92, 66]`, and prints `80.25`.
- **Observed:** Python reports a syntax error before the program can run.

### 2. `bug2.py` — Logical error
- **Scenario:** The function receives a list containing only negative numbers: `[-8, -3, -12, -5]`.
- **Expected:** It returns `-3`, the largest value.
- **Observed:** It returns an incorrect result (`0`).

### 3. `bug3.py` — Runtime exception
- **Scenario:** The program searches for username `samir`, which is not present in the sample user list.
- **Expected:** It prints a friendly “user not found” message and exits normally.
- **Observed:** The lookup returns no email, and the subsequent string operation raises an exception.

### 4. `bug4.js` — Off-by-one / loop logic
- **Scenario:** The function is called with `getLastItems(values, 3)` and `getLastItems(values, 5)`.
- **Expected:** The results are `["c", "d", "e"]` and `["a", "b", "c", "d", "e"]`.
- **Observed:** The loop omits the final array element from each result.

### 5. `bug5.c` — Data type / library-function misuse
- **Scenario:** A user enters a line containing spaces, for example `hello world`.
- **Expected:** The program reads the complete line and reports the number of characters entered (11 for `hello world`).
- **Observed:** The input operation reads only the first whitespace-delimited token, and the reported length is the buffer capacity rather than the number of entered characters. The unbounded `%s` conversion also does not safely enforce the stated 99-character input limit.

## Connection to the supplied reference materials

The examples are designed to be investigated using the debugging approaches in the supplied **Debug Assistant — Expert Prompts Collection**, especially:
- **Error Analysis & Root Cause Investigation** — identify the failure and trace it to its cause.
- **Bug Reproduction & Test Case Creation** — use the reproduction context and expected outcomes above to build test cases.
- **Live Production Issue Triage** and **Performance Debugging Deep-Dive** — useful investigation structures for larger real-world incidents, such as the supplied payment-service timeout scenario.

The supplied payment-system scenario is a separate real-world performance/debugging case; it is reference context, not a sixth code snippet required by this Task 0. The task's explicit deliverables remain the five buggy code files and this description file.
