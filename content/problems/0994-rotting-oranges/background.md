This is another multi-source BFS, but the answer is a time rather than a distance to one room. All rotten oranges start at minute 0 and infect outward simultaneously. Processing the queue one whole layer at a time makes each layer correspond to one minute.

### Everyday examples

- **A rumor in a group.** Everyone who knows the rumor tells all their immediate contacts during the same round, so the number of rounds measures how long the news takes to spread.
- **Dye in a channel network.** Dye enters at several openings at once and advances one segment per time step.

### How it shows up here

Count the fresh oranges and queue every rotten one. While fresh oranges remain and the queue is not empty, process exactly the current queue size, rot their fresh neighbors, and count one minute. If fresh oranges survive after the queue empties, they are unreachable, so the answer is `-1`.
