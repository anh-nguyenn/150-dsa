## Hint 1

Which list tells you the root immediately? Once you know the root, what does its position in the other list reveal?

## Hint 2

The root's index in the in-order list gives the size of the left subtree. How does that size split the pre-order list?

## Hint 3

Precompute a value-to-index map for the in-order list, then recurse on index ranges instead of copying sublists.
