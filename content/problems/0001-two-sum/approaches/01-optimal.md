## Idea

Walk the array once. Before storing the current value, ask whether its complement has already been seen. The map stores each value and the index where it appeared.

## Why it works

If the answer is the pair at indices `i` and `j` with `i < j`, then when the loop reaches `j`, the value at `i` is already in the map. Checking the complement at `j` finds it. The check happens before insertion, so `j` cannot pair with itself.

## Edge cases

- Duplicate values such as `[3, 3]`: the second copy finds the first in the map.
- Negative numbers: the complement is computed the same way.
- The pair may be the first and last elements; one pass still reaches it.
- The problem guarantees a pair, but returning an empty list keeps the function total.
