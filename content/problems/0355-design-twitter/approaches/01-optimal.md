## Idea

Assign every tweet a strictly increasing timestamp and append `(timestamp, tweetId)` to its author's list. Keep each user's followees in a set.

To build a feed, start a max-heap with the newest tweet from the user and each followee. Pop the newest candidate, append it, then push that same author's previous tweet. Stop after ten tweets or when the heap empties.

## Why it works

Tweets from one author are stored in increasing timestamp order, so the last entry is that author's newest tweet. The heap always contains the newest not-yet-emitted tweet from each relevant author; therefore its maximum is the next newest tweet in the merged feed. Refilling from the popped author preserves the merge invariant.

## Edge cases

- A user with no tweets and no followees gets an empty feed.
- Unfollowing removes an author from future feeds without deleting their tweets.
- Following yourself must not duplicate your own tweets; the union of followees and the user handles this.
- A feed stops at ten entries even when more tweets are available.
- Posting the same tweet id more than once still produces separate timestamped events.
