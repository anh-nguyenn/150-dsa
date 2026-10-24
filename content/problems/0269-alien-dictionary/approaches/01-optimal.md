## Idea

Build a precedence graph over letters. For each adjacent pair of words, find the first position where they differ and add an edge from the earlier word's letter to the later word's letter. Also reject a pair where the longer word comes first but has the shorter word as a prefix. Then run Kahn's topological sort over all letters seen and return the order, or an empty string if not every letter can be placed.

## Why it works

Every observed word ordering imposes exactly one constraint: at the first difference, the earlier letter precedes the later one. Any valid alphabet must satisfy all such constraints, and any topological order does. Kahn's algorithm emits every vertex exactly when the precedence graph is acyclic, so a shorter result indicates a contradictory cycle. The prefix check catches the other possible contradiction, where sorted order would require a longer word to precede its own prefix.

## Edge cases

- A single word imposes no ordering, so a one-letter word returns that letter.
- Duplicate words reveal no new information.
- A cycle such as `z -> x -> z` makes the answer empty.
- A prefix conflict like `["abc", "ab"]` makes the answer empty.
- Letters that never appear should not be invented; only seen letters are included.
