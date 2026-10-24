## Idea

Try every cell as a possible start. From a cell, recursively match the next character in the four orthogonal directions. Temporarily mark the current cell so it cannot be revisited on the same path, then restore it after exploring.

## Why it works

The recursion consumes the word one character at a time. At each step it only enters a neighboring cell whose letter matches the needed character, so any successful return corresponds to a valid path. Marking cells enforces the no-reuse rule, and restoring them means one failed path does not corrupt the search for another start or another branch.

## Edge cases

- A one-cell board with a one-letter word returns `true` if the letters match.
- A word longer than the number of cells cannot be traced and returns `false`.
- The empty word returns `true`, matching the convention that no letters are needed.
- A word requiring the same cell twice is rejected by the marking step.
- The board is modified during the search but restored before returning.
