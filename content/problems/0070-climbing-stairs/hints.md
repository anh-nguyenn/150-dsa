## Hint 1

Work out the answer by hand for `n = 1, 2, 3, 4`, and write the four numbers in a row. Do you notice how each one relates to the two before it?

## Hint 2

Think about the last move. Whatever route you took, it ended with either one step or two steps. What two smaller questions does that split the count into?

## Hint 3

Let the count for `k` steps be the sum of the counts for `k - 1` and `k - 2`. Seed the first two values and keep only the latest pair as you walk upward.
