## Idea

Walk through the array once. Keep the best sum of a slice ending at the current index, and the best sum seen so far. At each step, either extend the previous slice or restart at the current value, whichever is larger.

## Why it works

Any slice ending at position `i` is either the single value at `i` or a slice ending at `i - 1` with `nums[i]` appended. Keeping the better of those two covers every candidate. The global maximum therefore records the best slice overall, and a negative running prefix is naturally dropped because restarting wins.

## Edge cases

- A single element returns that element.
- When every value is negative, the answer is the largest (least negative) single value.
- When every value is positive, the whole array is best.
- Zeros neither help nor hurt; restarting on a zero ties with extending.
- Python integers handle the maximum possible sum without overflow.
