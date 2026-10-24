## Idea

Build the directed graph and record how many prerequisites each course still has. Put every course with zero unmet prerequisites into a queue, then repeatedly take one course, count it, and lower the prerequisite count of each course that depends on it. A course joins the queue when its count reaches zero. At the end, compare how many courses were taken with the total number of courses.

## Why it works

Every course removed from the queue has all of its prerequisites already removed, so the removal order is a valid completion order. Each dependency edge is processed once. If a cycle exists, every course on it waits for another course on the cycle, so none of them ever reaches a prerequisite count of zero and the taken count stays below the total. Conversely, a graph with no cycle always has a course with no remaining prerequisites, so the process can consume everything.

## Edge cases

- A course with no prerequisites is available immediately.
- No dependency pairs means every course is independent, so the answer is true.
- A two-course cycle or a longer cycle leaves those courses unprocessed.
- A self-dependency is a cycle and makes the plan impossible.
- Disconnected groups of courses are fine as long as none of them contains a cycle.
