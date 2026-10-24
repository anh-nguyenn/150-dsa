## Idea

At each node, exchange the left and right child pointers. Recurse into both children first so the subtrees arrive already mirrored, then perform the swap. The base case returns `None` for an empty child.

## Why it works

Every node is visited once. After the two recursive calls, the left subtree is the mirror of the original left subtree and likewise for the right. Swapping the pointers places each mirrored subtree on the opposite side, which is exactly the mirrored whole. Empty children need no swap because both sides are `None`.

## Edge cases

- An empty tree has nothing to mirror, so `None` comes back.
- A single node is unchanged; its two empty children swap harmlessly.
- A one-sided chain becomes a chain in the opposite direction.
- A leaf simply returns itself, since both of its children are `None`.
