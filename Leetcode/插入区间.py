#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-16 08:11:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def insert(self, intervals, newInterval):
		if not intervals:
			return [newInterval]
		cur = 0
		length = len(intervals)
		ans = []

		while cur < length and intervals[cur][1] < newInterval[0]:
			ans.append(intervals[cur])
			cur += 1
		while cur < length and intervals[cur][0] < newInterval[1]:
			newInterval[0] = min(intervals[cur][0],newInterval[0])
			newInterval[1] = max(intervals[cur][1],newInterval[1])
			cur += 1
		ans.append(newInterval)
		while cur < length:
			ans.append(intervals[cur])
			cur += 1
		return ans
		
s = Solution()
print(s.insert([],[6,8]))
