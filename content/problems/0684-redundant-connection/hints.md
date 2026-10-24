## Hint 1

Build the graph incrementally in the order the edges are given. At what moment does a cycle first appear?

## Hint 2

An edge is unnecessary when its endpoints were already connected before that edge is added. What structure lets you test that quickly?

## Hint 3

Use disjoint sets. Scan the edges, merging different groups; the first edge whose endpoints already share a root is the answer.
