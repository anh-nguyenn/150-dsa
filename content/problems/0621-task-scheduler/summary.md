Given a list of task labels and a cooldown `n`, find the minimum number of time units needed to finish all tasks. The same task must be separated by at least `n` units, and the CPU may sit idle when no legal task is available. Different tasks may run back to back.

**Example**

```text
tasks = [A, A, A, B, B, B], n = 2  ->  8
```

**Constraints, in plain words**

- Between 1 and 10,000 tasks.
- Each label is an uppercase English letter.
- The cooldown is between 0 and 100.
- The answer is a count of time units, including idle slots.

[Task Scheduler on LeetCode](https://leetcode.com/problems/task-scheduler/)
