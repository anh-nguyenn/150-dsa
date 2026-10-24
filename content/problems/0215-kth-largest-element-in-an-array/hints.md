## Hint 1

If the array were sorted from largest to smallest, which position would hold the answer? Why might a full sort be more work than necessary?

## Hint 2

You only need k candidates. When a new value arrives and the candidate set is full, which candidate should leave?

## Hint 3

Use a min-heap of size k. Insert each value and pop the minimum whenever the heap exceeds k; the root at the end is the kth largest.
