This is a reachability question. Instead of trying every possible split, mark which prefixes of the string can be formed from dictionary words, then extend those positions.

### Everyday examples

- **Run-on text.** A sentence written without spaces can be checked against a known vocabulary to see whether it divides into real words.
- **Product codes.** A long receipt code can be validated by splitting it into registered code fragments.
- **Route labels.** A domain-like string can be decomposed into known labels, where each label must match exactly.

### How it shows up here

Position zero is reachable before reading anything. If position `i` is reachable and a dictionary word matches the next block of characters, the position after that block becomes reachable too. The answer is whether the final position is reachable. Trying longer blocks from each reachable position explores exactly the legal splits without enumerating them all.
