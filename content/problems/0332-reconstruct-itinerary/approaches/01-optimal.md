## Idea

Store each airport's outgoing destinations in a min-heap. Depth-first search follows the smallest unused ticket at every step. An airport is appended to the route only after all of its outgoing tickets have been used, and the finished list is reversed. This is Hierholzer's algorithm with lexical tie-breaking built into the heap.

## Why it works

Hierholzer's algorithm produces an Eulerian path whenever one exists: each traversal consumes a distinct ticket, so the result uses every edge, and appending a node only after its outgoing edges are exhausted correctly splices cycles into the route. Reversing the post-order gives the forward itinerary. Choosing the smallest available destination first makes the resulting sequence the lexicographically smallest valid one.

## Edge cases

- Cycles are handled naturally: the search may wander around a loop before returning to use other tickets.
- Several tickets can share the same origin and destination; each is a separate heap entry.
- A ticket that starts exactly where another ends is chained correctly.
- The start airport is always `"JFK"` as guaranteed by the problem.
