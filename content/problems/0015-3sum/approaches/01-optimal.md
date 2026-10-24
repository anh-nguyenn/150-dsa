## Idea

Sort the array, fix the first value of each candidate triplet, and use two pointers to find the pair that completes the sum to zero. Skip duplicate fixed values and duplicate pointer values.

## Why it works

After sorting, every triplet can be written with its smallest value first. Fixing that value at `i` reduces the task to Two Sum on the suffix. The two-pointer sweep finds every pair for that fixed value because moving the smaller side right increases the sum and moving the larger side left decreases it. Duplicate skips ensure each value pattern is emitted once.

## Edge cases

All zeros produce exactly one triplet. Fewer than three values or a strictly positive array produce nothing. Repeats such as several `-1` values are handled by skipping duplicate fixed values. A triplet may include two equal values, as in `[-1, -1, 2]`.
