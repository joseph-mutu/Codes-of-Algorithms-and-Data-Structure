#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-07 20:10:50
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # use dp
        fin_max,cur_max,cur_min = float('-inf'),nums[0],nums[0]
        for i in range(1,len(nums)):
            if nums[i] < 0:
                cur_max,cur_min = cur_min,cur_max
            cur_max = max(cur_max * nums[i],nums[i])
            cur_min = min(cur_min * nums[i],nums[i])
            fin_max = max(cur_max,fin_max)
        return fin_max

s = Solution()
print(s.maxProduct([-2,0,-1]))