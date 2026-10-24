## Idea

Maintain the four edges of the unvisited rectangle. Read one edge, move that edge inward, and repeat until the edges cross.

## Why it works

Each pass reads exactly the cells on the current boundary and then removes that boundary from consideration. No cell is inside two consecutive boundaries because the top and right moves are followed by checks that the region still has height and width. Adding each cell once means the result has exactly `m * n` entries, and invalid states stop the loop.

## Edge cases

- A single row is read left to right by the top walk; the guarded bottom walk does nothing.
- A single column is read top to bottom by the right walk; the guarded left walk does nothing.
- A `1 x 1` grid produces one value.
- The final inner row or column may be visited by only one walk, which the boundary checks preserve.
