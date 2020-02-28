#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-27 10:05:13
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def setZeroes(self, matrix):
        if len(matrix[0]) == 0:
            return matrix

        row_len = len(matrix)
        col_len = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # 首先扫描第一行和第一列，看是否要将第一行或者第一列设为0
        for i in range(row_len):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        for i in range(col_len):
            if matrix[0][i] == 0:
                first_row_zero = True
                break

        for i in range(1,row_len):
            for j in range(1,col_len):
                if matrix[i][j] == 0:
                    # 在当前点的行首位和列首位留下 0 作为标记点
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # 将除第一行外，标记点的所在行全部设为 0
        for i in range(1,row_len):
            if matrix[i][0] == 0:
                matrix[i] = [0 for _ in range(col_len)]
        # 除第一列外，标记点所在的列全部设为 0
        for j in range(1,col_len):
            if matrix[0][j] == 0:
                for k in range(1,row_len):
                    matrix[k][j] = 0
        if first_col_zero:
            for i in range(row_len):
                matrix[i][0] = 0
        if first_row_zero:
            for i in range(col_len):
                matrix[0][i] = 0
        return matrix
s = Solution()
matrix =[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
print(s.setZeroes(matrix))