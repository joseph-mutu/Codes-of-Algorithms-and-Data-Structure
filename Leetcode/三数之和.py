#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-12 20:04:43
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def threeSum(self, nums):
		ans = []
		if not nums:
			return None
		nums.sort()
		# 保证三数之和为 0

		for left in range(0,len(nums)-2):
			if left > 0 and nums[left - 1] == nums[left]:
				continue
			mid = left + 1
			right = len(nums) - 1
			while mid < right :
				tem = 0 - nums[left]
				if nums[right] + nums[mid] == tem:
					ans.append([nums[left],nums[mid],nums[right]])
					tem_mid = nums[mid]
					tem_right = nums[right]
					while mid < right and nums[mid] == tem_mid:
						mid += 1
					while right > mid and nums[right] == tem_right:
						right -= 1
				elif nums[right] + nums[mid] < tem:
					mid += 1
				elif nums[right] + nums[mid] > tem:
					right -= 1

		return ans
s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))



