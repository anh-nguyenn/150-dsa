## Hint 1

Consider subarrays that end at the current index. If you knew their largest product, would you also need anything else before reading the next number?

## Hint 2

A negative next value turns a large positive product into a large negative one, and a large negative product into a large positive one. Keep both extremes.

## Hint 3

At each step, form candidates from the current value, the previous maximum times it, and the previous minimum times it. Update the running maximum and minimum, and remember the best maximum seen.
