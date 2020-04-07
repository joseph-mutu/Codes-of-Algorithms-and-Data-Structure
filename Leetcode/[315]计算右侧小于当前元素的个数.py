#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-07 06:43:44
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

from heapq import heappush,heappop,heapify
class Solution(object):
    def countSmaller(self, nums):
        if not nums:
            return []
        ans = [-1] * len(nums)

        nums_rank = nums[:]
        heapify(nums_rank)
        rank_arr = {}
        

        length = len(nums)

        rank = 1
        while nums_rank:
            rank_arr[heappop(nums_rank)] = rank
            rank += 1

        query_nums = [0] * (length+1)
        for i in range(len(nums)-1,-1,-1):
            self.update(rank_arr[nums[i]],length,query_nums)
            ans[i] = self.query(rank_arr[nums[i]] - 1,query_nums)

        return ans


    # 使用树状数组
    def update(self,index,length,nums):
        while index < length + 1:
            nums[index] += 1
            index += self.low_bit(index)

    def query(self,index,nums):
        res = 0
        while index  > 0:
            res += nums[index]
            index -= self.low_bit(index)
        return res

    def low_bit(self,x):
        return x & -x

s = Solution()
print(s.countSmaller([5,2,6,1]))