#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-13 22:02:26
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) <= 1:
            return False
        
        total = sum(nums)
        target = total/2
        if not target.is_integer():
            return False
        target = int(target)
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = True
        
        for i in range(1,len(nums)+1):
            for j in range(1,target+1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        print(dp)
        return dp[len(nums)][target]
        


s = Solution()
print(s.canPartition([1, 5, 11, 5]))
[[True, False, False, False, False, False, False, False, False, False, False, False], 
 [True, True, False, False, False, False, False, False, False, False, False, False], 
 [True, True, False, False, False, True, True, False, False, False, False, False], 
 [True, True, False, False, False, True, True, False, False, False, False, True], 
 [True, True, False, False, False, True, True, False, False, False, True, True]]