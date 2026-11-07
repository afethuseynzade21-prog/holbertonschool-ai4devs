# Reflection on AI-Assisted Debugging

## Introduction
I gave five small buggy programs (Python, JavaScript, C) to an AI assistant, asked it to explain each failure, then ran every suggested fix myself. The goal was to see how useful AI is as a debugging partner and where it still needs a human checking its work.

## AI Strengths
The easiest bug was `bug1.py`. The error message already said `SyntaxError: '(' was never closed`, and the AI named the cause and the one-character fix at once. Bugs with a stack trace were just as quick: for `bug3.py` the `AttributeError: 'NoneType' object has no attribute 'lower'` led straight to the explanation that `dict.get()` returns `None`.

The AI was also strong at finding causes I had not spelled out. In `bug5.c` it found three problems at once (`sizeof` vs `strlen`, `%s` stopping at spaces, no length limit), and AddressSanitizer later confirmed the overflow with `stack-buffer-overflow ... WRITE of size 151`.

## AI Weaknesses
The hardest bugs were the ones without an error message: `bug2.py`, `bug4.js` and `bug5.c`. Here the AI offered alternative fixes that looked right but were not. For `bug2.py`, flipping only the comparison gave `0` for `[-8, -3, -12, -5]`, because `largest = 0` stayed. For `bug4.js`, `items.slice(-n)` worked for n = 3 and 5 but returned the whole array for n = 0, since `-0 === 0`. For `bug5.c`, swapping only `sizeof` for `strlen` printed `5` for `hello world`. I would not have noticed any of these without running the code.

## Human Role
My trust in the AI's explanations was high, but my trust in its untested fixes was low. Humans were needed to choose test inputs (all-negative lists, n = 0, a 150-character line), to pick between valid alternatives, and to judge side effects, such as the `require.main` guard I added to `bug4_fixed.js` so it could be tested.

I also made a mistake myself: my `bug_descriptions.md` said `bug2.py` returned `0`. Running it showed `-12`. Writing down what a program "should" do is not the same as checking what it does.

## Conclusion
AI made diagnosis much faster, especially with clear error output, but the total process was not dramatically shorter, because validating every fix took real time. That time was worthwhile: three of five bugs had a tempting but wrong alternative. In real-world debugging I would use AI as a fast first reviewer that proposes hypotheses and fixes, while a human supplies the failing test cases, runs the code, and decides what is merged. A good prompt with the real error output and the intended behavior made the answers noticeably better.
