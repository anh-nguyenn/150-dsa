## Idea

Scan the sorted intervals once. First copy every interval that ends strictly before the new interval begins, since those cannot overlap it. Then absorb every interval that starts at or before the running end of the new interval, widening the running start and end as needed. Append the merged interval and finally copy the untouched remainder.

## Why it works

Before the first phase, all remaining intervals end at or after the new start, so no copied interval can overlap. During the second phase, every interval that could touch the growing block starts no later than its current end and is therefore merged. Once an interval starts beyond the block's end, sorted order guarantees that it and everything after it are disjoint from the block. The three phases thus produce exactly the merged union in sorted order.

## Edge cases

- An empty interval list simply returns the new interval.
- The new interval may sit entirely before or after every existing interval.
- Touching endpoints, such as `[1,2]` and `[2,5]`, merge into `[1,5]`.
- One new interval can swallow many existing intervals at once.
