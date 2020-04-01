#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-01 11:15:10
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if not nums:
            return 0

        #construct the prefix pro array
        prefix_pro = [1] * ( len(nums) +1 )

        results = []
        for idx,num in enumerate(nums):
            prefix_pro[idx+1] = prefix_pro[idx] * num
            for j in range(idx+1):
                if prefix_pro[idx + 1] / prefix_pro[j] < k:
                    results.append(nums[j:idx+1])
        return len(results)

s = Solution()
print(s.numSubarrayProductLessThanK([10,5,2,6],100))