This is flood fill with a measurement attached. Instead of only marking a region, you count the cells you mark. Whenever a new land cell starts a region, explore the whole region, tally its cells, and compare that tally with the best seen so far.

### Everyday examples

- **Measuring a spill.** You walk over every connected wet tile once and keep a running count to learn the spill's size.
- **Counting rooms on a floor plan.** Connected open squares form one room; walking all of them gives its area in tiles.

### How it shows up here

Each unvisited `1` begins a flood fill. As cells leave the queue, increment a local size and mark them as water so they are skipped later. After the flood, update the maximum. Water contributes nothing, so the answer is 0 when the grid has no land.
