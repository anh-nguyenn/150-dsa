## Idea

Sort the intervals by start time. Keep a list of merged blocks. For each interval, if it begins at or before the end of the last block, extend that block's end to cover both; otherwise begin a new block. The sorted order guarantees that once a block is left behind, no later interval can reach back into it.

## Why it works

Sorting by start ensures that any interval overlapping the current block appears while the block is still the last one. The two possible cases are exhaustive: the interval either touches or overlaps the block and must be merged, or it starts strictly after the block ends and is disjoint from it. Extending with the maximum end also handles intervals fully contained in the block. The output therefore contains exactly the union of the input ranges.

## Edge cases

- An empty input returns an empty list.
- A single interval is already merged.
- Intervals sharing an endpoint merge, since the comparison allows equality.
- A fully nested interval does not shrink the block because the maximum end is kept.
- Unsorted input is handled by sorting first.
