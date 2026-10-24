## Hint 1

A longest path has a highest node. If that node is fixed, which two downward paths should it join?

## Hint 2

The two downward paths are the heights of the left and right subtrees. How many edges does joining them use?

## Hint 3

Write a post-order helper that returns a subtree's height while updating a running maximum of `left_height + right_height`. Every node gets a turn as the turning point.
