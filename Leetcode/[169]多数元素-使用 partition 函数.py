#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-13 13:25:39
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        middle = len(nums)//2
        index = self.partition(0,len(nums)-1,nums)
        start = 0
        end = len(nums) - 1
        while index != middle:
            print(index)
            if index < middle:
                start = index + 1
                index = self.partition(start,end,nums)
            elif index > middle:
                end = index - 1
                index = self.partition(start,end,nums)
        return nums[index]

    def partition(self,start,end,nums):
        # 返回主元所在的 index，index 左边数字小于他
        # index 右边数字大于他
        p = self.median3(start,end,nums)
        l = start
        r = end - 1

        small = start - 1
        for i in range(start,end):
            if nums[i] < p:
                small += 1
                if small != i:
                    nums[i],nums[small] = nums[small],nums[i]
        small += 1
        nums[small],nums[end] = nums[end],nums[small]
        return small

    def median3(self,start,end,nums):
        left = start
        right = end 
        mid = int((left + right)/2)
        if nums[left] > nums[mid]:
            nums[mid],nums[left] = nums[left],nums[mid]
        if nums[left] > nums[right]:
            nums[right],nums[left] = nums[left],nums[right]
        if nums[mid] > nums[right]:
            nums[mid],nums[right] = nums[right],nums[mid]
        return nums[end]
s = Solution()
print(s.majorityElement([1]))