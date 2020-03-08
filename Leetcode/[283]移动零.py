#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-07 14:23:15
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):
    def moveZeroes(self, nums):
        if not nums:
            return []
        # zero 负责指向第一个为零的数
        # right 负责找到不为零的数进行交换
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i],nums[pos] = nums[pos],nums[i]
                pos += 1
        return nums


s = Solution()
print(s.moveZeroes([1,0]))




