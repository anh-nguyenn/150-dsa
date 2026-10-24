## Hint 1

At any prefix, what relationship must hold between the number of opens and the number of closes?

## Hint 2

When is it legal to add an opening parenthesis? When is it legal to add a closing one?

## Hint 3

Recurse with counts of opens and closes. Add `(` while opens are below `n`, add `)` only while closes are below opens, and save the string when its length reaches `2n`.
