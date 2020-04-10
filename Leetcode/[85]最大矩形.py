#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-10 15:37:12
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        max_area = 0

        nrow = len(matrix)
        ncol = len(matrix[0])
        
        #每一列能达到的高度
        height = [0] * ncol
        # #每一列能向左扩充的最大边界
        left = [-1] * ncol
        # 每一列能向右扩充的最大边界
        right = [ncol] * ncol

        for row in range(nrow):

            # 当前列的高度
            for col in range(ncol):
                if matrix[row][col] == '1':
                    height[col] += 1
                else:
                    height[col] = 0
            # 当前列的左边界
            left_border = -1
            for col in range(ncol):
                if matrix[row][col] == '0':
                    left[col] = -1
                    left_border = col
                else:
                    left[col] = max(left_border,left[col])

            #当前列的右边界
            right_border = ncol
            for col in range(ncol-1,-1,-1):
                if matrix[row][col] == '0':
                    right_border = col
                    right[col] = ncol
                else:
                    right[col] = min(right_border,right[col])
            print(left,right,height)
            for col in range(ncol):
                max_area = max(max_area,height[col] * (right[col] - left[col] - 1))
                print(height[col] * (right[col] - left[col] - 1))
            print('*'*20)


        return max_area

s = Solution()
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print(s.maximalRectangle(matrix))
