## Idea

Recurse from the root with an open interval of permitted values. Initially the interval is unbounded. At a node, reject it if it is not strictly between the bounds. Recurse into the left child with the same lower bound and the node's value as the new upper bound; recurse into the right child with the node's value as the new lower bound and the same upper bound.

Using `None` for a missing bound keeps the logic correct even when node values reach the extremes of the integer range.

## Why it works

The invariant is that every node in the current subtree must lie strictly inside `(low, high)`. The root has no restrictions, so the invariant holds at the start. Moving left adds the requirement of being below the current value, and every value in that subtree must also satisfy all earlier bounds because the other bound is carried unchanged. The right side is symmetric. Thus a node is accepted exactly when it obeys every ancestor, which is precisely the BST property.

## Edge cases

- Equal values are invalid because both comparisons are strict.
- A node can be locally correct but violate a distant ancestor's bound.
- Values at the 32-bit minimum or maximum must not be rejected by sentinel numbers; absent bounds handle this.
- A tree with only a left chain is valid only if values strictly decrease downward.
- An empty tree is accepted defensively, though the constraints start at one node.
