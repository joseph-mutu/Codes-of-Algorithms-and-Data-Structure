#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-12 08:40:21
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        if not nums:
            return -1
        k = len(nums) - k
        start,end = 0,len(nums)-1

        index = self.partition(start,end,nums)

        while index != k:

            if index  > k:
                end = index - 1
                index = self.partition(start,end,nums)
            elif index < k:
                start = index + 1
                index = self.partition(start,end,nums)
        return nums[index]            


    def partition(self,start,end,nums):

        p = self.median3(start,end,nums)

        l,r = start,end -1

        while 1:
            while nums[l] < p:
                l += 1
            while nums[r] > p:
                r -= 1
            if l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
            else:
                break

        nums[l],nums[end] = nums[end],nums[l]
        return l

    def median3(self,start,end,nums):

        mid = (start+end)//2
        if nums[start] > nums[mid]:
            nums[mid],nums[start] = nums[start],nums[mid]
        if nums[mid] > nums[end]:
            nums[mid],nums[end] = nums[end],nums[mid]
        if nums[start] > nums[mid]:
            nums[start],nums[mid] = nums[mid],nums[start]

        nums[mid],nums[end] = nums[end],nums[mid]
        return nums[end]

s = Solution()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6],4))