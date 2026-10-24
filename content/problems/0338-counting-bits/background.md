A population count table is a small lookup table that stores how many 1 bits each number has. Building it naively by scanning every bit of every number costs more than necessary because neighboring numbers share most of their bits.

Shifting a binary number right by one removes its last bit. The shifted value is smaller, so its count can already be known; adding the removed last bit gives the count for the original number.

### Everyday examples

- **Family tree.** Each generation is a smaller version of the previous one. To count people in a branch, reuse the count for the parent and add the new child.
- **Building a staircase.** Every step rests on the step below it. You do not rebuild the entire staircase for each new step.

### How it shows up here

For `i`, the value `i >> 1` is `i` without its final bit, and `i & 1` is that final bit. Therefore `bits[i] = bits[i >> 1] + (i & 1)`. Since `i >> 1` is smaller than `i`, its answer is already available when filling the table from left to right.
