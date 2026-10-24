## Idea

Compare the two nodes at the same position. If either is missing, the trees match only when both are missing. If both exist, their values must be equal and both the left and right pairs must match recursively.

## Why it works

The definition of equality is compositional: the roots must agree, and then the left subtrees must be equal and the right subtrees must be equal. The recursion checks exactly these conditions at every position. `p is q` handles the two empty cases at once: `None is None` is true, while one empty and one present is false.

## Edge cases

- Two empty trees are equal.
- One empty tree and one non-empty tree are not equal.
- Equal values in different positions still fail because the recursion follows corresponding children.
- One tree may be a single node; the comparison stops as soon as the shapes diverge.
- Values may be negative or zero, so no value is treated as a special marker.
