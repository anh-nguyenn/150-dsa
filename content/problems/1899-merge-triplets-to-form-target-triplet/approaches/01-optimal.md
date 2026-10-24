## Idea

Discard triplets that exceed the target in any coordinate, because maximum merges cannot shrink them back. For the remaining triplets, record which target coordinates are matched. The target is formable exactly when all three coordinates are covered.

## Why it works

Any triplet with a coordinate above the target can never be part of a merge that equals the target, since that coordinate would remain too large. All remaining triplets are at most the target in every coordinate, so merging any number of them cannot overshoot. If each target coordinate appears somewhere among them, merging all such triplets produces exactly the target. If a coordinate never appears, no merge can manufacture it, so the target is impossible.

## Edge cases

- A single triplet equal to the target succeeds immediately.
- A triplet that exceeds the target in only one coordinate is still unusable.
- If one target coordinate never appears among usable triplets, the answer is false.
- Duplicate triplets do not change the result.
- Merging extra usable triplets is safe because all their values are bounded by the target.
- Order of merging is irrelevant.
