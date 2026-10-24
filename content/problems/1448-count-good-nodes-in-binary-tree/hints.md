## Hint 1

For a single root-to-leaf path, what information would let you decide whether each node is good without looking backward?

## Hint 2

Carry the largest value seen so far down each branch. When does a node's value qualify as good?

## Hint 3

Pass the updated maximum to both children. Equal values remain good, and each branch keeps its own history.
