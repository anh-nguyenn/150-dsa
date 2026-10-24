Finding islands is a flood-fill problem. Once you step on land, you spread through every land cell reachable from it and mark those cells as visited, so the same region is never counted twice. The boundary of the region is simply water and the edge of the grid.

### Everyday examples

- **Paint bucket.** Clicking a colored region fills every connected pixel of that color and stops where the color changes.
- **Mold on bread.** A patch grows into neighboring spots, but two patches separated by a clean gap stay separate.

### How it shows up here

Scan the grid in reading order. Each unvisited land cell starts a new island: increase the count, then flood outward through the four neighbors, marking land as visited along the way. When the flood ends, continue the scan. The number of floods you start is the number of islands.
