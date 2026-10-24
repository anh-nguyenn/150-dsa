Dynamic programming on a grid records an answer for every prefix of the problem, then builds larger answers from smaller ones. Here a prefix is a particular cell, and the stored answer is the number of ways to reach it.

### Everyday examples

- **A staircase with two choices.** If each step lets you climb one stair or two, the number of ways to reach stair `n` is built from the counts at `n - 1` and `n - 2`. You do not enumerate every path; you add the two smaller results.
- **A rectangular street grid.** A courier who only travels east and south can reach an intersection either from the intersection to its west or the one to its north. Counting routes is adding those two incoming counts.
- **Filling a spreadsheet.** A cell defined as the sum of the cell above it and the cell to its left is computed without redoing the earlier arithmetic, because each prerequisite cell already holds its final value.

### How it shows up here

The first row and first column are easy: every route to those cells is forced to keep moving in one direction, so each has exactly one route. Interior cells receive traffic from the cell above and the cell to the left. Filling the table in row order makes both of those counts available before they are needed.
