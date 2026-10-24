## Hint 1

Why can you not fill in every `random` pointer during the first pass, before all copies exist?

## Hint 2

If you could look up the copy of any original node instantly, what would you store in that lookup table?

## Hint 3

First create a copy of every node and record original -> copy. Then set each copy's `next` and `random` by translating the original pointers through the map.
