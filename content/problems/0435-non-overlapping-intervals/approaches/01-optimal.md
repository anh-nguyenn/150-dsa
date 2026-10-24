## Idea

Sort intervals by their end time. Accept the first, then scan forward. An interval can be kept if its start is at least the end of the last accepted interval; otherwise it overlaps and must be removed. Always keeping the earliest-ending compatible interval is the greedy choice.

## Why it works

Among all intervals, the one ending earliest can always be part of some maximum compatible set: replacing whichever interval an optimal solution chose first with this earliest finisher cannot create new conflicts. Repeating the argument after each accepted interval shows the greedy count is optimal. Every rejected interval overlaps the last accepted one, so the number of rejections is the minimum number of removals.

## Edge cases

- An empty list needs no removals.
- A single interval is already non-overlapping.
- Touching intervals such as `[1,2]` and `[2,3]` are both kept because the check is strict.
- Intervals contained in another are rejected when they overlap the accepted block.
- Sorting by end rather than start is essential for the greedy argument.
