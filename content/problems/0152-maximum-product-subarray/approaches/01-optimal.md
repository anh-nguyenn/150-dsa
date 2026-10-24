## Idea

Scan once while maintaining `cur_max` and `cur_min`, the largest and smallest products of subarrays ending at the previous position. For each new value, compute the three candidates (value alone, previous max times value, previous min times value), take their maximum and minimum, and track the largest maximum encountered.

## Why it works

Every subarray ending at the current position is either the single current element or an extension of a subarray ending at the previous position. The best extension uses one of the two extreme previous products, because multiplying by a fixed number preserves order when it is positive and reverses it when it is negative. Thus the two extremes capture all possibilities, and the best over all ending positions is the answer.

## Edge cases

- A single element returns itself, including a negative one.
- A zero resets the running products, but zero can still be the best answer when everything else is negative.
- An even number of negatives can make a long subarray the winner, so the minimum must be retained.
- All-negative input is handled by the sign flip.
- The maximum may occur before the end of the array; the running best remembers it.
