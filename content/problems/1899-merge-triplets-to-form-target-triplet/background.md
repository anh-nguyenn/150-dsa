Merging by maximum is monotone: values can only stay the same or grow. That makes overshooting irreversible. Any piece that already exceeds the target in one coordinate can never appear in the final merged triplet, no matter what it is combined with. The useful pieces are the ones that fit underneath the target in every coordinate.

### Everyday examples

- **Mixing paint.** Each batch has intensity levels for three pigments, and mixing takes the strongest level of each. A batch that is already too strong in one pigment would ruin the target shade, so it must be left out.
- **Building a team score.** Three skill scores combine by taking the best result in each category. A candidate whose score is above the goal in any category cannot be part of a lineup meant to hit exactly that goal.

### How it shows up here

Ignore every triplet that has a coordinate larger than the target. Among the triplets that fit, merging all of them is harmless: each coordinate becomes the largest value seen there, which cannot exceed the target. The target is achievable exactly when every target coordinate appears in at least one fitting triplet. If all three coordinates are covered, merging the corresponding triplets produces the target.

Order does not matter, so one pass with three flags is enough.
