## Idea

Keep a stack of indices whose warmer day has not been found yet, with temperatures decreasing from bottom to top. For each new day, pop every waiting day that is colder than today, because today is its nearest warmer day. Then push today as a new waiting day.

## Why it works

The stack always holds days in increasing index order with non-increasing temperatures. When today's temperature is higher than the top, today is the first day after that top day that beats it, since any earlier warmer day would already have popped it. Popping continues until the top is at least as warm, preserving the decreasing order. Every day is pushed once and popped once, so the total work is linear.

## Edge cases

- A strictly decreasing sequence leaves every answer at 0.
- Equal temperatures do not count as warmer, so they remain on the stack together.
- A single day returns `[0]`.
- A strictly increasing sequence gives every answer 1 except the last, which is 0.
- The final unresolved days keep their initial 0 values.
