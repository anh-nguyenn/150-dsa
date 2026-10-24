## Idea

Treat the digit-square rule as a path through numbers. Send one walker one step at a time and another two steps at a time; a meeting means a loop.

## Why it works

The rule maps every positive integer to a non-negative integer, so the sequence is a functional graph: from any state there is exactly one next state. In such a graph, either the path ends at 1 or it eventually enters a cycle. Floyd's two-walker method finds any cycle because the fast walker closes the distance by one state per round. If the fast walker reaches 1, the path ended without a cycle, so the number is happy.

## Edge cases

- `n = 1` is happy immediately; both walkers start at 1.
- Known unhappy inputs such as `2` and `4` eventually meet inside their cycle.
- Large inputs are fine because each digit-square step quickly reduces the number's size.
- Zero digits contribute nothing and do not disturb the loop.
