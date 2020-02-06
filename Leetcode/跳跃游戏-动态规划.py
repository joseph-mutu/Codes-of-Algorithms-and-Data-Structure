#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-14 07:20:46
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def canJump(self, nums):
		if not nums:
			return False
		dp = [0 for i in range(len(nums))]
		for i in range(1,len(nums)):
			dp[i] = max(dp[i-1],nums[i-1]) - 1
			if dp[i] <0:
				print(i)
				return False
		return True

s = Solution()
print(s.canJump([2,0,0]))