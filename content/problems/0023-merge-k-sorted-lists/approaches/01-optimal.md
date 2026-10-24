## Idea

Put the head of each non-empty list into a min-heap as `(value, list_index, node)`. Pop the smallest entry, attach that node to the result, and push its successor from the same list. Repeat until the heap is empty.

## Why it works

At any point the smallest unplaced node must be the head of some remaining list, so it is the heap minimum. The list index breaks value ties without comparing node objects. Each node is pushed and popped once, and the heap holds at most `k` entries, giving `O(N log k)` time and `O(k)` extra space.

## Edge cases

- No lists at all: the heap stays empty and `None` is returned.
- All lists empty: every head is skipped, so the result is `None`.
- One list: the heap behaves like a simple walk through that list.
- Duplicate values across lists: the index tie-breaker keeps the heap valid.
- Very different list lengths: shorter lists simply stop contributing successors.
