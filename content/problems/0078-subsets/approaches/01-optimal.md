## Idea

Build subsets with a recursive walk. At each call, first record the current partial subset. Then try adding each unused number at or after the current position, recurse, and remove that number before trying the next one.

## Why it works

Every subset has a unique left-to-right list of chosen indices. The recursion visits exactly those choices because it only moves forward, so no subset is built twice. Recording at the start of each call captures the empty subset and every partial choice, not just full-length branches.

## Edge cases

- An empty input returns `[[]]`, since the empty subset is still valid.
- A single number returns the empty subset and the one-element subset.
- Negative values behave the same as positive values.
- The official input has distinct values; duplicate handling is the subject of Subsets II.
