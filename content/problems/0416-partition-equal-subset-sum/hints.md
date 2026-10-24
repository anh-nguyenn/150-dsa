## Hint 1

What does the parity of the total tell you before any subset is chosen?

## Hint 2

When the total is even, you need a subset whose sum is exactly half. Each number may be chosen or skipped once.

## Hint 3

Track reachable sums in a boolean array starting from zero, and iterate sums downward for each number so it cannot be reused. The answer is whether the half-total becomes reachable.
