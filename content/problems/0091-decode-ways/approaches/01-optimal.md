## Idea

Walk through the string once while keeping the counts for the two previous prefix lengths. For each position, start a new count at zero, add the previous count when the current digit can stand alone, and add the count from two positions back when the current and previous digit form a legal letter.

## Why it works

Every complete decoding has exactly one final piece, either one digit or two. The two choices are disjoint, so adding their prefix counts counts each decoding once. Validity checks on the final piece prevent leading zeros and values above 26; the rolling update makes the memory constant.

## Edge cases

- A leading zero or a string like `"06"` has no decoding.
- `"0"` alone is invalid, while `"10"` and `"20"` each have one decoding.
- Runs of ones such as `"111"` branch into several splits; the recurrence handles them without special cases.
- A string that is entirely zeros returns zero.
- An empty string returns zero by the implementation, though the official constraints start at length one.
