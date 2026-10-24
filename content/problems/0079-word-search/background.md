Depth-first search explores one path as far as it can before backing up. On a grid, a path is a sequence of neighboring cells. Marking a cell while it is being used prevents the search from stepping on itself, and unmarking it afterward lets other paths use that cell.

### Everyday examples

- **A maze.** You follow a corridor until it dead-ends, then return to the last junction and try a different turn. You do not teleport or walk diagonally through walls.
- **Connecting letters on a word puzzle.** You drag a finger from one letter to an adjacent letter, lifting only when the word is complete. The same square cannot be crossed twice in one attempt.

### How it shows up here

Each cell that matches the first letter is a possible starting point. From there, the search looks at the four neighboring cells for the next letter. A visited cell is temporarily replaced with a sentinel so the current path cannot reuse it. If the whole word is matched, the answer is `true`; otherwise the cell is restored and the search continues elsewhere.

Restoring the cell is essential. The grid is shared by many candidate paths, and a cell blocked by one failed attempt must be available to later attempts.
