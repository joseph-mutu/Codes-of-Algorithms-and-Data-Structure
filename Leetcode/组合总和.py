#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-10 19:05:36
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def combinationSum(self, candidates, target):
		if not candidates:
			return None
		candidates = sorted(candidates)
		ans = []
		cur_ans = []
		cur_pos = 0
		self.search(candidates,ans,cur_ans,cur_pos,target)

		return ans
	def search(self,data,ans,cur_ans,cur_pos,target):
		if target < 0:
			return 
		if target == 0:
			ans.append(cur_ans[:])
			print(ans)

		for i in range(cur_pos,len(data)):
			cur_ans.append(data[i])
			self.search(data,ans,cur_ans,i,target - data[i])
			if cur_ans: cur_ans.pop()


s = Solution()
print(s.combinationSum([2,3,6,7],7))
