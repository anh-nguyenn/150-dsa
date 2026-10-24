Counting palindromes is a cousin of finding the longest one. Instead of keeping only the best span, you add one for every valid span you meet while growing outward from a centre.

### Everyday examples

- **Patterns in a tiled floor.** A strip of tiles may contain several mirror-symmetric runs; you count each run at its own position rather than remembering just the largest.
- **Repeated words in a sentence.** If the same short word appears in several places, each occurrence counts separately because position matters.

### How it shows up here

Use the same centres as the longest-palindrome problem. For each odd and even centre, expand while the characters match, and add one to the total for each successful expansion step. The sum over all centres is the number of palindromic substrings.
