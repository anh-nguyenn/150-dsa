Closeness to the origin depends on the sum of squared coordinates. Taking a square root preserves the ordering, but it is unnecessary work and introduces floating-point values. A bounded heap can keep only the best candidates seen so far instead of storing every point.

### Everyday examples

- **Nearest cafes.** A map app wants the five cafes closest to your location, not a sorted list of every cafe in the city.
- **Parking search.** A driver only needs the three nearest available garages; once those are known, a fourth garage far away can be forgotten.

### How it shows up here

We scan every point and compute its squared distance. A max-heap of size `k` holds the closest candidates, with the farthest of those at the root. When a new point is closer than that root, the heap swaps it in. The heap therefore remembers exactly the k closest points without sorting the full input.
