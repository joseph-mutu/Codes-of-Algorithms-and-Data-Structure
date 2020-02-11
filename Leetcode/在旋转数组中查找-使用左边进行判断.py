#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-11 06:51:38
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution():
    def search(self, nums, target):
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1


        while left <= right:
            mid = int((left + right)/2)

            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                #说明左边有序，利用左边进行判断
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 说明右边有序,利用右边进行判断
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

s = Solution()
data = [5,1]
print(s.search(data,1))