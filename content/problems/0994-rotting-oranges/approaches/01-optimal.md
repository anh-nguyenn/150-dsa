## Idea

Queue all rotten oranges, count the fresh ones, and expand layer by layer. Each pass over the current queue size is one minute. Stop when there are no fresh oranges left or the queue runs dry; leftover fresh oranges mean failure.

## Why it works

Every orange in a layer is exactly the set that rots during that minute, because BFS processes cells in order of distance from the initial rotten set. Marking an orange rotten when it is enqueued prevents duplicates, and the fresh counter gives a direct test for unreachable oranges.

## Edge cases

- A grid with no fresh oranges needs 0 minutes.
- A single fresh orange with no rotten neighbor returns -1.
- Empty cells block the spread.
- All fresh oranges that are reachable rot in the same wave and share one minute count.
- The initial rotten oranges are already at minute 0.
