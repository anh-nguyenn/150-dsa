## Hint 1

Which prefixes of the string can already be built completely from dictionary words?

## Hint 2

If the first `i` characters are buildable, then a dictionary word that starts at `i` can make a later prefix buildable.

## Hint 3

Sweep end positions left to right. For each dictionary word that ends there, check whether the position before it was reachable. Start with position zero marked reachable and return the mark for the full length.
