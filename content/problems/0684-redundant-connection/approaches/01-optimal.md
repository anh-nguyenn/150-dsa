## Idea

Scan the edges in the given order while maintaining disjoint sets of connected nodes. For each edge, find the roots of its two endpoints. If the roots already match, the endpoints are connected without this edge, so the edge closes the graph's single cycle and is the answer. Otherwise merge the two components and continue.

## Why it works

Before the extra edge, the useful edges form a forest, so every accepted edge merges two distinct components. The first edge whose endpoints already share a root cannot be part of a forest and must close the only cycle. All later edges are no better: because the input is a tree plus exactly one edge, there is only one cycle, and this is the last of its edges in input order. Returning it satisfies both the structural requirement and the tie-break rule.

## Edge cases

- A triangle of three nodes returns the third edge that appears.
- A long cycle may close near the end of the list; the closing edge is still returned.
- Extra edges after the cycle cannot appear in this problem, because there is only one extra edge in total.
- The answer can be the final edge in the list.
- Node labels start at `1`, so the disjoint-set array needs room through `n`.
