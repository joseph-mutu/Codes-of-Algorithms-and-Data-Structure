#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-17 07:18:22
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def threeSum(self, nums):
        if not nums:
            return []

        fin_list = []
        nums = sorted(nums)

        left = 0
        while left < len(nums) - 2:

            if left != 0 and nums[left] == nums[left - 1]:
                left += 1
                continue
            mid = left + 1
            right = len(nums) - 1
            tem = 0 - nums[left]

            while mid < right:
                if nums[mid] + nums[right] == tem:
                    fin_list.append([nums[left],nums[mid],nums[right]])
                    mid += 1
                    right -= 1
                    while mid != left + 1 and mid < len(nums) and nums[mid - 1] == nums[mid]:
                        mid += 1
                    while right != len(nums) - 1 and right >= 0 and nums[right + 1] == nums[right]:
                        right -= 1
                elif nums[mid] + nums[right] > tem:
                    right -= 1
                elif nums[mid] + nums[right] < tem:
                    mid += 1
            left += 1

        return fin_list

s = Solution()
print(s.threeSum([0,0,0]))

