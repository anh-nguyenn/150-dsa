## Idea

Choose the end of the next piece from the current start. Keep the piece only when it is a palindrome, recurse on the remaining suffix, and undo the choice before trying a later end.

## Why it works

Every partition is determined by a sequence of increasing cut positions. The recursion considers every possible next cut, so it covers every sequence. Accepting only palindromic pieces enforces the rule at the moment a piece is created, and stopping exactly at the string's end guarantees the pieces cover the whole string with no gaps or overlaps.

## Edge cases

- A one-character string has exactly one partition, the string itself.
- A string of identical characters has many partitions, including all single characters and the whole string.
- A string with no palindromic proper prefixes still has at least the one-character partition.
- An empty string returns `[[]]` under the same base-case logic, though the official input is non-empty.
