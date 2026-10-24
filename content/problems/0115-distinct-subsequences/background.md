Counting subsequences is about choices: for each character of the source you either use it or skip it. If two different sets of choices produce the same target, they are counted separately, so the problem asks for the number of paths through those choices, not for the number of distinct resulting strings. This is a classic counting dynamic program.

### Everyday examples

- **Forming a word from letter tiles.** You have a row of tiles and want to spell a shorter word while keeping the tiles in order. Different selections of tiles are different attempts, even when they spell the same word.
- **Picking courses in order.** From a list of course slots, you choose a sequence that satisfies a requirement. Choosing Monday's slot versus Wednesday's slot for the same topic gives two different schedules.
- **DNA matching.** A short genetic pattern may appear as a subsequence of a longer strand in several position combinations.

### How it shows up here

Walk through `s` one character at a time. Maintain how many ways each prefix of `t` can currently be formed. When the current character of `s` matches a character of `t`, it can extend every way of forming the prefix before that character. Processing the target indices backwards prevents the current character from being reused twice in one step. The table shrinks from two dimensions to one row.
