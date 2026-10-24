## Idea

Perform an in-order traversal with an explicit stack. Descend left while pushing nodes so the smallest unvisited value is always on top. Pop a node, count it, and if it is the `k`-th one return its value immediately. Otherwise continue into its right subtree.

The traversal does not need to finish once `k` values have been visited.

## Why it works

In-order traversal of a BST yields values in strictly increasing order, so the `k`-th popped node is the `k`-th smallest. The inner loop always reaches the leftmost unvisited node, which is the next value in sorted order. Returning at the moment `k` reaches zero avoids unnecessary work, and the stack contains only one root-to-node path at a time.

## Edge cases

- `k = 1` returns the leftmost node without exploring the rest of the tree.
- `k` equal to the node count returns the rightmost value.
- A single-node tree returns that node for `k = 1`.
- A left-skewed tree pushes the whole chain, while a balanced tree uses logarithmic stack space.
- The problem guarantees `k` is valid, so the final fallback is never reached.
