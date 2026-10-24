## Hint 1

For subsequences of the same length, which ending value leaves the most room to extend later?

## Hint 2

Keep the smallest achievable last value for each length. A new number can replace the first last value that is not smaller than it.

## Hint 3

The candidate list stays sorted. Binary search finds the replacement position, and the list length is the answer, giving `O(n log n)` time.
