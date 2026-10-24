## Hint 1

How can you tell which of two tweets is newer when they come from different users? What extra value could you record at post time?

## Hint 2

Once each followed user's tweets are in chronological order, how do you merge only the newest few without scanning all of them?

## Hint 3

Keep per-user tweet lists in posting order and a global counter. For a feed, seed a max-heap with each relevant user's latest tweet, then pop and refill from the same user's older tweets until you have ten.
