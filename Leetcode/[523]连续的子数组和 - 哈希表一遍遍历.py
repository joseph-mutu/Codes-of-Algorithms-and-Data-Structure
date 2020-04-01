#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-31 18:37:18
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def checkSubarraySum(self, nums, k):
        if not nums:
            return False

        if k == 0:
            for i in range(1,len(nums)):
                if nums[i] == 0 and nums[i-1] == 0:
                    return True
            return False

        bucket = {0:-1}

        tem_sum = 0
        for idx,num in enumerate(nums):
            tem_sum += num
            bucket_num = tem_sum %k
            if bucket.get(bucket_num) is not None:
                if idx - bucket.get(bucket_num) >= 1:
                    return True
            else:
                bucket[bucket_num] = idx
        return False

s = Solution()
print(s.checkSubarraySum([0,1,0],k=0)) 
