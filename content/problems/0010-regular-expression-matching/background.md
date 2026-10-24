Pattern matching with repetition is a small language-recognition problem. A star makes the pattern able to consume an arbitrary run of one kind of character, so a greedy left-to-right scan is not enough; the matcher sometimes needs to reconsider how much a star consumed. Dynamic programming handles that by recording, for each prefix pair, whether a match is possible.

### Everyday examples

- **File name wildcards.** A shell pattern such as `ab*` matches any file name beginning with `ab`, where the star stands for a run of characters.
- **Form validation.** A rule like `a*` accepts the empty string, `a`, `aa`, and so on, and a validator must decide membership rather than search for a prefix.
- **Text search with repetition.** A search tool may treat `.*` as "anything at all" and combine it with literals around it.

### How it shows up here

Let `dp[i][j]` mean that the first `i` characters of the input match the first `j` characters of the pattern. A literal or dot advances both prefixes together. A star can either eliminate itself and its preceding character, which skips two pattern positions, or, when the preceding character matches the current input character, consume one more input character while keeping the star available. Filling the table from empty prefixes outward answers every combination without backtracking.
