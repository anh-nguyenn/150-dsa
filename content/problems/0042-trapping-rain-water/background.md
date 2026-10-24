Water at a position sits below the lower of the two skyline walls that surround it. Instead of measuring both walls for every position, two pointers can carry the best wall seen so far from each side.

### Everyday examples

- **Puddles on uneven pavement.** A dip holds water only up to the height of the lowest surrounding ridge. The taller ridge on the other side does not matter once a lower one exists.
- **Roof gutters.** Each valley between raised edges fills up to the lower edge. The amount is the edge height minus the valley floor.

### How it shows up here

Keep a left pointer, a right pointer, and the tallest bar seen on each side. Whichever current bar is shorter is processed: its opposite side is guaranteed to offer a wall at least as tall, so the lower of the two maxima is already known. Add the difference between that maximum and the current height, then advance that pointer.
