## Idea

When the scan finds an unvisited `1`, flood fill outward and count every cell the fill removes. Mark cells as water on entry, then keep the largest area seen across all fills.

## Why it works

A flood fill from one land cell reaches exactly its connected component, so the number of cells it removes is that island's area. Marking on entry prevents double counting and keeps every island from being explored more than once.

## Edge cases

- A grid with no land returns 0.
- A single `1` has area 1.
- Diagonally adjacent cells belong to different islands.
- A full grid is one island whose area is the cell count.
- Marking while enqueueing avoids adding the same cell twice.
