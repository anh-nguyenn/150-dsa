A rotation moves every point around a center by a fixed angle. For a square grid, a quarter turn clockwise sends the cell at row `i`, column `j` to row `j`, column `n - 1 - i`. Keeping the whole picture upright means moving every cell at once rather than sliding one row through another.

### Everyday examples

- **Turning a photo.** Rotating a phone photo by 90 degrees changes which edge is on top; every pixel keeps its color but lands somewhere new.
- **A rotating chessboard.** If you physically spin the board a quarter turn, the old top edge becomes the right edge, and the old left edge becomes the top.

### How it shows up here

Writing the destination of each cell directly would overwrite cells that have not moved yet. Two simple global moves avoid that: flip the grid across its main diagonal, then reverse each row. The first move swaps row and column, and the second fixes the direction of the turn.

This is convenient because neither step needs a second grid. The diagonal flip touches only pairs above and below the diagonal, and reversing a row can be done with two pointers moving inward.
