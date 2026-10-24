## Hint 1

Which data structure gives first-in, first-out order, and therefore visits nodes level by level?

## Hint 2

If you process nodes one at a time, how can you tell where the current level ends and the next begins?

## Hint 3

Use a queue and record its size at the start of each round. Pop exactly that many nodes into one level list, enqueueing their children as you go.
