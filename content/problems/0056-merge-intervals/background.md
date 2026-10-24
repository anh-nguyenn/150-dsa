A sweep over sorted intervals is the standard way to combine ranges. Sorting by start time puts every potential overlap next to the block it might extend. While scanning, only the end of the current merged block matters for deciding whether the next interval joins it.

### Everyday examples

- **Shift coverage.** Several people report overlapping working hours. Sorting their shifts and combining overlaps gives the true periods when the office is staffed.
- **Downloaded chunks.** A file arrives in pieces that may overlap. Merging the byte ranges shows which parts are complete.
- **Parking sessions.** Multiple sensors may record the same car; combining overlapping timestamps yields one continuous stay.

### How it shows up here

After sorting by start, walk through the intervals while maintaining the last merged block. If the next interval starts no later than the block's end, extend the block's end; otherwise start a new block. Because the input is sorted, no earlier block can overlap a later one that was already closed.
