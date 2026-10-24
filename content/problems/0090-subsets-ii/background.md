When a backtracking search runs over repeated values, different branches can produce the same answer. Sorting the input groups equal values together, and a simple rule removes the redundant branches: at one level of the decision tree, try only the first copy of a value.

### Everyday examples

- **Choosing fruit from a bowl.** Two identical apples are separate pieces of fruit, but a bowl containing one apple looks the same whichever apple you picked. The result depends on how many apples you took, not which copy.
- **Building words from letter tiles.** Duplicate letter tiles can spell the same word in several physical ways. A word list should show that word only once.

### How it shows up here

After sorting, equal numbers are adjacent. The recursion still records every partial subset, because the empty subset and every partial choice are valid answers. At a given position in the search, if the current number equals the previous number and the previous number was not chosen at this level, the current branch is skipped. This keeps one representative for each distinct subset.

The search only moves forward, so each subset is built in sorted order and no subset is assembled twice in different orders.
