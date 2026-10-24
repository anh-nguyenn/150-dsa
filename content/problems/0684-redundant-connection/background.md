A tree has no cycles, and adding one edge to a tree must create exactly one cycle. The extra edge is the one that closes that loop. Finding it is a matter of remembering which nodes are already linked as the edges are read.

### Everyday examples

- **Roads.** A road network that already connects every town does not need a second road between two towns that are already reachable; that extra road creates a loop.
- **Cabling.** Connecting two outlets that are already on the same circuit adds a redundant path and can create a dangerous ring.
- **Org charts.** If every employee already reports up to one root, adding a second reporting line between two people in the same chain creates circular responsibility.

### How it shows up here

Read the edges in order and keep track of connected groups. Most edges join two different groups and are useful. The first edge whose endpoints already belong to the same group is the one that closes the cycle. Because the input is a tree plus a single edge, that edge is also the last edge of the cycle in input order, which matches the required tie-breaking.
