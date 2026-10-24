## Idea

Scan the grid until an unvisited `"1"` appears. That cell starts a new island: bump the counter, then flood outward with a queue, turning every reached land cell into `"0"` so it will not be processed again.

## Why it works

Flood fill visits exactly the cells in one connected component. Marking a cell before adding its neighbors prevents revisiting, and since every land cell belongs to exactly one component, each component is counted once.

## Edge cases

- An empty grid or an empty first row returns 0.
- A single land cell is one island.
- Diagonally touching land cells are separate islands.
- One island that touches every edge still counts only once.
- A dense grid can fill the queue with most of its cells.
