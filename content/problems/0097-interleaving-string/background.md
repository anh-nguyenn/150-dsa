Merging two ordered sequences without disturbing either order is a constrained choice at every position. A grid of prefix pairs records whether a prefix of the merged string can be built from prefixes of the two sources.

### Everyday examples

- **Two queues at a counter.** Customers from two lines are served one at a time, but the relative order within each line is preserved. Given a service order, decide whether it could have come from those two lines.
- **Merging two playlists.** You shuffle songs from two playlists while keeping each playlist's internal order. A proposed merged playlist is valid only if it can be split back into the two original orders.
- **Weaving two strands.** Two strands are woven without reversing either. A finished pattern is possible only if every character can be attributed to the next unused character of one strand.

### How it shows up here

Let `dp[i][j]` mean that the first `i + j` characters of `s3` can be formed from the first `i` characters of `s1` and the first `j` characters of `s2`. A transition consumes the next character of `s1` or of `s2` when it matches the next character of `s3`. Since each row depends only on the previous row and the current row's left neighbor, one row is enough.
