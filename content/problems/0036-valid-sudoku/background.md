Several independent constraints can be checked together by giving each group its own membership set. A cell belongs to exactly one row, one column, and one small box, so one visit can update all three groups and detect a conflict immediately.

### Everyday examples

- **Weekly schedule.** The same person cannot be booked in two places during one time slot, and cannot be booked twice for the same day-part. Checking both views at once catches conflicts faster than reviewing them separately.
- **Storage bins.** A shelf, a stack, and a small crate each may hold only one item of a given type. Repeating a type in any of those groupings is a conflict.

### How it shows up here

Rows, columns, and 3 by 3 boxes are the three groupings. Each gets nine sets. For every filled cell, compute its box from the row and column, then confirm the digit is absent from all three sets before adding it.
