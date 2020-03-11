#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-11 17:51:43
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

        if not k or k <= 0:
            return nums
        length = len(nums)
        k = k%length if k > len(nums) else k
        nums = self.swap(0,length - 1,nums)
        print(nums)
        nums = self.swap(0,k-1,nums)
        print(nums)
        nums = self.swap(k,length-1,nums)



    def swap(self,pos1,pos2,nums):
        """
        reverse the list from pos1 to pos2
        """

        left,right = pos1,pos2

        while left < right and left >= 0 and right <= len(nums):
            tem = nums[left]
            nums[left] = nums[right]
            nums[right] = tem
            right -= 1
            left += 1
        return nums