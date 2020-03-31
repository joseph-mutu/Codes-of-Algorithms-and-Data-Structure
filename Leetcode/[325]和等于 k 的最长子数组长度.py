#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-30 16:21:00
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
    def maxSubArrayLen(self, nums, k):
        if not nums:
            return 0

        prefix_sum = {}
        prefix_sum[0] = 0

        tem_sum = 0
        length = 0
        for i in range(len(nums)):
            tem_sum += nums[i]
            target = tem_sum - k

            if target in prefix_sum:
                length = max(length,i+1 - prefix_sum[target])

            if tem_sum not in prefix_sum:
                prefix_sum[tem_sum] = i + 1

        return length


s = Solution()
print(s.maxSubArrayLen( [-2, -1, 2, 1],1))
