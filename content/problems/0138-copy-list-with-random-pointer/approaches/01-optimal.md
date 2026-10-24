## Idea

Make one pass to create a bare copy of each node and store it in a map from original to copy. Make a second pass to connect the copies: translate `cur.next` and `cur.random` through the map so they point to copies rather than originals. Return the copy of the original head.

## Why it works

After the first pass, every original node has exactly one copy. The second pass can therefore resolve any pointer, including backward and forward `random` jumps, in constant time. The map preserves identity, so two different originals never share a copy and `random = None` stays `None`.

## Edge cases

- Empty list: return `None`.
- One node: copy its value and leave both pointers `None` unless it points to itself.
- A node whose `random` is `None`: `copies.get(None)` returns `None`.
- A self-referential `random`: the map translates it to the copy itself.
- Several nodes pointing to the same random target: all copies point to that one copied target, matching the original structure.
