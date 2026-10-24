## Idea

Process exactly 32 bits. Pull off the input's least significant bit and push it onto the right side of a growing result, shifting the result left each round.

## Why it works

After `k` rounds the result holds the `k` bits removed from the input, in reverse order. Shifting left before appending keeps earlier bits in place while making room for the next one. Running exactly 32 rounds accounts for leading zeros, so the output always represents a full 32-bit reversal.

## Edge cases

- Input 0 produces 0; every extracted bit is 0.
- Input 1 produces 2^31 because its single set bit moves from the right end to the left end.
- All-ones input is unchanged by reversal.
- Doing only enough iterations to clear `n` would drop leading zeros, so the loop must always run 32 times.
