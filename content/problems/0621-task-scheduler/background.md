Scheduling problems often revolve around the most frequent item. If one task appears many times, it creates fixed gaps that other tasks can fill. Counting frequencies is enough to measure those gaps without simulating every time unit.

### Everyday examples

- **Baking batches.** A tray must cool for two minutes before the next batch of the same recipe, while a different recipe can use the oven in between.
- **Meeting buffers.** A person needs a break between back-to-back meetings with the same client, but can meet another client during that gap.

### How it shows up here

The most frequent task determines the skeleton of the schedule. If its frequency is `f`, there are `f - 1` gaps between its occurrences, and each gap needs `n` units. Other tasks either fill those gaps or force the schedule to grow when there are too many of them to fit.
