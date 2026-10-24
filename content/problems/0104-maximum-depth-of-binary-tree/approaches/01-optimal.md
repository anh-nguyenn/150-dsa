## Idea

Return zero for an empty tree. Otherwise compute the depth of both children recursively and take one plus the larger result, because the longest path must continue into the deeper child.

## Why it works

Every root-to-leaf path begins at the current node and then lies entirely in one of the two subtrees. The deeper subtree therefore determines the longest path through the current node, and adding one counts the current node itself. The recursion reaches every node exactly once.

## Edge cases

- An empty tree returns 0.
- A single node returns 1.
- A completely skewed tree is as deep as its node count.
- A tree with one deep side and one missing side follows the deep side, since `max` with 0 keeps the larger value.
