## Idea

Represent each node as a dictionary of child characters. A special key marks the end of a stored word. Insertion follows or creates one child per character and marks the final node.

`search` follows the same route and then asks whether the final node is marked as a word. `startsWith` follows the route but does not require the marker.

## Why it works

Every path from the root spells exactly one prefix, so walking the characters of a query tests membership without comparing against every stored word. The terminal marker records complete words independently of their children, which is what separates `search` from `startsWith`.

## Edge cases

- If a query path is missing a child, both `search` and `startsWith` return false immediately.
- Inserting a word that is a prefix of another word marks an internal node, so both words remain searchable.
- Searching for a longer string than any stored word fails at the missing child.
- Lowercase letters never collide with the internal terminal marker.
- Reinserting a word is harmless and keeps the same marker.
