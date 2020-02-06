#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-11 17:15:06
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def combinationSum2(self, candidates, target):
		if not candidates:
			return None
		candidates = sorted(candidates)
		ans = []
		cur_ans = []

		self.search(candidates,0,target,ans,cur_ans)

		return ans
	def search(self,data,cur_pos,target,ans,cur_ans):
		if target < 0:
			return

		if target == 0:
			ans.append(cur_ans[:])
			return

		for i in range(cur_pos,len(data)):
			# if i != cur_pos and data[i-1] == data[i]:
			# 	continue
			cur_ans.append(data[i])
			self.search(data,i+1,target - data[i],ans,cur_ans)
			cur_ans.pop()

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5],8))

