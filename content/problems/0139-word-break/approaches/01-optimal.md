## Idea

Keep a boolean array `reachable` whose entry at index `i` says whether the first `i` characters can be segmented. Mark zero true. For each end position, try every dictionary word that could end there; if the word matches and the position before it is reachable, mark the end reachable. The answer is the final entry.

## Why it works

Any valid split of a prefix ends with some dictionary word. Removing that last word leaves a valid split of an earlier prefix. Conversely, appending a matching word to any reachable prefix produces a valid split. The DP checks both directions of this relationship, so it marks exactly the reachable positions.

## Edge cases

- A one-character string is decided by whether that character is in the dictionary.
- A word longer than the string is never considered.
- Reusing words is allowed, so repeated characters such as `"aaaa"` can be built from a repeated shorter word.
- A dictionary containing several words that share prefixes does not cause false positives because each match is checked independently.
- An empty string is treated as already segmented, returning true, although the official constraints start at length one.
