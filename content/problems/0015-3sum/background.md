Sorting turns a search for three values into a search for two values around a fixed one. That is the same squeeze pattern as Two Sum II, repeated for each possible first value.

### Everyday examples

- **Splitting a bill.** Three friends need their shares to balance to zero. If you fix one person's share, the other two must make up the exact opposite amount.
- **Packing three weights.** After lining weights up by size, you can test a light and a heavy weight against a target without trying every combination.

### How it shows up here

Sort the array. Fix the smallest value of the triplet at index `i`. The remaining two values must sum to `-nums[i]`, so two pointers search the sorted suffix. Duplicate work is removed in two places: skip a fixed value equal to the previous one, and after finding a triplet, skip equal values at both moving pointers. Once the fixed value is positive, no later triplet can sum to zero.
