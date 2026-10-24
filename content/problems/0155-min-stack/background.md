A running minimum is the smallest value seen so far. Keeping one is easy while values only arrive, but a stack also removes values. Once the current minimum is removed, the minimum must roll back to what it was before that value was added.

### Everyday examples

- **Lowest price while shopping.** You track the cheapest price seen today. If you discard the most recent receipt, you may need the previous cheapest price, not a fresh scan of every receipt.
- **Scoreboard history.** A game shows the best score so far after each round. Undoing the last round should restore the previous best, which may be lower or higher than the current one.
- **Altitude record.** A hiker notes the lowest altitude reached at each point. Walking back along the trail should reveal the record that applied just before the latest step.

### How it shows up here

A second stack records the minimum that applies at each depth. Its top always answers `getMin`. When a value is pushed, the minimum either stays the same or becomes the new value. When a value is popped, the matching minimum entry leaves only if that value was setting the record.
