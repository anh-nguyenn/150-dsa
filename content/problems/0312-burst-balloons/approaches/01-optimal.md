## Idea

Pad the list with a 1 at each end. Define `dp[left][right]` as the most coins obtainable by bursting every balloon strictly between the two boundary positions. For each interval, try every balloon as the last one burst; it earns `values[left] * values[mid] * values[right]`, and the remaining work splits into the intervals on either side.

## Why it works

If `mid` is the last balloon burst inside `(left, right)`, then at that moment every other balloon in the interval is gone, so `mid`'s neighbors are exactly the boundaries `left` and `right`. Bursts before that moment happen entirely to the left or entirely to the right of `mid`, and those two regions do not affect each other because `mid` remains as a separator. Therefore the total is the sum of the two independent subproblems plus the final burst. Taking the maximum over all choices of `mid` is exhaustive and optimal.

## Edge cases

- An empty list has no balloons to burst, so the answer is 0.
- A single balloon earns its own value because both neighbors are treated as 1.
- Two balloons are handled by choosing either one as the last burst; the better order wins.
- Balloons with value 0 contribute nothing but can still act as separators, so they must not be skipped.
- Large values and many balloons can produce large totals, which Python integers handle without overflow.
