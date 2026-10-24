## Hint 1

Which courses could safely appear first in the ordering? Start from the ones with nothing blocking them.

## Hint 2

After you place a course, the courses that depended on it have one fewer obstacle. How can you tell when one becomes ready?

## Hint 3

Queue courses whose unmet prerequisite count is zero and append them as you remove them. If fewer than all courses come out, the rest are stuck in a cycle and the answer is empty.
