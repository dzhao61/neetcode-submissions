class Twitter:

    def __init__(self):
        self.userInfo = [[[0]*100, []] for _ in range(100)]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        loc = self.userInfo[userId][1]
        
        if len(loc) == 10:
            loc.pop(0)
        
        loc.append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.userInfo[userId][0]
        feed = []

        for i, flag in enumerate(following):
            if flag == 1 or i == userId:
                for tweet in self.userInfo[i][1]:
                    heapq.heappush(feed, tweet)
                while len(feed) > 10:
                    heapq.heappop(feed)
        res = []
        while feed:
            time, tweet = heapq.heappop(feed)
            res.append(tweet)
        return res[::-1]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userInfo[followerId][0][followeeId] = 1
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userInfo[followerId][0][followeeId] = 0
        
