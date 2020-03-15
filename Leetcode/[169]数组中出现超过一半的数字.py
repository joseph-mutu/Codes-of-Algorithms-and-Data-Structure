#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-13 09:27:23
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
        if len(nums) <= 2:
            
            return self.find_pivot(0,len(nums)-1,nums)
        middle = len(nums)//2
        index = self.partition(0,len(nums)-1,nums)
        while index != middle:
            print(index)
            if index < middle:
                index = self.partition(index,len(nums) - 1,nums)
            elif index > middle:
                index = self.partition(0,index,nums)
        return nums[index] 
                

    
    def partition(self,start,end,nums):
        # 返回主元所在的 index，index 左边数字小于他
        # index 右边数字大于他
        pivot = self.find_pivot(start,end,nums)
        print(start,end,pivot)
        left = start
        right = end

        while 1:
            while nums[left] < pivot:
                left += 1
            while nums[right] >= pivot and right >= 0:
                right -= 1
            if left < right:
                nums[left],nums[right] = nums[right],nums[left]
            else:
                break
        nums[left],nums[end-1] = nums[end-1],nums[left]
        return left 

    def find_pivot(self,start,end,nums):
        left = start
        right = end 
        mid = int((left + right)/2)
        if nums[left] > nums[mid]:
            nums[mid],nums[left] = nums[left],nums[mid]
        if nums[left] > nums[right]:
            nums[right],nums[left] = nums[left],nums[right]
        if nums[mid] > nums[right]:
            nums[mid],nums[right] = nums[right],nums[mid]
        # 将主元藏到最后一个元素减 1 的位置，因为最后一个元素肯定比他大
        nums[mid],nums[end-1] = nums[end-1],nums[mid]
        return nums[end-1]

s = Solution()
print(s.majorityElement([3,3,3,4]))