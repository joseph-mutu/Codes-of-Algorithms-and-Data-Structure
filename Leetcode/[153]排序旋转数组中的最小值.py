#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-03 06:45:58
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def findMin(self, nums):
        if not nums:
            return None
        if nums[0] <= nums[-1]:
            return nums[0]

        start = 0
        end = len(nums) - 1

        while end - start > 1:
            
            mid = int( (end +start) / 2)
            if nums[mid] <= nums[end]:
                # 当前 mid 值在没有旋转的一边:
                end = mid
            elif nums[mid] > nums[end]:
                # 当前 mid 值在旋转的数组一边
                start = mid
        return nums[end]

s = Solution()
print(s.findMin([4,5,6,7,0,1,2]))