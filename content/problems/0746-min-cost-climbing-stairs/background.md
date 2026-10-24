Dynamic programming turns a question about the best path into a question about the best value at each position. You store the cheapest way to arrive somewhere, then extend to the next position using only nearby states.

### Everyday examples

- **Toll booths.** A highway charges at each booth you pass, and some booths can be skipped by taking a longer jump. The cheapest trip is built from the cheapest cost of reaching each booth.
- **Parking meters.** You walk down a street feeding meters; paying for one meter can let you skip the next, and you want the least total spent before reaching your destination.

### How it shows up here

Let `dp[i]` be the cheapest toll for standing on step `i`. You can arrive from `i - 1` or `i - 2`, and arriving means paying the toll of the step you left. The virtual top sits at index `n`, so the answer is `dp[n]`.
