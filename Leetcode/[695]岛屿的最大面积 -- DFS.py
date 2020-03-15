#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-15 07:27:05
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        max_area = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] != 0:
                    max_area = max(self.dfs(x,y,grid),max_area)
        return max_area
    def dfs(self,s_x,s_y,grid):
        grid[s_x][s_y] = 0
        area = 1
        for n_x,n_y in self.generate_children(s_x,s_y,grid):
            area += self.dfs(n_x,n_y,grid)
        return area
    def generate_children(self,s_x,s_y,grid):
        for n_x,n_y in ((s_x-1,s_y),(s_x,s_y+1),(s_x+1,s_y),(s_x,s_y-1)):
            if 0 <= n_x < len(grid) and 0 <= n_y < len(grid[0]) and grid[n_x][n_y] != 0:
                yield n_x,n_y


s = Solution()
grid =[[1,1],
       [1,0]]
print(s.maxAreaOfIsland(grid))
