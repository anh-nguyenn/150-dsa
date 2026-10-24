## Hint 1

What order would you visit the nodes in if you wanted the values to come out sorted?

## Hint 2

A BST's in-order walk is sorted. How could you count visits as they happen instead of collecting every value?

## Hint 3

Use a stack, push left children, pop a node, decrement `k`, and stop when it reaches zero. Then the popped value is the answer.
