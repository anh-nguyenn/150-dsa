A binary search tree is an ordered structure: reading it in-order, from the leftmost node to the rightmost, produces a strictly increasing sequence. Each node acts as a boundary for everything below it, not only for its immediate children. A left-subtree value must stay below an ancestor even when the local parent looks fine.

### Everyday examples

- **Nested filing rules.** A folder's rule applies to everything inside it, including files several levels down. A subfolder cannot loosen the parent's range.
- **A tournament bracket.** Every match winner must have come from the allowed side of the bracket. Winning one local match is not enough if an earlier rule was already broken.

### How it shows up here

A recursive check passes an allowed open interval `(low, high)` down the tree. The root starts with no bounds. Going left tightens the upper bound to the node's value; going right tightens the lower bound. A node is acceptable only when it is strictly inside its interval.

Checking only `left.val < node.val < right.val` is the common mistake. It misses violations involving grandparents, exactly like the `3` under `5` in the example above.
