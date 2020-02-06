#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-11 19:28:10
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def rotate(self, matrix):
		if not matrix:
			return None
		length = len(matrix)
		for i in range(0,int(length/2)):
			for j in range(i,length - 1 - i):
				tem = matrix[i][j]
				matrix[i][j] = matrix[length - 1 - j][i]
				matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]
				matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
				matrix[j][length - 1 - i] = tem
		return matrix

s = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(s.rotate(matrix))
