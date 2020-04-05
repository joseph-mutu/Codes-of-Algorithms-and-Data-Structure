#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 17:09:24
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):

    def __init__(self):
        self.nums = 0

    def totalNQueens(self, n):
        if n == 0:
            return 0

        # construct the graph
        graph = [["." for _ in range(n)]for _ in range(n)]

        self.backtrack(0,graph)

        return self.nums


    def backtrack(self,row,graph):
        if row == len(graph):
            self.nums += 1

        for col in range(len(graph)):
            if self.check(row,col,graph):
                graph[row][col] = 'Q'
                self.backtrack(row + 1,graph)
                graph[row][col] = '.'

    def check(self,x,y,graph):
        #检查列
        for nx in range(x):
            if graph[nx][y] == 'Q':
                return False

        # 检查左上对角线
        nx,ny = x -1,y-1
        while nx >= 0  and ny >= 0:
            if graph[nx][ny] == 'Q':
                return False
            nx -= 1
            ny -= 1

        # 检查右上对角线
        nx,ny = x-1,y+1
        while 0 <= nx and ny < len(graph):
            if graph[nx][ny] == 'Q':
                return False
            nx -= 1
            ny += 1

        return True

s = Solution()
print(s.totalNQueens(5))