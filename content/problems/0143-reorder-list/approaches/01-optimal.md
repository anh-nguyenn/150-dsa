## Idea

Use slow and fast pointers to find the last node of the first half. Cut the list there and reverse the second half. Then walk both halves together, inserting one node from the reversed back half after each node of the front half.

## Why it works

The front half supplies `L0, L1, ...` and the reversed back half supplies `Ln, Ln-1, ...`. Alternating inserts therefore produce exactly the requested order. Reversing and merging only rewires existing nodes, so the process uses constant extra space.

## Edge cases

- Empty list and one-node list: nothing to rearrange.
- Two nodes: the order is already `L0 -> L1`.
- Odd length: the middle node belongs to the first half and ends up after the larger positions.
- Even length: both halves have the same size.
- The second half is shorter than or equal to the first, so the merge loop stops when it is exhausted.
