## Idea

Build a table whose rows are prefixes of the input and whose columns are prefixes of the pattern. Seed the empty-input row so that star pairs can vanish. Then fill each cell using either the diagonal for a direct character match, or the two star rules: skip the pair, or absorb one input character.

## Why it works

Every valid match ends in one of a few local ways. If the last pattern token is a literal or dot, it must pair with the last input character, so the rest is the diagonal subproblem. If the last token is a star, either the star and its character match nothing, leaving the cell two columns left, or the star's character matches the current last input character and the star stays available, leaving the cell above. These cases cover all possibilities, and the base row correctly handles patterns that can match the empty string.

## Edge cases

- Empty input and empty pattern match.
- An empty input matches a pattern made only of character-star pairs such as `a*` or `a*b*`.
- An empty input does not match a pattern containing a literal or a dot.
- A star always has a preceding character, so the pattern is well formed.
- A trailing star may consume zero characters, which the skip-two rule handles.
- A dot inside a star, as in `.*`, can absorb any run of input characters.
