#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-13 09:09:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$


class Twitter:

    class Node:
        def __init__(self):
            self.twit = []
            self.followee = set()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 1
        self.twit_time = {}
        self.users = {}

        self.max_len = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.users:
            self.users[userId] = Twitter.Node()
        self.users[userId].twit.append(tweetId)

        self.twit_time[tweetId] = self.time
        self.time += 1
        

    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId in self.users:
            ans = self.users[userId].twit[-10:][::-1]
            for followee in self.users[userId].followee:
                if followee in self.users:

                    candidate = self.users[followee].twit[-10:][::-1]

                    pos1,pos2,res = 0,0,[]

                    while pos1 < len(ans) and pos2 < len(candidate):
                        if self.twit_time[ans[pos1]] > self.twit_time[candidate[pos2]]:
                            res.append(ans[pos1])
                            pos1 += 1
                        else:
                            res.append(candidate[pos2])
                            pos2 += 1
                    if pos2 < len(candidate):
                        res.extend(candidate[pos2:])
                    elif pos1 < len(ans):
                        res.extend(ans[pos1:])
                    ans = res[:10]
            return ans
        return []

        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId not in self.users:
                self.users[followerId] = Twitter.Node()
            self.users[followerId].followee.add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId in self.users and  followeeId in self.users[followerId].followee:
                self.users[followerId].followee.remove(followeeId)

