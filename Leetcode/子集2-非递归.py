#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-09 07:18:33
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def subsetsWithDup(self, nums):
		if not nums:
			return []
		res = [[]]
		nums.sort()
		pre_num = None
		pre_len = 0

		for num in nums:

			start = pre_len if num == pre_num else 0
			pre_len = len(res)
			pre_num = num
			for i in range(start,len(res)):
				tem = res[i][:]
				tem.append(num)
				res.append(tem)
			# print(res)
		return res

s = Solution()
print(s.subsetsWithDup([2,2,2,2]))

