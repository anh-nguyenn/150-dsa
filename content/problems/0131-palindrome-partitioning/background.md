A partition is a set of cut positions that divides a sequence into consecutive pieces. Backtracking can choose the next cut, keep the prefix if it satisfies the rule, and then solve the remaining suffix in the same way.

### Everyday examples

- **Cutting a ribbon.** You make cuts from left to right. Each piece must be a usable length, and the pieces together must use the whole ribbon without gaps or overlaps.
- **Splitting a sentence.** You break a sentence into phrases at chosen spaces. The phrases keep their original order, and every word must belong to exactly one phrase.

### How it shows up here

The search starts at the beginning of the string. It tries every possible end position for the next piece. If the substring from the start to that end reads the same forwards and backwards, it is a valid next piece, so the search appends it and continues from the end position. When the start reaches the end of the string, the current list of pieces is a complete partition.

Trying end positions in increasing order produces the pieces in their original left-to-right order. Since any cut is allowed as long as the piece is a palindrome, this explores exactly all valid partitions.
