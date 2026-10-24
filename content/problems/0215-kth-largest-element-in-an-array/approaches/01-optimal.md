## Idea

Keep a min-heap containing the k largest values seen so far. After inserting a value, remove the heap minimum if its size exceeds k.

At the end, the heap holds exactly the top k values, and its minimum is the kth largest.

## Why it works

The heap invariant ensures that after each prefix, no discarded value can be larger than all k retained values. Any value popped is smaller than the current kth best, so it cannot affect the final rank. Once the whole array is processed, the root is the smallest of the top k values, which is the required rank.

## Edge cases

- Duplicate values occupy separate heap entries, so ties are counted correctly.
- `k = 1` reduces the heap to tracking the maximum.
- `k` equal to the array length returns the minimum.
- Negative values need no special handling because the comparison order is unchanged.
