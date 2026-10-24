## Idea

First record where each letter appears last. Sweep the string, extending the current part's endpoint to the last occurrence of every letter encountered. Whenever the scan reaches that endpoint, close the part, record its size, and begin again on the next character.

## Why it works

When the scan reaches `end`, every letter seen in the part has its final occurrence at or before `end`, so none of them appears in a later part. Thus cutting there is valid. Cutting earlier would leave some letter split across two parts. Because every valid part must contain at least the connected range of overlapping last occurrences, closing at the earliest safe point yields the maximum possible number of parts.

## Edge cases

- A one-character string produces one part of size one.
- A string where every letter is the same produces a single part containing the whole string.
- A string with all distinct letters produces one part per character.
- Repeated blocks of letters may still merge if a letter crosses a potential boundary.
- The empty string produces no parts; the loop simply returns an empty list.
- Non-adjacent occurrences of a letter force the part to span everything between them.
