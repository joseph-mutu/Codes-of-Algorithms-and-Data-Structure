#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-08 09:27:35
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def maxCoins(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        memo = {}
        return self.backtrack(nums,memo)

    def backtrack(self,nums,memo):
        if not nums:
            return 0
        print(nums)
        if tuple(nums) in memo:
            print('ere')
            return memo[tuple(nums)]

        res = float('-inf')
        for i,num in enumerate(nums):
            tem_gain = nums[i]
            if i != 0:
                tem_gain *= nums[i-1]
            if i != len(nums) -1:
                tem_gain *= nums[i+1]
            stat = nums[:i] + nums[i+1:]
            cmp_gain = tem_gain + self.backtrack(stat,memo)
            res = max(cmp_gain,res)

        memo[tuple(nums)] = res
        return res

s = Solution()
print(s.maxCoins([8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2]))
