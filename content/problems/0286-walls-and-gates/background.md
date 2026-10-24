When several starting points should expand at the same speed, a multi-source BFS handles them together. All sources enter the queue at distance 0. Each layer of the queue represents one more step, so a cell is first reached by whichever source is closest.

### Everyday examples

- **Ripples from several stones.** Drop all stones at once and the first ripple to reach a point comes from the nearest stone.
- **Emergency response.** Several stations dispatch at the same moment; the first crew to arrive at a location is the closest one.

### How it shows up here

Put every gate in one queue. Expand outward through empty rooms, writing the distance as the previous room's distance plus one. The first value written to a room is final because BFS explores in order of increasing distance. Walls and already-filled rooms are simply skipped.
