A subsequence is formed by deleting zero or more characters without changing the order of the remaining ones. It differs from a substring, which must be contiguous. Comparing two sequences usually uses a table whose entry records the best match for a pair of prefixes.

### Everyday examples

- **Two reading lists.** You and a friend each list books in the order you read them. The longest shared ordered list is a common subsequence: titles may be skipped, but neither list may be reordered.
- **Two DNA strands.** A biologist looks for the longest ordered pattern of bases present in both strands, allowing gaps where the strands differ.
- **Two edited drafts.** Unchanged sentences appear in the same order in both versions of a document; the longest such sequence measures how much structure the drafts still share.

### How it shows up here

Build a table indexed by prefixes of `text1` and `text2`. When the last characters of the two prefixes match, that pair can extend the answer for the prefixes without those characters. When they differ, at least one of the two last characters must be dropped, so take the better of the two smaller prefix pairs.
