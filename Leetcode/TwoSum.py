#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-30 08:22:42
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def __init__(self):
		self.dict = {}
	def twoSum(self, nums, target):
		for i in range(len(nums)):
			if self.dict.get(target - nums[i]) is None:
				self.dict[nums[i]] = i
			else:
				return [self.dict[target-nums[i]],i]
data = [2, 7, 11, 15]
s = Solution()
print(s.twoSum(data,9))
