#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-04 19:31:15
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def removeDuplicates(self, nums):
		if nums:
			cur = 1
			change_pos = 1
			while cur < len(nums):
				if nums[cur] != nums[cur-1]:
					nums[change_pos] = nums[cur]
					change_pos += 1
				cur += 1
			return change_pos


a = [1,1,2]
s = Solution()
print(s.removeDuplicates(a))