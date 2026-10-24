## Idea

Use squared distance instead of Euclidean distance. Keep a max-heap of at most `k` points by storing negative squared distances, so Python's min-heap removes the farthest candidate first.

For each point, push it and then pop once if the heap exceeds size `k`. The remaining heap entries are the k closest points.

## Why it works

After processing any prefix of the input, the heap contains the k closest points from that prefix. A new point only belongs in the answer if it beats the current farthest selected point, which is exactly the root; pushing and trimming performs that replacement. Squared distance preserves the same ordering as true distance because all distances are nonnegative.

## Edge cases

- Duplicate points are independent candidates and may both appear in the result.
- `k` equal to the total number of points returns all of them.
- Points on an axis or at the origin have distance zero and sort first.
- Equal distances are acceptable in any order because the problem allows a free ordering.
