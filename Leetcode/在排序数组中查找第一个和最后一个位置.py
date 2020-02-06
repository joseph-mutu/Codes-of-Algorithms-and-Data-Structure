#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-09 17:32:24
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def searchRange(self, nums, target):
		if not nums:
			return [-1,-1]

		if len(nums) == 1 :
			if nums[0] == target:
				return [0,0]
			else:
				return [-1,-1]

		first = target - 0.5
		last = target + 0.5 

		first_pos = self.search(nums,first)
		last_pos = self.search(nums,last) - 1

		print(first_pos,last_pos)
		if first_pos >= len(nums) or nums[first_pos] != target:
			return [-1,-1]
		else:
			return [first_pos,last_pos]

	def search(self,nums,target):

		left = 0
		right = len(nums) - 1

		while left <= right:
			mid = int( (left+right)/2)
			if nums[mid] < target:
				left = mid + 1 
			elif nums[mid] > target:
				right = mid - 1
		return left

a = Solution()
print(a.searchRange([5,7,7,8,8,10],6))
