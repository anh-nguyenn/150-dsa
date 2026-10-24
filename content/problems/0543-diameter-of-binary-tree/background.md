The diameter of a graph or tree is its longest shortest path; in a tree, that is simply the longest path between any two nodes. In a binary tree, a path can go up toward an ancestor and then down another branch, so the highest point of the path is not necessarily the root.

### Everyday examples

- **Two far-apart rooms in a building.** The distance between them is the number of corridors on the route, and the route may pass through a central junction rather than the main entrance.
- **Two leaves on a branch.** The longest trip between leaves can be entirely inside one large branch, without going back to the trunk.

### How it shows up here

For each node, the longest path that turns at that node combines the deepest descent into its left subtree with the deepest descent into its right subtree. Measuring those two heights and adding them gives a candidate diameter. One post-order pass can compute heights and collect the best candidate from every possible turning point.
