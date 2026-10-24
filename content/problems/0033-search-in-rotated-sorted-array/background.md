Even after rotation, at least one half of any range is normally sorted. A rotated array has one wrap point; a midpoint splits the range so that one side does not contain the wrap. Identifying that side lets you test whether the target falls inside its sorted value range, then discard the other side.

### Everyday examples

- **A circular dial with numbered stops.** Numbers increase around the dial but wrap once. Choosing a halfway stop tells you which arc is continuous.
- **A shifted queue of tickets.** Ticket numbers are in order except for one jump, so the midpoint helps decide which side still has consecutive numbers.
- **A rotated list of chapters.** One side of the middle follows normal chapter order; if the desired chapter is in that side's range, the other side can be ignored.

### How it shows up here

Find the middle. If the left endpoint is no larger than the middle, the left half is sorted. A target inside that sorted range must be there, so search left; otherwise search right. If the left half is not sorted, the right half is, and the mirrored test chooses the side. If the middle itself matches, return it.
