## Idea

Count how often each task appears. Let `f` be the largest frequency and `c` the number of tasks that appear `f` times.

Arrange the `f` copies of the busiest tasks in `f - 1` full blocks of length `n + 1`, followed by a final block containing the `c` tied tasks. If there are enough other tasks to fill every gap, the schedule is simply the total number of tasks; otherwise the skeleton length is required.

## Why it works

Every pair of consecutive copies of a maximally frequent task needs at least `n` time units between them, which produces the block structure. Tasks with smaller frequencies can be placed inside those gaps without violating their own cooldowns. When the task count exceeds the skeleton, the gaps fill completely and no idle time is needed, so the total length is the task count.

## Edge cases

- With `n = 0`, tasks can run back to back, so the answer is the task count.
- A single task type fills every gap with idle time.
- Several tasks tied for maximum frequency each need one slot in the final block.
- Many distinct tasks can fill all gaps and make the task count the larger value.
