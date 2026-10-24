A spiral walk stays on the outside of a shape, moves along one edge at a time, and then continues along the next edge just inside the previous one. The important bookkeeping is not the values but the four boundaries that describe the unvisited rectangle: its top row, bottom row, left column, and right column.

### Everyday examples

- **Peeling an orange.** You remove the skin in one continuous strip around the fruit, turning it as you go; the remaining fruit gets smaller.
- **Walking around a block.** You go along the front, turn at the corner, go down the side, turn again, and keep walking around the ever-smaller inner block.

### How it shows up here

The grid starts with boundaries at its four edges. After walking the top row, that row is finished, so the top boundary moves down. After the right column, the right boundary moves left, and so on. When two boundaries cross, the unvisited region is empty and the walk stops.

Thin grids are the tricky part: after the top and right walks, a single remaining row or column should not be read twice. Guarding the bottom and left walks with a boundary check prevents that.
