## Idea

Slide a window of length `len(s1)` across `s2` and keep a 26-slot letter count for the window. Whenever the count equals the count of `s1`, a rearrangement has been found.

## Why it works

Two strings are rearrangements exactly when their letter counts match. The sliding window always represents a contiguous stretch of `s2` of the right length, and the add-one/remove-one update keeps its counts exact. Checking every possible window start therefore tests every candidate substring.

## Edge cases

If `s1` is longer than `s2`, no window fits and the answer is false. A window at the very start is checked before any removal. A window at the very end is checked after the final add and removal. Repeated letters are handled because counts, not just presence, must match.
