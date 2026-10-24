A marker is a temporary note stored somewhere that will not be read as data until later. In a grid, the first row and first column are natural notebooks: each can record whether another row or column needs to be cleared.

### Everyday examples

- **A checklist on the edge of a whiteboard.** You mark which rows of a seating chart have a problem by putting a dot in the margin, then act on the marks afterward.
- **Bookmarks in a recipe.** Instead of rewriting a page, you put sticky notes on the side, finish reading, and only then go back to the marked steps.

### How it shows up here

If you clear a row as soon as you find a zero, that cleared row may destroy zeros you have not inspected yet, causing extra rows and columns to disappear. The fix is two phases: first record which rows and columns contain a zero, then apply all the clears.

The first row and first column can hold those records. A zero in `matrix[0][c]` means column `c` must be cleared, and a zero in `matrix[r][0]` means row `r` must be cleared. The first row and column themselves need two separate flags, because their own cells are also part of the data being recorded.
