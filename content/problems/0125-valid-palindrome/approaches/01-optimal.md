## Idea

Keep a pointer at each end. Skip characters that are not letters or digits, compare the remaining characters in lowercase, then step both pointers inward.

## Why it works

Every comparison checks the outermost unmatched pair of the cleaned string. Skipping punctuation does not change which letters must mirror which. If all pairs match until the pointers meet or cross, the cleaned string is a palindrome; a mismatch proves it is not.

## Edge cases

Strings made only of punctuation or spaces clean to empty and return true. Single characters and case differences such as `"Aa"` are handled by the lowercase comparison. Digits count as alphanumeric, so `"0P"` compares `"0"` with `"p"` and returns false.
