#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-31 16:45:51
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        # sliding window
        l,r = 0,0
        length = float('inf')
        tem_sum = 0

        while r < len(nums):
            tem_sum += nums[r]
            r += 1

            while tem_sum >= s:
                if r - l < length:
                    length = r - l
                tem_sum -= nums[l]
                l += 1
        return length
s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
