#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-12 20:04:43
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def calMax(self,height,num1,num2):
		if height[num1] <= height[num2]:
			width = height[num1]
		else:
			width = height[num2]
		return width * abs(num2 - num1)
	def maxArea(self, height):
		if not height:
			return None
		fin_max = -1
		start = 0
		end = len(height) - 1
		while start < end:
			tem_area = self.calMax(height,start,end)
			if tem_area > fin_max:
				fin_max = tem_area
			if height[start] < height[end]:
				start += 1
			else:
				end -= 1
		return fin_max

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))

