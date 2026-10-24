A binary search tree stores smaller values to the left and larger values to the right of each node. The lowest common ancestor of two nodes is the deepest node whose subtree contains both of them; it is the point where their root-to-node paths meet.

### Everyday examples

- **Two files in a folder tree.** Their lowest common ancestor is the deepest folder that contains both of them, not the top-level drive.
- **Two stops on a transit map.** The shared station where their routes first join is the meeting point closest to both.

### How it shows up here

The BST ordering turns ancestor-finding into a directional walk. If both values are smaller than the current node, both paths must continue left. If both are larger, both continue right. The first node where that is no longer true sits between the two values, and that is exactly where the paths split.
