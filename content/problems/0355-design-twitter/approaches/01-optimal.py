import heapq


class Twitter:
    def __init__(self):
        self.clock = 0
        self.tweets: dict[int, list[tuple[int, int]]] = {}
        self.following: dict[int, set[int]] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.clock += 1
        self.tweets.setdefault(userId, []).append((self.clock, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        heap: list[tuple[int, int, int, int]] = []
        for author in self.following.get(userId, set()) | {userId}:
            posts = self.tweets.get(author)
            if posts:
                index = len(posts) - 1
                time, tweet = posts[index]
                heap.append((-time, tweet, author, index))
        heapq.heapify(heap)

        feed: list[int] = []
        while heap and len(feed) < 10:
            _, tweet, author, index = heapq.heappop(heap)
            feed.append(tweet)
            if index > 0:
                index -= 1
                time, older = self.tweets[author][index]
                heapq.heappush(heap, (-time, older, author, index))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following.get(followerId, set()).discard(followeeId)
