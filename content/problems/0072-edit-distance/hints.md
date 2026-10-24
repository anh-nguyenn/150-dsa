## Hint 1

Compare the two strings from the front. What are all the ways the last character of each prefix could be handled?

## Hint 2

Define the cost for prefixes `word1[:i]` and `word2[:j]`. Which smaller prefix pairs does each allowed operation lead to?

## Hint 3

Matching final characters cost nothing extra. Otherwise take one plus the minimum of the delete, insert, and replace options, and keep only the previous row of the table.
