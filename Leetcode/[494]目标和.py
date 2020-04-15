#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-14 17:40:13
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

from typing import List
#使用回溯
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        t_sum = sum(nums)
        if S < -t_sum or S > t_sum:
            return 0
        length = t_sum * 2 + 1
        dp = [[0 for _ in range(length)] for _ in range(len(nums))]
        #初始化第一行
        if nums[0] == 0:
            dp[0][0+t_sum] = 2
        else:
            dp[0][nums[0]+t_sum] = 1
            dp[0][-nums[0]+t_sum] = 1

        for i in range(1,len(nums)):
            for j in range(length):
                if j - nums[i] >= 0:
                    dp[i][j] += dp[i-1][j-nums[i]]
                if j + nums[i] < length:
                    dp[i][j] += dp[i-1][j+nums[i]]
        return dp[len(nums)-1][S+t_sum]

s = Solution()
print(s.findTargetSumWays([0,0,0,0,0,0,0,0,1],1))
[[0, 1, 0], 
 [0, 2, 0], 
 [0, 4, 0], 
 [0, 8, 0], 
 [0, 16, 0], 
 [0, 32, 0], 
 [0, 64, 0], 
 [0, 128, 0], 
 [128, 0, 128]]

