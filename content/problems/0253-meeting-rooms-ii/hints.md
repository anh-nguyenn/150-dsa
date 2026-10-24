## Hint 1

What is the smallest number of rooms if you only look at the busiest instant?

## Hint 2

When a new meeting starts, how can you tell whether some existing room has already become free?

## Hint 3

Sort by start time and keep a min-heap of end times. Reuse the earliest end when it is no later than the new start, then push the new end.
