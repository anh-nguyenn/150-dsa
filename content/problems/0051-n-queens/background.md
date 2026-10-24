Backtracking is a natural fit for constraint satisfaction: make a choice, check that it does not violate any rule, continue, and undo the choice if the branch fails. Good pruning rejects a bad partial arrangement immediately instead of waiting until the board is full.

### Everyday examples

- **Seating guests with conflicts.** You seat people one table at a time. If a new guest conflicts with someone already seated, you try a different seat instead of finishing the whole arrangement and starting over.
- **Scheduling talks.** You assign one time slot per room while avoiding clashes. As soon as a slot conflicts with an existing booking, that partial schedule is abandoned.

### How it shows up here

Place queens one row at a time. Since each row gets exactly one queen, row conflicts are handled automatically. The only things to track are which columns, which down-right diagonals, and which up-right diagonals are already occupied. A diagonal has a constant value of `row + col` or `row - col`, so those two numbers identify it uniquely.

When a square is free in all three sets, place the queen, add its column and diagonals to the sets, and recurse on the next row. After the recursive call, remove them so the next column can be tried. Reaching row `n` means every queen is placed legally.
