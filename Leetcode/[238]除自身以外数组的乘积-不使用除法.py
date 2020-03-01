#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-01 08:21:00
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def productExceptSelf(self, nums):
        if not nums:
            return []

        product_except_self = [0] * len(nums)

        # 首先构建左数组乘积
        product_except_self[0] = 1
        for i in range(1,len(nums)):
            product_except_self[i] = product_except_self[i-1] * nums[i-1]
        # 构建右数组乘积
        R = 1
        for i in range(len(nums) - 1,-1,-1):
            product_except_self[i] = R * product_except_self[i]
            R *= nums[i]

        return product_except_self

s = Solution()
print(s.productExceptSelf([0,1,2,0,4]))


