#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-29 20:26:17
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def fourSum(self,nums,target):
		if len(nums) < 4:
			return None
		nums.sort()
		ans = []
		for first_pos in range(0,len(nums)-3):
			if first_pos != 0 and nums[first_pos] == nums[first_pos-1]:
				continue
			for second_pos in range(first_pos+1,len(nums) - 2):
				if second_pos != first_pos+1 and nums[second_pos] == nums[second_pos-1]:
					continue
				tem_target = target - nums[first_pos] - nums[second_pos]
				right = second_pos + 1
				left = len(nums) - 1
				while right < left:
					if nums[right] + nums[left] == tem_target:
						ans.append([nums[first_pos],nums[second_pos],nums[right],nums[left]])
						tem_right = nums[right]
						tem_left = nums[left]
						while right < left and nums[right] == tem_right:
							right += 1
						while right < left and nums[left] == tem_left:
							left -= 1
					elif nums[right] + nums[left] < tem_target:
						right += 1
					elif nums[right] + nums[left] > tem_target:
						left -= 1
		return ans

s = Solution()
print(s.fourSum([-1,0,1,2,-1,-4,-1],-1))

