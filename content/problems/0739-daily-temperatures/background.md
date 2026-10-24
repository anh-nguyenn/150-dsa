A monotonic stack keeps its values in one direction, usually increasing or decreasing. When a new value breaks that order, it resolves the items that were waiting for exactly such a value. Each item is pushed once and popped at most once, which is why the method stays linear.

### Everyday examples

- **People waiting for a taller person.** Shorter people in line are blocked from seeing until someone taller arrives. The newest unresolved people are the easiest to resolve.
- **Support tickets waiting for a fix.** A ticket stays open until a later event resolves it. When the event arrives, you close the most recent unresolved tickets that it covers.
- **Stock prices looking for a higher price.** Each day waits for the next day whose price exceeds it; days that never get one remain at zero.

### How it shows up here

Days that have not yet found a warmer day wait on a stack whose temperatures decrease from bottom to top. A new, warmer day pops every waiting day it beats and records the gap in indices. Days that are not beaten stay on the stack until a later, even warmer day arrives.
