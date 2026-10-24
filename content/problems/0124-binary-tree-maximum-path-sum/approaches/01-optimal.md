## Idea

Use a post-order helper that returns the maximum gain available by starting at a node and descending into at most one child. At each node, compute the positive gains from both children. The best path that turns at this node is `left + node.val + right`, which is a candidate for the overall answer. Return `node.val + max(left, right)` so the parent can continue the path through one side only.

Clamping each gain with `max(gain, 0)` represents choosing not to include that subtree.

## Why it works

Any path has a highest node. At that node the path may use zero, one, or both child directions, and the parts below are independent best downward gains. The helper evaluates exactly that combination for every node as the highest point, so the maximum recorded candidate is the best path in the tree. The value returned upward is restricted to one direction, which matches the shape a path must have when it continues to a parent. Every node is processed once.

## Edge cases

- All values negative: clamping would suggest an empty side, but the node itself is still included, so the best single node wins.
- A single node returns its own value.
- A path may end before reaching a leaf.
- A child's gain can be zero after clamping, effectively excluding that entire branch.
- Deep recursion uses stack space proportional to the tree height, up to 30,000 in a skewed tree.
