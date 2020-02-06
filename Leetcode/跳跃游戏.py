#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-14 06:39:38
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def canJump(self, nums):
		length = len(nums) - 1
		reach = 0
		for i in range(len(nums)):
			if i > reach or reach > length:
				break
			reach = max(reach,nums[i]+i)
		return reach>=length

s = Solution()
print(s.canJump([2,0,0]))

