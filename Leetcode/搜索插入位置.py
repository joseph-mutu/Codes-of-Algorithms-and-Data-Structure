#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-09 18:03:08
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def searchInsert(self, nums, target):
		if not nums:
			return None
		left = 0
		right = len(nums) - 1

		while left <= right:
			mid = int( (left+right)/2 )
			if nums[mid] == target:
				return mid
			elif nums[mid] > target:
				right = mid - 1
			elif nums[mid] < target:
				left = mid + 1
		return left

s = Solution()
print(s.searchInsert([1,3,5,6],7))
