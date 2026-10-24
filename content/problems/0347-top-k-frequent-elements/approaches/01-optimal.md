## Idea

Count how often each value occurs, then place each value into a bucket indexed by its count. Walk the buckets from the largest count down to the smallest and stop once `k` values have been collected.

## Why it works

A value with a larger count always sits in a higher-numbered bucket, so scanning buckets from high to low visits values in non-increasing frequency order. No value can have a count greater than the list length, which is why that many buckets is enough. The uniqueness guarantee means the first `k` values collected are the required answer, regardless of order within a bucket.

## Edge cases

- When `k` is 1, only the single most frequent value is returned.
- When `k` equals the number of distinct values, every value is returned.
- Negative and zero values work normally because they are dictionary keys.
- If all values are identical, the only bucket used is the one for the full length.
- If all values are distinct, `k` must be handled from the size-1 buckets without assuming an order among ties.
