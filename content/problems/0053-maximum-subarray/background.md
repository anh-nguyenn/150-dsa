A running total is useful only while it helps the future. Once a partial sum has become a drag, keeping it around makes every later slice worse. The greedy idea is to decide, at each position, whether to extend the previous slice or start fresh with the current value.

### Everyday examples

- **A losing streak.** A team tracks its best point differential over a stretch of games. If the current stretch is deep in the negative, the next game is better treated as the start of a new stretch.
- **Weekly spending.** A budget watcher looks for the best consecutive run of days. A run that has already lost more than it gained is abandoned before adding tomorrow's numbers.

### How it shows up here

Scan the array once while keeping two values: the best sum of a slice that ends at the current position, and the best sum seen anywhere so far. At each new number, either append it to the slice ending just before, or begin again at this number. This local choice is enough because a prefix with a negative sum can never improve a later slice.

The answer is the largest value the running local best ever reaches.
