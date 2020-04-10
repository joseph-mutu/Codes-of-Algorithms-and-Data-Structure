#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 17:08:29
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$


from heapq import heapify,heappop
class Solution(object):
    def __init__(self):
        self.count = 0
    def reversePairs(self, nums):

        # 用最小堆做离散化
        nums_2times = list(set(term*2+0.5 for term in nums))
        nums_2times += list(set(nums))
        heapify(nums_2times)

        rank = 1
        pos = {}
        while nums_2times:
            pos[heappop(nums_2times)] = rank
            rank += 1
        self.build_tree(pos)
        for i in range(len(nums)-1,-1,-1):
            #do the query
            self.count += self.query(pos[nums[i]])
            # update its value by 2 times
            self.update(pos[nums[i]*2+0.5],1)
        return self.count
    
    def build_tree(self,pos):
        self.tree = [0] * (len(pos)+1)
    
    def update(self,idx,val):
        pos = idx
        while pos < len(self.tree):
            self.tree[pos] += val
            pos += self.low_bit(pos)

    def query(self,idx):
        pos = idx
        tem_sum = 0
        while pos > 0:
            tem_sum += self.tree[pos]
            pos -= self.low_bit(pos)
        return tem_sum

    def low_bit(self,x):
        return x & -x

s = Solution()
print(s.reversePairs([-5,-5]))



