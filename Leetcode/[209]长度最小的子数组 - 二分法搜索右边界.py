#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-31 17:27:15
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        # 使用前缀和可以求解任意区间内的加和问题

        prefix_sum = [0]*(len(nums)+1)

        length = float('inf')

        for idx,val in enumerate(nums):
            prefix_sum[idx+1] = prefix_sum[idx] + val

        for i in range(len(nums)):
            l,r = i,len(nums)

            while l < r:
                mid = (l+r)//2
                if prefix_sum[mid+1] - prefix_sum[i] < s:
                    l = mid + 1
                else:
                    r = mid
                print("start:",i,"left:",l,"mid:",mid,prefix_sum[mid+1] - prefix_sum[l])
            print(r)
            if r != len(nums):
                length = min(length,r - i + 1)
        if length == float('inf'):
            return 0
        return length
s = Solution()
print(s.minSubArrayLen(11,[1,2,3,4,5]))

