## Hint 1

If the intervals were sorted by start, could you decide whether the next one continues the current merged block?

## Hint 2

What should happen when the next interval starts exactly where the current block ends?

## Hint 3

Sort by start, keep one running interval, and extend its end whenever the next start is not beyond it.
