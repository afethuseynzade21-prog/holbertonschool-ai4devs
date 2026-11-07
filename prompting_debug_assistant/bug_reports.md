# Bug Reports — Prompting Debug Assistant (Task 3)

One structured report per bug. Details and test evidence: `bug_snippets/ai_debug_log.md` (diagnoses) and `bug_fixes/fix_validation.md` (tests). **AI-generated** = diagnosis and fix proposed by the AI assistant (Claude). **Manual** = edits made on top of the AI suggestion.

---

## Bug Report – bug1.py
- **File name**: `bug_snippets/bug1.py` (fixed: `bug_fixes/bug1_fixed.py`)
- **Summary**: The script crashes before it starts: `SyntaxError: '(' was never closed` at line 17.
- **Root Cause**: The last line is `main(` — the call's closing parenthesis is missing, so Python cannot parse the file.
- **Resolution**:
  - *AI-generated:* close the parenthesis.
  - *Manual edits:* none.
  ```python
  # before                 # after
  main(                    main()
  ```
  Verified: output `Average score: 80.25`.
- **Lesson Learned**: Read the exact line and caret in a `SyntaxError`; it points to the unclosed token. An editor with bracket matching or a linter would have caught it immediately.

---

## Bug Report – bug2.py
- **File name**: `bug_snippets/bug2.py` (fixed: `bug_fixes/bug2_fixed.py`)
- **Summary**: `find_largest([-8, -3, -12, -5])` returns `-12` instead of `-3`; the function actually finds the smallest value.
- **Root Cause**: Two logic errors: (1) inverted comparison `number < largest`; (2) `largest` starts at `0`, so an all-negative list can never beat the initial value.
- **Resolution**:
  - *AI-generated:* start from the first element and use `>`.
  - *Manual edits:* none to the code. I rejected the AI's incomplete alternative (flip the sign only, keep `largest = 0`), which still returned `0` for all-negative input. I also corrected the "Observed" value in `bug_descriptions.md` from `0` to `-12` after running the code.
  ```python
  # before                          # after
  largest = 0                       largest = numbers[0]
  if number < largest:              if number > largest:
  ```
  Verified: `-3` for the negative list, `9` for `[4, 9, 2]`. Known limit: an empty list raises `IndexError`.
- **Lesson Learned**: Test with data that differs from the "typical" case (all negatives). A hard-coded starting value like `0` is a hidden assumption. Also run the code before writing down what it "observed".

---

## Bug Report – bug3.py
- **File name**: `bug_snippets/bug3.py` (fixed: `bug_fixes/bug3_fixed.py`)
- **Summary**: Looking up a user that does not exist (`"samir"`) crashes with `AttributeError: 'NoneType' object has no attribute 'lower'` instead of printing "User not found".
- **Root Cause**: `dict.get()` returns `None` for a missing key. The code then calls `.lower()` on `None`, so it crashes before `main()` can reach its "User not found" branch.
- **Resolution**:
  - *AI-generated:* check for `None` before using the value.
  - *Manual edits:* none. (A `try/except KeyError` version also worked; the guard was chosen as clearer.)
  ```python
  # before                       # after
  email = users.get(username)    email = users.get(username)
  return email.lower()           if email is None:
                                     return None
                                 return email.lower()
  ```
  Verified: `samir` → `User not found`; `aydan` → `aydan@example.com`.
- **Lesson Learned**: Any function that can return `None` must be handled by its caller. Test the "not found" path, not only the happy path.

---

## Bug Report – bug4.js
- **File name**: `bug_snippets/bug4.js` (fixed: `bug_fixes/bug4_fixed.js`)
- **Summary**: `getLastItems(values, 3)` returns `['c','d']` instead of `['c','d','e']`; the last element is always missing.
- **Root Cause**: Off-by-one in the loop condition `i < items.length - 1`, which stops one index too early. The start index `items.length - n` was correct.
- **Resolution**:
  - *AI-generated:* use `i < items.length`.
  - *Manual edits:* added `module.exports` and an `if (require.main === module)` guard so the function can be imported for testing (logic unchanged). I rejected the AI alternative `items.slice(-n)` because it returns the whole array when `n = 0`.
  ```js
  // before                             // after
  i < items.length - 1                  i < items.length
  ```
  Verified: n = 3, 5, 1, 0 and empty array all correct; `assert.deepStrictEqual` checks passed.
- **Lesson Learned**: Loop boundaries are the classic place for off-by-one errors, so check both ends (n = length and n = 0). A shorter "clever" one-liner can hide its own edge-case bug (`-0 === 0`).

---

## Bug Report – bug5.c
- **File name**: `bug_snippets/bug5.c` (fixed: `bug_fixes/bug5_fixed.c`)
- **Summary**: For input `hello world` the program prints `Character count: 100` instead of `11`. It compiles with no warnings.
- **Root Cause**: Three combined problems: (1) `sizeof(text)` is the buffer size (100), not the string length; (2) `scanf("%s")` stops at whitespace, so only `hello` is read; (3) `%s` has no width limit, so input over 99 characters overflows the buffer (confirmed: AddressSanitizer `stack-buffer-overflow`).
- **Resolution**:
  - *AI-generated:* read with `fgets`, remove the newline with `strcspn`, count with `strlen`.
  - *Manual edits:* none. I rejected the partial fix of replacing only `sizeof` with `strlen`, which printed `5` for `hello world` and kept the overflow.
  ```c
  /* before */                          /* after */
  scanf("%s", text);                    if (fgets(text, sizeof(text), stdin) == NULL) return 1;
  size_t length = sizeof(text);         text[strcspn(text, "\n")] = '\0';
                                        size_t length = strlen(text);
  ```
  Verified: `11` for `hello world`, `0` for an empty line, `99` for a 150-character input, clean under AddressSanitizer.
- **Lesson Learned**: `sizeof` gives memory size, `strlen` gives string length. Never use an unbounded `%s`. A clean compile does not mean correct behavior; test with spaces and over-long input.

---

## Overall Reflection
- The AI diagnosed all five bugs correctly, and the stack traces/outputs in the prompts made the diagnoses precise.
- In bugs 2, 4 and 5 the AI also offered an alternative fix that looked reasonable but failed an edge case. Only running each suggestion caught this, so AI output should always be tested, not just read.
- My own contributions were limited to testing, choosing between the AI's alternatives, the small testability tweak in `bug4_fixed.js`, and correcting one wrong "observed" value in my own description file.
