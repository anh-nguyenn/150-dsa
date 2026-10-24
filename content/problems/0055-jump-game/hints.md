## Hint 1

You do not need to try every path. Ask only how far to the right you could possibly have gotten by the time you reach a given position.

## Hint 2

While scanning, if the current index is already beyond the farthest position you can reach, you are stuck.

## Hint 3

Keep one frontier value and update it with `i + nums[i]` at each reachable index. If it covers the last index, you can finish.
