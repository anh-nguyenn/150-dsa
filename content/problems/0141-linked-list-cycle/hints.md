## Hint 1

Marking every visited node would work, but what extra memory does it require? Is there a way to use only two pointers?

## Hint 2

Imagine two walkers starting together, one moving one link per step and one moving two. What happens to their separation if the path loops?

## Hint 3

Use slow and fast pointers. If fast reaches `None`, there is no cycle; if they meet, the loop is confirmed.
