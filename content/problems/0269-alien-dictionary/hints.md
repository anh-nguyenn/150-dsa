## Hint 1

Comparing two adjacent sorted words reveals at most one useful fact. Which pair of letters is it?

## Hint 2

Collect those facts as directed edges. What does a cycle in that graph mean, and what does a prefix conflict mean?

## Hint 3

Run a topological sort that starts with letters having no incoming edge. If the result does not include every letter, the words are inconsistent.
