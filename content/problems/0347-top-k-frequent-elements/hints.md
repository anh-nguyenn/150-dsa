## Hint 1

What two pieces of information do you need for each distinct value? Can you build a frequency table in one pass?

## Hint 2

Once you have the counts, you need the largest frequencies rather than a full ordering. What is the largest possible frequency, and can that range be used directly?

## Hint 3

Create buckets indexed by count, place each value in the bucket for how often it appears, then scan buckets from highest to lowest until you have k values.
