A running maximum is the largest value encountered so far while moving through a sequence. It only changes when a new value exceeds it, and it gives a compact summary of everything behind you. On a tree, each root-to-node path has its own running maximum.

### Everyday examples

- **A hiking trail with elevation signs.** A sign feels like a new high point only if its elevation beats every sign before it on the trail. Side trails have separate histories.
- **Personal bests in a game.** A score at the end of a round is a record only if it beats your previous best. If you switch to a different game, that game's history is what matters.

### How it shows up here

A depth-first walk carries the largest value seen from the root along the current branch. When the walk reaches a node, compare its value with that carried maximum: a node is good when its own value is not smaller. Then update the maximum and pass it to both children.

The important detail is that the maximum travels down the call stack, not globally across the tree. A large value in one branch must not disqualify nodes in a sibling branch.
