Binary search repeatedly cuts a sorted search range in half. Looking at the middle value tells you which half can possibly contain the target: everything before the middle is too small, or everything after it is too large. The range shrinks geometrically, so even a huge sorted collection needs very few comparisons.

### Everyday examples

- **A paper dictionary.** You open near the middle, decide whether your word comes before or after that page, and ignore the other half.
- **Guessing a number.** When told whether a guess is too high or too low, the best next guess is halfway through the remaining possibilities.
- **Finding a date in a sorted log.** You jump to the middle entry, then continue in the earlier or later portion.

### How it shows up here

Two indices mark the current candidate range. Each step examines the middle. If it is the target, return that index. If it is smaller, discard the left half; if larger, discard the right half. When the range becomes empty, the target is not present.
