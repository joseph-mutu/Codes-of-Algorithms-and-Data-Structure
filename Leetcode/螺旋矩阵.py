#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-08 06:51:03
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

class Solution(object):

    def __init__(self):
        self.spiral = []

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix:
            self.printSpiral(matrix,0,0,len(matrix[0])-1,len(matrix)-1)
        return self.spiral

    def printSpiral(self,matrix,start_x,start_y,end_x,end_y):
        """
        start_x, start_y:
            the start X and Y are coordinates of the starting point
        end_x, end_y:
            the coordinates of the end point(on the diagonal line)
        """
        if start_x > end_x or start_y > end_y:
            return 
        col = end_y + 1
        row = end_x + 1

        # 打印第一行
        for i in range(start_x,row):
            self.spiral.append(matrix[start_y][i])

        # 满足第二个条件，打印最后一列
        if end_y - start_y >= 1:
            for i in range(start_y+1,col):
                self.spiral.append(matrix[i][end_x])

        # 打印最后一行
        if end_y - start_y >= 1:
            for i in range(end_x - 1,start_x - 1,-1):
                self.spiral.append(matrix[end_y][i])

        # 打印第一列
        if end_y - start_y > 1 and end_x - start_x >=1:
            for i in range(end_y - 1,start_y,-1):
                self.spiral.append(matrix[i][start_x])

        self.printSpiral(matrix,start_x + 1, start_y + 1, end_x - 1,end_y - 1)

matrix = [
  [1], [2], [3]
]

s = Solution()
print(s.spiralOrder(matrix))

