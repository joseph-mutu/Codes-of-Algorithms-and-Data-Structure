#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-06 07:09:07
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution():
    def __init__(self):
        self.island_count = 0
        self.adjacent_ope = [[0,-1],[1,0],[0,1],[-1,0]]
        self.node_bfs = []

    def dfs(self,grid,cur_row,cur_col):
        self.visit[cur_row][cur_col] = -1
        for row,col in self.adjacent_ope:
            if cur_row+row < self.row_limit and cur_row+row >= 0 and \
            cur_col+col < self.col_limit and cur_col+col >= 0 and \
            grid[cur_row+row][cur_col+col] != '0' and\
            self.visit[cur_row+row][cur_col+col] == 1:
                self.visit[cur_row+row][cur_col+col] = -1
                self.dfs(grid,cur_row + row,cur_col + col)

    def bfs(self,grid):
        while len(self.node_bfs) != 0:
            cur_row,cur_col = self.node_bfs.pop(0)
            
            for row,col in self.adjacent_ope:
                if cur_row+row < self.row_limit and cur_row+row >= 0 and cur_col+col < self.col_limit and cur_col+col >= 0 and grid[cur_row+row][cur_col+col] != '0' and self.visit[cur_row+row][cur_col+col] == 1:
                    self.node_bfs.append([cur_row+row,cur_col+col])
                    self.visit[cur_row+row][cur_col+col] = -1

    def numIslands(self, grid):
        if not grid:
            return 0
        self.visit = [[1 for i in range(len(grid[0]))]for j in range(len(grid))]
        self.row_limit = len(grid)
        self.col_limit = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '0' and self.visit[i][j] == 1: 
                    self.island_count += 1
                    self.node_bfs.append([i,j])
                    self.visit[i][j] = -1
                    self.bfs(grid)
        return self.island_count

s = Solution()
matrix = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
print(s.numIslands(matrix))
