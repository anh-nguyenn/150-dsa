## Hint 1

Decide only about the last house in a row. What are the two possibilities, and what does each leave you with?

## Hint 2

If you skip the last house, the answer is whatever the previous houses gave. If you take it, the house before it is unavailable.

## Hint 3

Let `best[i] = max(best[i-1], best[i-2] + nums[i])`; seed the two values before the row with 0 and roll two variables.
