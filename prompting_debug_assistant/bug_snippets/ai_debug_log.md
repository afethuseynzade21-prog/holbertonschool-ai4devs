# AI Debug Log — Prompting Debug Assistant (Task 1)

**AI assistant used:** Claude (Anthropic).
**Method:** For each snippet the AI was given the prompt below plus the code and the real error output or observed result. Every suggested fix was then executed (Python 3.13, Node 22, GCC 13) and the result recorded. Outputs shown are real, not predicted.

**Prompt template used for every bug** (structured as in the Expert Prompts Collection, "Error Analysis & Root Cause Investigation"):

> This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?
> **Language:** [..] **Intended behavior:** [from bug_descriptions.md] **Observed:** [error / output]
> Please give: root cause, the fix, and any alternative fixes with trade-offs.

---

## Bug 1 – bug1.py

**Prompt context:** Run `python3 bug1.py` and received:
```
  File "bug1.py", line 17
    main(
        ^
SyntaxError: '(' was never closed
```
**AI Diagnosis**: The last line `main(` opens a call but never closes the parenthesis, so Python cannot parse the file and nothing runs. The error is reported at the unclosed `(`, which points directly at the cause.
**Suggested Fix**: Change line 17 to `main()`.
**Alternative Fixes Tested**: None (a syntax error has a single correct repair).
**Result**: Fix works. Output: `Average score: 80.25`.

---

## Bug 2 – bug2.py

**Prompt context:** `find_largest([-8, -3, -12, -5])` should return `-3` but printed `Largest number: -12`.
**AI Diagnosis**: Two logic errors combine. (1) The comparison `number < largest` is inverted, so the function actually finds the **minimum**. (2) `largest` starts at `0`, which is wrong for lists that contain only negative numbers: even with `>`, nothing is ever greater than `0`, so `0` would be returned although it is not in the list.
**Suggested Fix**: Initialise `largest = numbers[0]` and use `number > largest`.
**Alternative Fixes Tested**:
- **A (initialise with first element + `>`)**: `[-8,-3,-12,-5]` → `-3`, `[4,9,2]` → `9`. Works.
- **B (`return max(numbers)`)**: `-3`. Works; simplest, but hides the algorithm and raises `ValueError` on an empty list (A raises `IndexError`), so either needs an empty-list guard.
- **C (only flip `<` to `>`, keep `largest = 0`)**: `[-8,-3,-12,-5]` → `0`, `[4,9,2]` → `9`. **Fails** for all-negative input.
**Result**: Fix A (or B) works; C is an incomplete fix that was rejected.

---

## Bug 3 – bug3.py

**Prompt context:** Searching for username `samir` (not in the dictionary) crashed with:
```
File "bug3.py", line 9, in find_user_email
    return email.lower()
AttributeError: 'NoneType' object has no attribute 'lower'
```
**AI Diagnosis**: `users.get("samir")` returns `None` for a missing key (no `KeyError`). Calling `.lower()` on `None` raises `AttributeError`. The "User not found" branch in `main()` is never reached because the crash happens first.
**Suggested Fix**: Guard before using the value: `if email is None: return None`.
**Alternative Fixes Tested**:
- **A (`is None` guard)**: `samir` → `User not found`, `aydan` → `Email: aydan@example.com`. Works.
- **B (`try: users[username].lower() except KeyError: return None`)**: same two results. Works; idiomatic EAFP style, but catches only a missing key, not other errors.
**Result**: Both fixes work. Fix A chosen as the clearer one for this snippet.

---

## Bug 4 – bug4.js

**Prompt context:** `getLastItems(values, 3)` should be `["c","d","e"]` and `getLastItems(values, 5)` the full array. Actual output:
```
[ 'c', 'd' ]
[ 'a', 'b', 'c', 'd' ]
```
**AI Diagnosis**: Off-by-one in the loop condition. `i < items.length - 1` stops one index too early, so the last element is always dropped. The start index (`items.length - n`) is correct.
**Suggested Fix**: Change the condition to `i < items.length`.
**Alternative Fixes Tested**:
- **A (`i < items.length`)**: `['c','d','e']` and `['a','b','c','d','e']`. Works.
- **B (`items.slice(items.length - n)`)**: same correct results, and `n = 0` → `[]`. Works.
- **C (`items.slice(-n)`)**: correct for 3 and 5, but `n = 0` returns the **whole array** because `-0 === 0`. Works for the tested cases only; **fails the edge case** `n = 0`.
**Result**: Fix A works with minimal change; B is the most robust. C rejected because of the `n = 0` edge case.

---

## Bug 5 – bug5.c

**Prompt context:** Input `hello world` should report `11` characters. Compiled with `gcc -Wall -Wextra`; no warnings, but the output was `Character count: 100`.
**AI Diagnosis**: Three problems. (1) `sizeof(text)` returns the **buffer size** (100 bytes), not the length of the string; `strlen()` is needed. (2) `scanf("%s")` stops at the first whitespace, so only `hello` is read. (3) `%s` has no width limit, so input longer than 99 characters overflows the buffer. Confirmed with AddressSanitizer: a 150-character input gives `stack-buffer-overflow ... WRITE of size 151`.
**Suggested Fix**: Read with `fgets(text, sizeof(text), stdin)`, strip the newline with `text[strcspn(text, "\n")] = '\0'`, and use `strlen(text)`.
**Alternative Fixes Tested**:
- **A (`fgets` + `strcspn` + `strlen`)**: `hello world` → `11`; 150-char input → `99` (safely truncated, no overflow). Works.
- **B (`scanf("%99[^\n]", text)` + `strlen`)**: `hello world` → `11`. Works and is also bounded, but leaves the newline in the input buffer and fails (returns 0) on an empty line.
- **C (keep `scanf("%s")`, replace only `sizeof` with `strlen`)**: `hello world` → `5`. **Fails**: still reads one word and still has the overflow risk.
**Result**: Fix A works and is the safest. B is acceptable. C rejected as incomplete.

---

## Summary

| Bug | File | Root cause | Working fix |
|---|---|---|---|
| 1 | bug1.py | Unclosed parenthesis | `main()` |
| 2 | bug2.py | Inverted comparison + wrong initial value | `largest = numbers[0]`, `>` |
| 3 | bug3.py | `.get()` returns `None`, then `.lower()` | `is None` guard |
| 4 | bug4.js | Loop ends at `length - 1` | `i < items.length` |
| 5 | bug5.c | `sizeof` vs `strlen`, `%s` stops at space, no bounds | `fgets` + `strlen` |

**Observation:** In 3 of 5 bugs (2, 4, 5) a plausible-looking "quick fix" (C) was suggested alongside the correct one and only failed when tested on an edge case. Running every suggestion was necessary; reading the AI's explanation alone would not have caught these.
