A tree path can bend at one node: it comes up from one side and leaves through another. From the perspective of a node, the best path that turns there is a downward gain from the left plus the node's value plus a downward gain from the right. A gain is the best sum obtainable by walking from a node into one of its subtrees.

### Everyday examples

- **Choosing the best route through a junction.** A trip can enter from one road and leave by another. The best trip through the junction combines the strongest inbound route with the strongest outbound one.
- **Combining two best streaks.** If you have the best earning streak ending at a point from the left and another from the right, joining them at that point can beat either streak alone, provided both contributions are positive.

### How it shows up here

A post-order helper returns the best one-sided gain a subtree can contribute upward. At each node, the candidate path that turns at that node combines the left gain, the node value, and the right gain. Record the best candidate seen anywhere. The value returned to the parent can use only one side, because a path cannot branch twice.

Negative gains are dropped by clamping them to zero, which means "do not include that side".
