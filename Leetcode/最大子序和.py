#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-12 06:56:44
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def maxSubArray(self, nums):
		if not nums:
			return None
		tem_sum = 0
		fin_max = float('-inf')

		for i in range(len(nums)):
			tem_sum += nums[i]
			tem_sum = max(tem_sum,nums[i])
			if tem_sum > fin_max:
				fin_max = tem_sum
		return fin_max
s = Solution()
print(s.maxSubArray([-2,-1]))