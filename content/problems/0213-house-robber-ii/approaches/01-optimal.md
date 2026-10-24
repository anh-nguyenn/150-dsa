## Idea

Break the circle by considering two straight-line rows: one that removes the last house and one that removes the first. Run the rolling House Robber recurrence on each and return the larger total.

## Why it works

Every valid circular selection omits house `0` or omits house `n - 1`; otherwise the two ends would both be chosen and they are adjacent. The first linear run covers selections that include house `0` but not the last, and the second covers selections that include the last but not house `0`. Some selections appear in both, which is harmless because we take a maximum, and no valid selection is missed.

## Edge cases

- One house: the circle has no real adjacency, so return its value directly.
- Two houses: they are adjacent, so return the larger amount.
- All zeros: both runs return 0.
- The helper takes a half-open range, so the two runs never include both ends.
