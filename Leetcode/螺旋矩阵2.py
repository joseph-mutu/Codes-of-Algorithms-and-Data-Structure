#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-16 17:28:42
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def generateMatrix(self, n):
		if n <= 0:
			return [[]]
		if n == 1:
			return [[1]]

		cur_num = 1
		fin_mat = [[0 for i in range(n)] for j in range(n)]

		start = 0



		while start*2 < n :

			end_col = n - start - 1
			end_row = n - start - 1	


			# first row
			for i in range(start,end_col+1):
				fin_mat[start][i] = cur_num
				cur_num += 1
			# print(fin_mat)
			# last column
			if end_row > start:
				for i in range(start+1,end_row+1):
					fin_mat[i][end_col] = cur_num
					cur_num += 1
			# print(fin_mat)
			# last row
			if end_row > start and end_col > start:
				for i in range(end_col - 1,start-1,-1):
					fin_mat[end_row][i] = cur_num
					cur_num += 1
			# print(fin_mat)
			# first column
			if end_row - start > 1 and end_col > start:
				for i in range(end_row - 1,start,-1):
					fin_mat[i][start] = cur_num
					cur_num+=1
			start += 1
		return fin_mat
s = Solution()
print(s.generateMatrix(3))



