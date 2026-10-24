## Hint 1

Compare the smallest remaining value in each list. Which node must come next in the merged result?

## Hint 2

A placeholder node before the result means you never need a separate branch for the first node you attach.

## Hint 3

Keep a tail pointer, attach the smaller current node, and advance that list. Once one list is empty, attach all of the other list.
