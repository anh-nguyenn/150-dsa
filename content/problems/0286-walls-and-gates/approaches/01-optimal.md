## Idea

Seed a queue with every gate, then run BFS across empty rooms. When an empty room is reached for the first time, its distance is its parent's distance plus one; walls and filled rooms are never revisited.

## Why it works

BFS expands in non-decreasing distance from all sources at once, so the first arrival at a room comes from a nearest gate. Filling the room immediately marks it visited, which keeps the work linear in the number of cells.

## Edge cases

- An empty grid returns without changes.
- A grid with no gates leaves every empty room at the large sentinel value.
- A single gate or a single empty room behaves correctly.
- Walls block paths and are never overwritten.
- Unreachable rooms keep the sentinel rather than becoming -1.
