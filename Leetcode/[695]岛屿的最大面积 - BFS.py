#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-15 08:10:38
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0

        node_list = []
        max_area = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] != 0:
                    grid[x][y] = 0
                    node_list.append((x,y))
                    area = 1
                    while node_list:
                        x,y = node_list.pop(0)
                        print(x,y)
                        for n_x,n_y in ((x-1,y),(x,y+1),(x+1,y),(x,y-1)):
                            if 0 <= n_x < len(grid) and 0 <= n_y < len(grid[0]) and grid[n_x][n_y] != 0:
                                area += 1
                                grid[n_x][n_y] = 0
                                node_list.append((n_x,n_y))
                    if max_area < area:
                        max_area = area

        return max_area
s = Solution()
grid =[
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(s.maxAreaOfIsland(grid))