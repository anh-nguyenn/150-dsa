## Idea

Sort the meetings by their start times. Then walk through the list and compare each meeting's start with the previous meeting's end. Any start that falls strictly before that end means two meetings overlap, so the person cannot attend all of them. If no such pair exists, every meeting can be attended.

## Why it works

A start that falls before the immediate predecessor's end is a genuine overlap, so returning false is always correct. If no such adjacent pair exists, no pair overlaps at all: between any two conflicting meetings in start order there would be some first adjacent conflict. Since the scan would catch that pair, a full pass with no failure proves the whole schedule is compatible.

## Edge cases

- An empty schedule is trivially attendable.
- A single meeting is always attendable.
- Touching meetings such as `[1,5]` and `[5,10]` are fine.
- Sorting handles input given in arbitrary order.
- Three or more chained meetings are checked pairwise after sorting.
