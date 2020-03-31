#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-31 18:33:09
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def checkSubarraySum(self, nums, k):
        if not nums:
            return False
        
        # define a prefix_sum  array to calculate the sum between two indexes
        prefix_sum = [0]*(len(nums)+1)
        
        for idx,val in enumerate(nums):
            prefix_sum[idx+1] = prefix_sum[idx] + val
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if k == 0:
                    if (prefix_sum[j+1] - prefix_sum[i]) == 0:
                        return True
                else:
                    if (prefix_sum[j+1] - prefix_sum[i]) % k == 0:
                        return True
        return False
