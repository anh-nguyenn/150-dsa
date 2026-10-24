Interval dynamic programming solves problems where the last decision splits a contiguous range into two independent ranges. Instead of choosing the first action, it is often easier to choose the final action, because after the final action the left and right parts no longer interact. This flips the usual order of reasoning and removes the awkward dependence on changing neighbors.

### Everyday examples

- **Demolishing a row of buildings.** The last building removed has clear space on both sides, which makes its payoff easy to state. Earlier removals then split the row into independent sections.
- **Cutting a log into pieces.** The final cut separates the log into two pieces that can be optimized separately; the cost of that cut depends only on its endpoints.
- **Scheduling the last meeting in a day.** Once the final meeting is fixed, the morning and afternoon can be planned independently.

### How it shows up here

Padding the array with a 1 on each end gives every real balloon fixed boundary neighbors. For an interval between two boundary balloons, guess which balloon is burst last inside it. That last balloon sees only the two boundary values, and the balloons to its left and right form smaller independent intervals. Trying every possible last balloon yields an interval DP with three nested loops.
