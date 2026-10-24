## Hint 1

Start with a node that has two children. What one change turns that small tree into its mirror image?

## Hint 2

After you swap a node's children, are the subtrees beneath them already mirrored? If not, what has to happen first?

## Hint 3

Invert the left subtree and the right subtree, then swap the two child pointers at the current node. Any traversal order that reaches every node works.
