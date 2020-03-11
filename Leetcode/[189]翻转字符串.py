#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-11 17:21:04
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
        if k <= 0:
            return nums
        
        while k > 0:
            record = nums[-1]
            for i in range(len(nums)-2,-1,-1):
                nums[i+1] = nums[i]
            nums[0] = record
            k -= 1
        


