#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-05 14:08:55
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or target < nums[0] or target > nums[-1]:
            return -1
        
        l,r = 0,len(nums)
        while l < r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
        return -1


