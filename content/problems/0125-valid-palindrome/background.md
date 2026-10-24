A two-pointer scan compares a sequence from both ends at the same time. Instead of building a cleaned-up copy, the pointers move inward and simply step over anything that should be ignored.

### Everyday examples

- **Reading a sign.** You check whether a phrase is symmetric by looking at the first and last letters, then the second and second-to-last, and so on.
- **Checking a mirror.** If two people face a mirror from opposite edges, they only need to compare the nearest unmatched pair before moving closer.

### How it shows up here

One pointer starts at the beginning and one at the end. Each pointer advances past spaces, punctuation, and other non-alphanumeric characters. The surviving characters are compared in lowercase. If any pair differs, the answer is immediately false; if the pointers meet or cross, every pair matched and the string is a palindrome. This avoids allocating a filtered string.
