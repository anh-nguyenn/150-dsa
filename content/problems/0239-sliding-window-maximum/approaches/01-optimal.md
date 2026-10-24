## Idea

Maintain a deque of indices whose values strictly decrease. Drop dominated values from the back, drop expired indices from the front, and read the current maximum from the front.

## Why it works

If an older value is no larger than a newer value, the older one can never be the maximum while the newer one is still in the window, so it is safe to remove. The deque therefore keeps exactly the undominated candidates in decreasing order. The front is always the largest remaining value, and removing indices before the window start keeps it current.

## Edge cases

A window size of one returns the original array. A window as large as the array returns a single maximum. Negative numbers work because comparisons are ordinary numeric comparisons. Duplicate maxima are handled by using `<=` when removing from the back, keeping only the newest copy.
