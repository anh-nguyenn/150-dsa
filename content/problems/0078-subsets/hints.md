## Hint 1

Start with the list `[1, 2]`. Write down all four subsets by hand, then ask what changes when `3` is added.

## Hint 2

For each number there are exactly two possibilities: take it or leave it. What does one path from the top of that decision tree to a node represent?

## Hint 3

Keep a current partial subset and an index of the next number to consider. Record the partial subset at every recursive call, then try adding each later number and undo it afterward.
