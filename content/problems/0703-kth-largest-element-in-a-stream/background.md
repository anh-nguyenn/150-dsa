A priority queue serves the item with the highest or lowest priority first. A min-heap is a compact way to keep the smallest item at the front while still allowing fast insertion and removal. When a problem only needs a fixed number of extreme values, the heap can be capped at that size.

### Everyday examples

- **Leaderboard.** A game only displays the top ten scores. Once the board is full, a new low score is discarded immediately instead of being stored forever.
- **Fresh deliveries.** A warehouse keeps the three most recent shipments at the loading dock. An older shipment leaves as soon as a newer one arrives.

### How it shows up here

We care about the k largest values, so we keep exactly those in a min-heap. The smallest member of that group sits at the root, which is precisely the kth largest value. When a new number arrives, it joins the heap; if the heap grows beyond k, the smallest value leaves. The root then answers `add` in constant time.
