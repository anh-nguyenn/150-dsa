## Idea

Sort intervals by start and queries by value, keeping each query's original index. Sweep the queries in increasing order. Before answering a query, insert all intervals whose start is at most the query into a min-heap keyed by interval length. Then discard expired intervals whose end is below the query. The heap top is the shortest interval covering the query; write it into the answer slot for the original index.

## Why it works

At the moment a query is answered, the heap contains exactly the intervals that started early enough, minus those that already ended, so every interval in it covers the query and every covering interval is either in it or was already popped as too short-lived. Because the heap is ordered by length, its top is the shortest valid one. Processing queries in ascending order means intervals enter once and leave at most once, giving near-linear total work.

## Edge cases

- A query outside every interval gets `-1`.
- Queries exactly on a start or end are inside, so the sweeps use `<=` and `<` in the right places.
- Duplicate queries each receive an answer.
- A single-point interval has length `1`.
- Answers are stored by original query index, so unsorted queries are handled.
