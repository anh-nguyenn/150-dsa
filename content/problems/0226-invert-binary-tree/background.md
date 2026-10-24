Mirroring a tree means changing left and right at every node, not merely reversing the order in which values are printed. The shape itself is reflected, so a left-only child becomes a right-only child.

### Everyday examples

- **A photo flipped horizontally.** Everyone in the picture stays the same, but the person who stood on the left now appears on the right.
- **A mirrored room.** Furniture against the left wall seems to sit against the right wall, and the room keeps the same layout in reverse.

### How it shows up here

The operation is local at each node once the subtrees are already mirrored. At the current node, you swap the two child pointers. Before that swap makes sense, each child subtree must itself be inverted, so the work naturally recurses down the tree.
