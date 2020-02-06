#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-21 08:07:01
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def findMin(self, nums):
		if not nums:
			return None

		left = 0
		right = len(nums) - 1
		if nums[left] < nums[right]:
			return nums[left]
		while right - left > 1:
			mid = int((left+right)/2)

			if nums[mid] >= nums[right]:
				# mid is in the first array
				left = mid
			else:
				right = mid
		return nums[right]

s = Solution()
print(s.findMin([3,4,5,1,2]))