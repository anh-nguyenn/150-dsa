Edit distance measures how far apart two sequences are by counting the cheapest series of small edits that transforms one into the other. The same idea appears in spell checkers, version control diffs, and comparing typed text with a reference. It is a canonical two-dimensional dynamic program because the cost of aligning prefixes builds directly on shorter prefixes.

### Everyday examples

- **Typing correction.** A phone suggests the nearest correctly spelled word by counting insertions, deletions, and substitutions from what you typed.
- **Document revisions.** A diff tool highlights inserted, removed, and changed words between two versions of a paragraph.
- **Comparing recordings.** A music app can align two performances of the same piece by allowing skipped or altered notes.

### How it shows up here

Let `dp[i][j]` be the minimum edits to turn the first `i` characters of the first word into the first `j` characters of the second. If the two current characters agree, no edit is needed at this position. Otherwise one operation is spent, followed by the cheapest of deleting, inserting, or replacing. Only the previous row and the current row are needed, so the table collapses to two rows; swapping the strings so the shorter one supplies the row width keeps memory modest.
