#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-19 14:53:27
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        length = [1] * len(nums)
        counts = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        counts[i] = counts[j]
                    elif length[j] + 1 == length[i]:
                        counts[i] += counts[j]
        longest = max(length)
        n_longest = sum(c for i,c in enumerate(counts) if length[i] == longest)        
        return n_longest

s = Solution()
print(s.findNumberOfLIS([1,3,5,4,7]))


