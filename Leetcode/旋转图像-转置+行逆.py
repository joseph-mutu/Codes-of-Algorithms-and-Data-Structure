#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-20 07:40:31
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def rotate(self, matrix):
        if not matrix:
            return []

        length = len(matrix)

        # transpose the matrix
        for i in range(length - 1):
            for j in range(i,length):
                tem = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = tem
        print(matrix)
        # Reverse each row of the matrix
        for i in range(length):
            matrix[i].reverse()
        return matrix

s = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(s.rotate(matrix))
