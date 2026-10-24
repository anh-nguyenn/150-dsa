## Hint 1

At each position of s3, the next character must come from the current front of s1 or the current front of s2. What state do you need to remember?

## Hint 2

Use the number of characters taken from each source as state. What should happen when the next character of s3 matches one candidate but not the other?

## Hint 3

Fill a table of prefix pairs; each cell looks up and left. Only the previous row is needed, so one row works when it is updated from left to right.
