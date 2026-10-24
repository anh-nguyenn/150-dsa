## Hint 1

If a subtree match exists, where in the larger tree does it begin? How many possible starting points are there?

## Hint 2

Once a starting node is chosen, what exactly must hold between its subtree and `sub_root`?

## Hint 3

Try each node as a starting point and compare the whole subtree for equality. If one comparison succeeds, stop; otherwise repeat for the left and right children.
