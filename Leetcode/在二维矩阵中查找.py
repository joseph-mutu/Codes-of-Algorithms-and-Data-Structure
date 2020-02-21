#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-21 06:12:17
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        思路:
            首先利用二分，查找列,最后一个小于 target 的目标，确定行的位置
            再次利用普通二分，查找行
        """
        if not matrix or not matrix[0]:
            return False
        row_len = len(matrix) 
        col_len = len(matrix[0])

        left_row = row_len - 1
        left_col = 0

        right_row = 0
        right_col = col_len - 1

        while left_row >= right_row and left_col <= right_col:
            if matrix[left_row][left_col] == target or matrix[right_row][right_col] == target:
                return True
            if matrix[left_row][left_col] > target:
                left_row -= 1
            else:
                left_col += 1
            if matrix[right_row][right_col] > target:
                right_col -= 1
            else:
                right_row += 1
        return False



matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
s = Solution()
print(s.searchMatrix(matrix,20))
