#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 08:21:56
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return None
        n = len(matrix)
        pos = [[i,0]for i in range(n)]

        while 1:
            row,col = min(pos,key = lambda x: matrix[x[0]][x[1]] if x[1] < n else float('inf'))
            if k == 1:
                return matrix[row][col]
            pos[row][1] += 1
            k -= 1
s = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
print(s.kthSmallest(matrix,9))
