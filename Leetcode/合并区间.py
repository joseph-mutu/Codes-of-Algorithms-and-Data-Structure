#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-15 06:19:30
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def merge(self, intervals):
		if not intervals:
			return []
		intervals = sorted(intervals)

		merge_inte = [intervals[0]]

		for i in range(1,len(intervals)):
			if merge_inte[-1][1] < intervals[i][0]:
				merge_inte.append(intervals[i])
			else:
				merge_inte[-1][1] = max(merge_inte[-1][1],intervals[i][1])
		return merge_inte

s = Solution()
print(s.merge([[1,4],[2,3]]))

