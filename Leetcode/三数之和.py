#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-12 20:04:43
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums and len(nums) < 3:
            return []
        nums = sorted(nums)
        left = 0 
        ans_list = []

        while left < len(nums) - 2:
            if left != 0 and nums[left] == nums[left - 1]:
                left += 1
                continue
            target = 0 - nums[left]
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                if nums[mid] + nums[right] == target:
                    ans_list.append([nums[left],nums[mid],nums[right]])
                    tem_mid = mid 
                    tem_right = right
                    # 在恰好找到一个合适的序列后，mid 与 right 都要进行移动
                    # 这里将 mid 移到不重复的第一个点
                    # 将 right 同样移动到不重复的第一个点
                    # mid 值不变，right 值变是不可能的答案，所以不需要考虑
                    while mid < right and nums[mid] == nums[tem_mid]:
                        mid += 1
                    while mid < right and nums[right] == nums[tem_right]:
                        right -= 1
                elif nums[mid] + nums[right] > target:
                    right -= 1
                elif nums[mid] + nums[right] < target:
                    mid += 1
            left += 1
s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))



