#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-03 13:19:49
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def maxSubArray(self, nums):
		max_sum = float('-inf')
		tem_sum = 0
		for num in nums:
			tem_sum += num
			if tem_sum < num:
				tem_sum = num
			if max_sum < tem_sum:
				max_sum = tem_sum
		return max_sum
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
