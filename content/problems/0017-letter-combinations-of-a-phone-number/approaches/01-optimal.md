## Idea

Walk through the digits from left to right. For each digit, try every letter it maps to, append that letter to the current string, and recurse on the next digit. When all digits have been processed, add the completed string.

## Why it works

Every result is a choice of one letter per digit, made in digit order. The recursion tries all choices at each position, so it reaches every such sequence exactly once. The path length grows by one for each digit, so a string is complete exactly when the digit index reaches the end.

## Edge cases

- An empty digit string returns `[]`, since there is no meaningful letter combination.
- A single digit returns its individual letters.
- Digits 7 and 9 contribute four letters each, while the others contribute three.
- All groups are non-empty, so every partial path can be completed.
