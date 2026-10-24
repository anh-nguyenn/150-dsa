Dynamic programming is what you reach for when a big answer can be assembled from answers to smaller versions of the same question. Instead of enumerating every route, you record a few numbers and build forward, reusing work you have already done.

### Everyday examples

- **Paving a path.** A garden path is filled with slabs that are either one metre or two metres long. The number of ways to finish depends only on how much path is left, not on how you got there.
- **A playlist.** You may play the next song or skip one. Counting the ways to land on a particular track again depends on the two tracks before it.

### How it shows up here

The state is simply the step number. The number of routes to step `k` is the sum of the routes to `k - 1` and `k - 2`, because the final move was either a single or a double. Since each value depends on the previous two, two rolling variables replace a whole table.
