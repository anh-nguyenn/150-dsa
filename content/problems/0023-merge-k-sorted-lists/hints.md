## Hint 1

If you merged the lists two at a time, what would the total cost be? Can you choose the next node by looking at all current heads instead?

## Hint 2

At each step you need the smallest of `k` current nodes. Which structure returns the minimum without scanning all `k`?

## Hint 3

Push every non-empty list head into a min-heap. Pop the smallest node, append it, and push its successor. A unique list index can serve as a tie-breaker.
