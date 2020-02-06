#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-15 20:28:35
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution():
	def removeElement(self, nums, val):
		if not nums:
			return None
		cur_pos = 0
		judge = 0
		new_lenth = 0
		while judge < len(nums):
			if nums[judge] != val:
				nums[cur_pos] = nums[judge]
				cur_pos += 1
				new_lenth += 1
			judge += 1
		return new_lenth
s = Solution()
print(s.removeElement([4,1,2,3,4],4))


