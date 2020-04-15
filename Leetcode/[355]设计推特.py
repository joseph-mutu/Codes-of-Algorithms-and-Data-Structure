#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-13 06:39:20
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
class ListNode:
    def __init__(self,val,time):
        self.val = val
        self.time = time
        self.next = None

class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        #存储每个用户自己的链表节点
        self.users = collections.defaultdict(list)
        self.time = 1
        #存储每个用户都订阅了谁
        self.following = collections.defaultdict(list)
        self.length = collections.defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId in self.users:
            node = ListNode(tweetId,self.time)
            self.length[userId] += 1

            record = self.users[userId].next
            self.users[userId].next = node
            node.next = record

            # 如果发文数超过 10，则删除最后一个
            if self.length[userId] > 10:
                head = self.users[userId]
                while head.next.next:
                    head = head.next
                head.next = None

        else:
            # 如果该用户不存在，则新创立一个
            self.create_Id(userId)
            head = self.users[userId]
            node = ListNode(tweetId,self.time)
            head.next = node

        self.time += 1

    def create_Id(self,userId):
        head = ListNode(0,-1)
        self.following[userId].append(userId)
        self.length[userId] = 1
        self.users[userId] = head
        return 

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """

        def merge_mul(l,r,lists):
            # print(l,r)
            if l == r:
                return self.get_node_list(self.users[lists[l]])

            mid = (l + r) //2

            list1 = merge_mul(l,mid,lists)
            list2 = merge_mul(mid+1,r,lists)

            return merge_two(list1,list2,1,[])

        def merge_two(list1,list2,length,nodes):
            if length > 10:
                return nodes
            if not list1:
                nodes.extend(list2[:])
                return nodes
            if not list2:
                nodes.extend(list1[:])
                return nodes

            if list1[0][0] > list2[0][0]:
                nodes.append(list1[0])
                nodes = merge_two(list1[1:],list2,length+1,nodes)
                return nodes
            else:
                nodes.append(list2[0])
                nodes = merge_two(list1,list2[1:],length+1,nodes)
                return nodes



        nodes = []
        if len(self.following[userId]) == 1:
            head = self.users[userId]
            head = head.next
            while head:
                nodes.append(head.val)
                head = head.next
        elif len(self.following[userId]) > 1:
            #如果存在 followers，则需要合并多个链表
            nodes = merge_mul(0,len(self.following[userId])-1,self.following[userId])

            for idx,lists in enumerate(nodes):
                nodes[idx] = lists[1]
        return nodes[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.users:
            self.create_Id(followerId)
        if followeeId not in self.users:
            self.create_Id(followeeId)

        if followerId != followeeId and followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)
        return

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.users and followeeId in self.following[followerId] and followerId != followeeId:
            
            self.following[followerId].remove(followeeId)

        return 

    def get_node_list(self, head):
        nodes = []
        head = head.next
        while head:
            nodes.append([head.time,head.val])
            head = head.next
        return nodes

# ["Twitter","postTweet","postTweet","postTweet","postTweet",
# "postTweet","postTweet","postTweet","postTweet","postTweet",
# "postTweet","postTweet","postTweet",
# "postTweet","postTweet",
# "follow","follow","follow","follow",
# "follow","follow","follow","follow","follow","follow","follow",
# "follow","getNewsFeed","getNewsFeed","getNewsFeed","getNewsFeed","getNewsFeed"]
# [[],[1,6765],[5,671],[3,2868],[4,8148],[4,386],
# [3,6673],[3,7946],[3,1445],[4,4822],[1,3781],[4,9038],
# [1,9643],[3,5917],[2,8847],[1,3],[1,4],[4,2],[4,1],[3,2],
# [3,5],[3,1],[2,3],[2,1],[2,5],[5,1],[5,2],

# [1],[2],[3],[4],[5]]

t = Twitter()
t.postTweet(1,6765)
t.postTweet(5,671)
t.postTweet(3,2868)
t.postTweet(4,8148)
t.postTweet(4,386)
t.postTweet(3,6673)
t.postTweet(3,7946)
t.postTweet(3,1445)
t.postTweet(4,4822)
t.postTweet(1,3781)
t.postTweet(4,9038)
t.postTweet(1,9643)
t.postTweet(3,5917)
t.postTweet(2,8847)

t.follow(1,3)
t.follow(1,4)
t.follow(4,2)
t.follow(4,1)
t.follow(3,2)
t.follow(3,5)
t.follow(3,1)
t.follow(2,3)
t.follow(2,1)
t.follow(2,5)
t.follow(5,1)
t.follow(5,2)

print(t.following)
print(t.getNewsFeed(1))
print(t.getNewsFeed(2))



