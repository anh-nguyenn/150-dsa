## Idea

Track the farthest index reachable so far. Scan the array, and whenever the current index is still within reach, extend the frontier using the jump available there. If the scan reaches a position beyond the frontier, report failure.

## Why it works

Every index up to the frontier is reachable, since the frontier was produced by some reachable position. When the current index is at most the frontier, its jump can be used, so updating the frontier keeps the invariant. If an index exceeds the frontier, no reachable position could have jumped that far, so the last index cannot be reached either.

## Edge cases

- A single position is already the last index, so the answer is true even when its value is zero.
- A leading zero makes every later position unreachable unless the array has length one.
- Zeros in the middle are fine if the frontier has already passed them.
- Jump values larger than the remaining distance simply overshoot; that still reaches the end.
- The frontier may grow beyond the array length, which is harmless.
