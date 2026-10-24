Design a small social network. Users can post tweets, follow or unfollow other users, and request a news feed. A feed contains up to ten tweet ids: the user's own tweets plus tweets from people they follow, ordered newest first. Each new tweet receives a later position in time than every earlier tweet.

**Example**

```text
postTweet(1, 5)
follow(1, 2)
postTweet(2, 6)
getNewsFeed(1)  ->  [6, 5]
```

**Constraints, in plain words**

- User ids and tweet ids are positive integers up to 10,000.
- At most 30,000 operations are performed.
- A feed shows at most ten tweets.
- Newest-first ordering is determined by when tweets were posted.
- Following and unfollowing the same user repeatedly must behave predictably.

[Design Twitter on LeetCode](https://leetcode.com/problems/design-twitter/)
