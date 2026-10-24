## Idea

Run a post-order helper that returns the height of each subtree. At every node, the best path whose highest point is that node has `left_height + right_height` edges; record the largest such value in a nonlocal variable. The helper then passes its own height upward.

## Why it works

Any path in a tree has a unique highest node. At that node the path descends into the left subtree for `left_height` edges and into the right subtree for `right_height` edges, and those descents can be chosen independently. The pass evaluates every node as a possible highest point, so the recorded maximum is the diameter. Heights are computed bottom-up, so each node is processed once.

## Edge cases

- A single node has no edges, so the diameter is 0.
- A two-node tree has diameter 1.
- A perfect tree's diameter passes through the root, while a deep one-sided subtree can make the best turning point lower down.
- An empty tree returns 0 defensively, even though the stated constraints start at one node.
- The diameter counts edges, not nodes.
