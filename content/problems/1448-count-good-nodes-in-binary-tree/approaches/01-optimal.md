## Idea

Walk the tree depth-first while carrying the maximum value on the path from the root to the current node. At each node, increment the count when the node's value is at least that maximum. Then replace the maximum with the larger of the two and continue into both children.

The maximum is a parameter of the recursive call, so each branch receives the history of its own ancestors only.

## Why it works

For any node, the path from the root is unique. The carried value is exactly the largest value on that path before the node is considered, so comparing against it matches the definition of a good node. Updating the maximum before descending preserves the invariant for the children. Every node is visited once, and the maximum is propagated to both subtrees, so no good node is missed and no bad node is counted.

## Edge cases

- The root is always good because its path contains no earlier value.
- Equal values are good: the comparison is `>=`, not `>`.
- Negative values are fine; the running maximum may stay negative.
- A long chain uses recursion depth equal to the height, so the stack cost is `O(h)`.
- A single node returns 1.
