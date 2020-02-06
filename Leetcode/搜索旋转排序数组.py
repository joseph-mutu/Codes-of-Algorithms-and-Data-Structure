#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-08 07:00:38
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
			mid = int((left+right)/2)
			print("left,right",left,right)
			if nums[mid] == target:
				return mid
			if nums[mid] > nums[right]:
				# 左边有序，且mid 本身在有序数组内
				if nums[left] <= target and nums[mid] > target:
					# mid 值存在于 mid 左边
					right = mid - 1
				else:
					# mid 值存在于 mid 右边
					left = mid + 1
			else:
				# 右边有序，且 mid 本身就在有序数组中
				if nums[right] >= target and nums[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
		return -1

a = Solution()
print(a.search([4,5,6,7,0,1,2],3))

