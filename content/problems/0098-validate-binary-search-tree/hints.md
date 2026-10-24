## Hint 1

A node does not just need to compare correctly with its parent. What range of values is allowed anywhere in its subtree?

## Hint 2

Carry a lower and an upper bound down the recursion. Which bound changes when you move left, and which when you move right?

## Hint 3

Use open bounds and allow them to be absent. Strict comparisons reject duplicates, and absent bounds avoid problems at the 32-bit limits.
