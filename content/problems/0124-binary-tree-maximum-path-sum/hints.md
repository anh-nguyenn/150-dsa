## Hint 1

At a node, a path can use its left side, its right side, both, or neither. Which combinations are legal for a path that continues to the parent?

## Hint 2

A path that turns at a node can include both children, but the value passed upward may include only one. What should a helper return?

## Hint 3

Return the best one-sided gain, clamp negative gains to zero, and record the best two-sided sum at every node.
