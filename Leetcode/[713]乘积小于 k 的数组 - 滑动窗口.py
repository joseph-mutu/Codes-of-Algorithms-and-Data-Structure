#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-01 14:24:00
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import math
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if not nums:
            return 0

        l,r = 0,0
        k = math.log(k) if k > 0 else 0

        tem_sum = 0
        results = 0
        while r < len(nums):
            tem_sum += math.log(nums[r])
            r += 1

            while tem_sum >= k - 1e-9 and l < r:
                tem_sum -= math.log(nums[l])
                l += 1

            results += r - l
            print(l,r,results)

        return results

s = Solution()
print(s.numSubarrayProductLessThanK([1,2,3],0))

