## Idea

Build the graph and count unmet prerequisites for each course. Place all zero-count courses in a queue. Pop a course, append it to the answer, and decrease the prerequisite count of every course that depends on it. Whenever a dependent course reaches zero, enqueue it as well. At the end, return the recorded order only if it contains every course.

## Why it works

A course is appended only after all of its prerequisites have already been appended, because its count reaches zero only when every incoming edge has been removed. Thus the result respects every dependency. Every edge is handled once. If the graph contains a cycle, the courses on the cycle never lose their last prerequisite and the answer stays short, so the length check correctly rejects the input.

## Edge cases

- A single course with no prerequisites returns a one-element order.
- No prerequisites at all still produces a complete order.
- An empty course set produces an empty order, which also satisfies the length check.
- A cycle anywhere leaves the answer short and must produce an empty list.
- Courses outside the cyclic part may be placed successfully, but the final check still rejects the whole schedule.
