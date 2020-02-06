#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-06 18:52:21
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution():
	def nextPermutation(self, nums):
		if not nums:
			return None
		flag = False
		for i in range(len(nums)-1,0,-1):
			for j in range(i-1,-1,-1):
				if nums[j] < nums[i] and not flag:
					tem = nums[i]
					nums[i] = nums[j]
					nums[j] = tem

					break_pos = j + 1
					nums[break_pos:] = sorted(nums[break_pos:])
					return nums
		return nums[::-1]

a = Solution()
print(a.nextPermutation([3,2,1]))



