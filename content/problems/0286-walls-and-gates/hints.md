## Hint 1

What is wasteful about starting a separate search from every empty room?

## Hint 2

All gates are distance 0. If they expand at the same time, how can you process them one layer at a time?

## Hint 3

Queue every gate, then run BFS. When an untouched empty room is first reached, assign the current distance plus one; BFS makes that the nearest gate.
