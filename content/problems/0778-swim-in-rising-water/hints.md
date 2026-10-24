## Hint 1

If you knew the water level, how would you check whether the goal is reachable?

## Hint 2

Instead of adding edge costs, what quantity should you carry along a path so that it represents the water level needed?

## Hint 3

Run a shortest-path search where a step's cost is the larger of the current level and the next cell's height. The first time the goal leaves the heap is the answer.
