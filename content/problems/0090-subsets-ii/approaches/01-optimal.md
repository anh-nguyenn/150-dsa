## Idea

Sort the values so duplicates are adjacent. Record the current subset at each call, then extend it with each later value. Skip a value when it matches the value just before it at the same level of recursion.

## Why it works

Every distinct subset can be written with values in sorted order and with a unique first position for each chosen value. The forward-only loop produces those choices. The duplicate skip removes branches that pick a later copy of a value when the earlier copy was available at the same level, which is exactly the branch that would repeat an existing subset.

## Edge cases

- An empty input returns `[[]]`.
- A single value returns the empty subset and the one-value subset.
- Repeated values produce each subset once, including the subset containing all copies.
- Negative values sort and combine normally.
