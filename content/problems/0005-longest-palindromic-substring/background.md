A palindrome mirrors around its middle. That middle is either a single character (odd length) or the gap between two characters (even length). Growing outward from a middle is a natural way to test symmetry without rechecking the whole substring.

### Everyday examples

- **Mirror writing.** Words such as "level" or "noon" look the same when reversed; the centre is the anchor and the letters match outward.
- **A symmetrical seating row.** A row of chairs is symmetric about the aisle. Checking symmetry means comparing pairs moving away from the aisle, not starting at the ends.

### How it shows up here

Every palindromic substring has exactly one centre. For each of the `2n - 1` centres, expand while the two sides match, and remember the longest span seen. This examines every palindrome without storing a table of all substrings.
