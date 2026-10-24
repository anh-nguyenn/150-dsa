## Idea

Keep a set of values already visited. For each value, check membership before inserting it into the set.

## Why it works

A repeated value must either be the first occurrence or a later one. On its later occurrence the set already contains it, so the check fires. If the loop finishes, every value was inserted exactly once, which means there was no repeat.

## Edge cases

- A single element cannot contain a duplicate, so the result is false.
- Negative values and zero work exactly like positive values.
- A repeat at the very end is still found because the set holds every earlier value.
- The constraints guarantee at least one element, but an empty list correctly returns false.
