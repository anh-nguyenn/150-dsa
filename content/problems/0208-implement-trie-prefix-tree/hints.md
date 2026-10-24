## Hint 1

How can words that share a beginning reuse the same work instead of being stored as separate strings?

## Hint 2

If a node represents one character, how would you distinguish reaching the end of a stored word from merely reaching the end of a prefix?

## Hint 3

Store child links in a map and a boolean end marker. Insertion creates the path and sets the marker; `search` checks the marker, while `startsWith` only requires the path to exist.
