## Idea

Store each in-order value's index in a hash map. Then recurse over ranges: the first pre-order value in the current range is the subtree root. Its in-order index splits that range into left and right portions. The size of the left portion determines how many following pre-order values belong to the left subtree, and the remainder belongs to the right.

Only indices are passed down, so no list copying is needed.

## Why it works

For a subtree, pre-order lists its root first, followed by all nodes of the left subtree, then all nodes of the right subtree. In-order lists the left subtree, the root, then the right subtree. The root's in-order position therefore gives the left subtree's size, which in turn cuts the pre-order range at exactly the right place. Applying the same argument recursively reconstructs every node and child link. Each node is created once and each index lookup is constant time.

## Edge cases

- A single node produces a leaf.
- A tree with only left children: each root's in-order index is at the end of its range.
- A tree with only right children: the left range is empty each time.
- Empty lists return `None` defensively, though the constraints start at one node.
- Distinct values are what make the index map unambiguous; duplicates would require a different strategy.
