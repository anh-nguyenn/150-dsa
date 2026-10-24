## Idea

Flood fill backward from the Pacific edges and from the Atlantic edges. In this reverse direction you may step to a neighbor only if it is at least as high as the current cell. Return the coordinates found by both fills.

## Why it works

A reverse path from an ocean cell to a cell exists exactly when water can flow forward from that cell to the ocean, because each reverse step uses an equal-or-higher neighbor. Running the fill once per ocean marks cells that can reach that ocean, and the intersection marks cells that can reach both in linear time.

## Edge cases

- An empty grid returns an empty list.
- A single cell touches both oceans and qualifies.
- With one row or one column, every cell touches two opposite edges.
- Equal heights allow flow, so plateaus must be connected in the search.
- Border cells are seeds for their ocean even if they are low.
