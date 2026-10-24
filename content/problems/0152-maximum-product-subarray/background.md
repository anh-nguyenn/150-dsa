Products are less forgiving than sums because multiplying by a negative flips the sign. A very negative product can become the largest one after another negative number, so a single "best so far" value is not enough.

### Everyday examples

- **Profit and loss streaks.** A run of percentage changes can swing from a large loss to a large gain when another negative change arrives.
- **Altitude changes.** Multiplying signed elevation adjustments means the most negative running value may later become the most positive.
- **Signal inversion.** Two sign flips in a row restore the original direction, so the smallest value deserves as much attention as the largest.

### How it shows up here

For subarrays ending at the current position, only two products matter: the largest and the smallest. Extending either one by the next number gives all candidates for the new ending position. When the next number is negative, the largest and smallest swap roles, which is why both must be carried forward.
