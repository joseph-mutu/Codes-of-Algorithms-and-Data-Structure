#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-07 18:40:54
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 0:
            return nums[0]
        return max(self.dp(nums[:len(nums)-1]),self.dp(nums[1:]))
    
    def dp(self,nums):
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp_1 = nums[0]
        dp_2 =  0
        dp = 0
        for i in range(1,n):
            dp = max(dp_1,nums[i]+dp_2)
            dp_2 = dp_1
            dp_1 = dp

        return dp


s = Solution()
print(s.rob([1,1]))