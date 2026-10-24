## Hint 1

Sorting would reveal consecutive runs, but it costs more than linear time. What structure answers "is this exact value present?" quickly?

## Hint 2

If a value's predecessor is also in the set, can that value be the beginning of a run? How could that observation reduce repeated work?

## Hint 3

Put every value in a set. Start counting only at values whose predecessor is absent, then walk upward while each next value exists, tracking the longest run.
