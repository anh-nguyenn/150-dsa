## Idea

Maintain a min-heap whose size never exceeds `k`. Every value in the heap belongs to the current top-k group, and the smallest member of that group is the heap root.

When a new value arrives, push it and then pop the minimum if the heap has grown too large. The root after that adjustment is the answer.

## Why it works

The heap always holds the k largest values seen so far. Its minimum is therefore the smallest among those k values, which is exactly the kth largest value overall. Values removed during a resize are smaller than every remaining member, so they can never be needed for a future kth-largest query.

## Edge cases

- Duplicate values must count separately; the heap stores one entry per occurrence.
- The initial list can contain fewer than `k` values, but `add` is only queried once enough values exist.
- Negative values work without special handling because only their relative order matters.
- A stream that never exceeds `k` values returns the current minimum on every `add`.
