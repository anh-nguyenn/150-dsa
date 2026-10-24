## Hint 1

Group positions by how many jumps they require. All positions reachable in the same number of jumps form one continuous range.

## Hint 2

While scanning the current range, record the farthest position that can be reached from anywhere inside it. That becomes the next range.

## Hint 3

Count a new layer whenever the scan reaches the current range's end, and stop the loop before the final position.
