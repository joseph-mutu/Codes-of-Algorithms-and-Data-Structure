#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-11 18:27:53
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 使用额外的数组进行循环
        if not k or k <=0:
            return nums
        else:
            tem_nums = [0]*len(nums)
            k = k%len(nums) if k >= len(nums) else k
            for i in range(len(nums)):
                tem_nums[(i+k)%len(nums)] = nums[i]
            for i in range(len(nums)):
                nums[i] = tem_nums[i]
