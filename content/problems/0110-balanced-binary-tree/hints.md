## Hint 1

A tree is balanced only if both subtrees are balanced and their heights differ by at most one. What two facts must each child report?

## Hint 2

Can you avoid measuring the same subtree's height repeatedly at every ancestor?

## Hint 3

Use a helper that returns a subtree's height, or -1 if that subtree is unbalanced. Propagate -1 upward immediately; otherwise apply the height-difference rule.
