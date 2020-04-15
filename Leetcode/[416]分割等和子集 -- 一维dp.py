#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-14 07:30:57
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

        dp = [False] *(target + 1)
        dp[0] = True

        pos = 0

        for num in nums:
            for i in range(target,-1,-1):
                if i < num:
                    continue
                else:
                    dp[i] = dp[i] or dp[i-num]
        return dp[-1]

s = Solution()
print(s.canPartition([1, 5, 11, 5]))