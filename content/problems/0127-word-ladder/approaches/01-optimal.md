## Idea

Precompute a map from wildcard patterns to the words matching them. A pattern replaces one position with `*`, so words sharing a pattern differ at most at that position. Run breadth-first search from `begin_word`, tracking the number of words used. For each dequeued word, generate its patterns, look up all candidate neighbors, and enqueue unvisited ones. Return the step count as soon as `end_word` is found.

## Why it works

In the implicit word graph, an edge exists exactly between two words that share a wildcard pattern and differ at that position. Breadth-first search processes words in nondecreasing distance from the start, so the first time the target is reached, no shorter chain can exist. Marking words visited when they are enqueued prevents cycles and duplicate work, and clearing a pattern group after expansion avoids scanning the same neighbors again.

## Edge cases

- If the start and target are the same word, the chain has one word.
- If the target is absent from the list, no chain can end there; return `0`.
- A direct one-letter neighbor gives a chain of length two.
- Words with no neighbors are dead ends and are simply never expanded.
- Disconnected clusters of words produce no route, so the search drains and returns `0`.
- The start word need not be in the list; it is still the first word of the chain.
