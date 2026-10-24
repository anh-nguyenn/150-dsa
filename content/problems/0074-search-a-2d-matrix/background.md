The matrix is ordered as if all its rows were laid end to end into one long sorted list. That means a single binary search can treat it as flat, converting a flat index back into a row and column when needed.

### Everyday examples

- **A multi-volume dictionary.** Volumes are in order, and pages within each volume are in order, so the whole set behaves like one long sorted sequence.
- **A stadium with numbered sections.** Seats increase along a row and continue increasing from the end of one row to the start of the next. Finding a seat can ignore half the stadium at a time.
- **A calendar split into months.** Days are ordered within a month and months continue the order, so a date can be located without scanning every day.

### How it shows up here

Treat the matrix as `rows * cols` sorted positions. A flat midpoint maps to `matrix[mid // cols][mid % cols]`. Ordinary binary search then either finds the target or rules out half of the flattened positions.
