## Hint 1

Start with a pencil and paper. Pick one number and ask what other number would finish the pair. What would you need to remember to avoid checking everyone twice?

## Hint 2

For the current number `x`, the only useful partner is `target - x`. Can you test whether you have seen that partner before?

## Hint 3

Walk left to right with a map from value to index. Check for the complement before inserting the current value; that ordering also prevents using the same index twice.
