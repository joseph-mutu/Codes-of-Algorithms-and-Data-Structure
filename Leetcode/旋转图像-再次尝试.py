#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-20 06:30:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []

        length = len(matrix)

        for i in range(int(length/2)):
            for j in range(i,length - 1 - i):
                tem = matrix[i][j]
                matrix[i][j] = matrix[length - 1 - j][i]
                matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]
                matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
                matrix[j][length - 1 - i] = tem
        return matrix

s = Solution()
matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
print(s.rotate(matrix))