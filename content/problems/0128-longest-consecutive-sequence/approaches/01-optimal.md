## Idea

Store all values in a set. Only begin counting at values whose predecessor is missing, then extend upward while each following value is present.

## Why it works

Every consecutive run has exactly one starting value: the one with no predecessor in the set. By counting only from those starts, the algorithm measures each run once and skips every interior value. The total number of upward steps across all starts is bounded by the number of distinct values, so the overall work is linear.

## Edge cases

- An empty list has no run, so the answer is 0.
- Duplicates collapse into a single set entry and do not inflate the length.
- Negative runs are counted the same way as positive runs.
- A list with no consecutive pairs returns 1 when it is non-empty.
- The entire list can form one run; the start is found at its smallest value.
- Values far apart do not create gaps in the count because expansion stops at the first missing value.
