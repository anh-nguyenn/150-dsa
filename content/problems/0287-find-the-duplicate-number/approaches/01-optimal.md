## Idea

Read `nums[i]` as the next node after index `i`. Detect a cycle with slow and fast pointers. After they meet, reset one pointer to the start and advance both one step at a time; their second meeting is the first index that belongs to the cycle, which is the duplicated value.

## Why it works

Every index has exactly one outgoing pointer, so the walk is deterministic. With `n + 1` indices and only `n` possible values, at least two indices share a value and a cycle is unavoidable. The standard two-phase Floyd argument shows that the second meeting occurs at the cycle entrance; that entrance value is the duplicate.

## Edge cases

- The duplicate is the smallest possible value, as in `[1, 1]`.
- The duplicate is the largest possible value, as in `[1, 2, 3, 4, 4]`.
- The value appears more than twice, as in `[2, 2, 2, 2, 2]`.
- The duplicate appears at the beginning or the end of the array.
- The array is never sorted or overwritten, and no hash set is allocated.
