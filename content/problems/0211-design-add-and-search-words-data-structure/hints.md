## Hint 1

A normal trie follows exactly one child per character. What happens at a dot, where several children could be correct?

## Hint 2

If a dot creates multiple possible branches, how can you check all of them while still respecting the remaining pattern?

## Hint 3

Store words in a trie and use recursive search. At a dot, recurse into every child; at a normal letter, recurse only into that child. The base case checks the end-of-word marker.
