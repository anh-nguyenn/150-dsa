Koko has several piles of bananas and a deadline of `h` hours. Each hour she picks one pile and eats up to `k` bananas from it; a pile carries over to later hours if unfinished. Find the smallest integer `k` that lets her finish in time.

```text
piles = [3,6,7,11], h = 8  ->  4
piles = [30,11,23,4,20], h = 5  ->  30
```

**Constraints, in plain words**

- Between 1 and 10,000 piles.
- Each pile has between 1 and 10^9 bananas.
- The deadline is at least the number of piles and at most 10^9 hours.
- With `k` bananas per hour, finishing one pile takes `ceil(pile / k)` hours.

[Koko Eating Bananas on LeetCode](https://leetcode.com/problems/koko-eating-bananas/)
