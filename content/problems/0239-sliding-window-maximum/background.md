A monotonic deque keeps candidates in a useful order while discarding ones that can no longer win. It is a queue with an extra rule: values inside it never increase from front to back.

### Everyday examples

- **A moving spotlight.** As a spotlight slides along a row, a tall object behind a newer, taller object can never be the highest visible point again.
- **A queue at a counter.** If a taller person joins behind shorter people, those shorter people are hidden and no longer matter for the current view.

### How it shows up here

Keep indices in a deque whose corresponding values decrease from front to back. Before adding a new index, remove indices at the back whose values are no larger, since the new value dominates them. Remove the front when it falls outside the window. After the window is full, the front is its maximum.
