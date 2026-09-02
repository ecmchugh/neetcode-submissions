class Twitter:

    def __init__(self):
        self.followers = defaultdict(set) #person who follows people : who they follow as a set
        self.queue = deque() #full timestamp of all tweets [userId, tweetId]
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.queue.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        counter = 0
        for i in range(len(self.queue) - 1, -1, -1):
            user = self.queue[i][0]
            tweet = self.queue[i][1]
            if counter > 9:
                return res
            if user == userId or (len(self.followers[userId]) > 0 and user in self.followers[userId]):
                res.append(tweet)
                counter += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
