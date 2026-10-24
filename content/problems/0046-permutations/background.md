Backtracking builds an answer incrementally and abandons a branch as soon as it cannot lead anywhere useful. For permutations, the order of choices matters: `[1, 2]` and `[2, 1]` are different answers, so the search must try every possible order rather than only forward-moving combinations.

### Everyday examples

- **Seating arrangements.** Four distinct people can sit in a row in many different orders. Swapping two people creates a genuinely different arrangement.
- **Race finishes.** A race with distinct runners has a different podium order for every ordering of the top finishers. First place versus second place matters.

### How it shows up here

The recursion fills one position at a time. At each position it may place any number that has not already been used. A boolean array records which numbers are currently in the partial permutation. When the partial permutation has the same length as the input, it is complete and gets copied into the answer.

After returning from a branch, the choice is undone: the number is removed from the partial permutation and marked unused. That restores the state so the next candidate can be tried in the same position.
