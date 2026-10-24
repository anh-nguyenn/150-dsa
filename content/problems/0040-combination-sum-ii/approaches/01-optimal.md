## Idea

Sort the candidates, then search combinations from left to right. A chosen position advances the next start by one, so no position is reused. At each level, ignore a value equal to the previous value because the first copy already explored every combination that can start with that value.

## Why it works

Sorting groups equal values, so the duplicate check only needs to compare neighbors. Skipping later equal copies at the same recursion depth removes identical branches without removing combinations that use several copies, because those copies are chosen at deeper levels. Advancing the start index guarantees each input position contributes at most once.

## Edge cases

- An empty result is returned when no subset reaches the target.
- A single candidate equal to the target gives one one-element combination.
- Two equal candidates can both be used, as in `[1, 1]` for target 2.
- Duplicate input values never cause duplicate output combinations.
- Candidates larger than the remaining target end the loop after sorting.
