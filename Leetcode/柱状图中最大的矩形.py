#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-06 07:17:06
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def largestRectangleArea(self, heights):
		if not heights:
			return 0

		stack = [-1]
		heights.append(-1)
		res = 0

		for idx,num in enumerate(heights):
			while heights[stack[-1]] > num:
				cur_idx = stack.pop()
				print(cur_idx,heights[cur_idx],heights[cur_idx] * (idx - stack[-1] - 1))
				res = max(res,heights[cur_idx] * (idx - stack[-1] - 1))
			stack.append(idx)
		return res

s = Solution()
heights = [2,1,5,6,2,3]
print(s.largestRectangleArea(heights))