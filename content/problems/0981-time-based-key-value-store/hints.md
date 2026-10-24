## Hint 1

For one key, how are its stored timestamps ordered, and what does that let you do instead of scanning them?

## Hint 2

When searching for the largest timestamp at or below the query, what should you remember whenever you see a valid candidate?

## Hint 3

Store a growing list of timestamp-value pairs per key. Binary search for the rightmost timestamp not greater than the query, and return an empty string if none qualifies.
