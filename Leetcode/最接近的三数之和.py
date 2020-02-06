#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-15 20:28:35
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution():
	def threeSumClosest(self, nums, target):
		cur_min = 9999
		nums.sort()
		ans = [[]]
		for left in range(0,len(nums) - 1):
			mid = left + 1
			right = len(nums) - 1
			tem_target = target - nums[left]
			while mid < right:
				if abs(tem_target - nums[mid] - nums[right]) < cur_min:
					cur_min = abs(tem_target - nums[mid] - nums[right])
					ans[0] = [nums[left],nums[mid],nums[right]]
					if cur_min == 0:
						return sum(ans[0])
				if nums[mid] + nums[right] < tem_target:
					mid += 1
				elif nums[mid] + nums[right] > tem_target:
					right -= 1
		return sum(ans[0])

s = Solution()
print(s.threeSumClosest([0,1,2],3))

