A tree traversal is a fixed order for recording nodes. Pre-order records a node before its subtrees, so the root always comes first. In-order records the left subtree, then the node, then the right subtree, so the root's position divides the remaining values into a left group and a right group. Combining these two views pins down the whole shape.

### Everyday examples

- **Assembling a family tree from two lists.** One list names each parent before their children; the other lists siblings and relatives in left-to-right order. The first name anchors the parent, and its position in the second list shows who belongs on each side.
- **Rebuilding a nested outline.** An outline read top-down gives section headings in the order they open, while a left-to-right read gives the contents in reading order. Seeing where a heading appears in the second list tells you which entries are nested under it.

### How it shows up here

The next unused pre-order value is always the root of the current subtree. Look up that value's index in the in-order list to learn how many nodes belong to the left subtree. That count tells you the exact slice of pre-order values for the left side; the rest belong to the right. Recursing on those slices reconstructs the tree.

A hash map from value to in-order index removes the linear scan that would otherwise make the recursion quadratic.
