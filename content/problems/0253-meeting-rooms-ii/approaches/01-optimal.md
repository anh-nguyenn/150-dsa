## Idea

Sort meetings by start time. Maintain a min-heap holding the end times of rooms currently in use. For each meeting, if the earliest ending room is free by the meeting's start, release that room and reuse it; then record the new meeting's end. The heap size after processing everything is the number of rooms required.

## Why it works

Processing in start order means every room in the heap is occupied by a meeting that has already begun. Reusing the room that frees up earliest is always safe and never worse than opening another room, since only the smallest end matters. The heap size at any point is the number of concurrent meetings, and its maximum is the peak overlap, which is a lower bound on rooms. The algorithm attains that bound.

## Edge cases

- An empty schedule needs zero rooms.
- A single meeting needs one room.
- Touching meetings can share a room because the reuse check allows equality.
- All meetings overlapping at once each need a separate room.
- Input order does not matter because the list is sorted first.
