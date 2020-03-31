#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-30 20:04:18
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def findMaxLength(self, nums):
        # 使用滑动窗口
        if not nums:
            return 0
        length = 0
        # meets 0 ,count subtracts 1;meets 1, count adds one
        count = 0
        record = {0:-1}
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count not in record:
                record[count] = i

            elif count in record:
                length = max(length,i - record[count])
        return length

s = Solution()
print(s.findMaxLength([0,0,0,0,1,1,1,0]))
