#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-15 09:22:18
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        node_list = []
        perimeter = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] > 0:
                    node_list.append((x,y))
                    # -1 means the visited area
                    grid[x][y] = -1

                    while node_list:
                        x,y = node_list.pop(0)
                        if x == 0:
                            perimeter += 1
                        elif grid[x-1][y] == 0:
                            perimeter += 1
                        if x == len(grid) - 1:
                            perimeter += 1
                        elif grid[x+1][y] == 0:
                            perimeter += 1
                        if y == 0:
                            perimeter += 1
                        elif grid[x][y-1] == 0:
                            perimeter += 1
                        if y == len(grid[0]) - 1:
                            perimeter += 1
                        elif grid[x][y+1] == 0:
                            perimeter += 1
                        for nx,ny in ((x-1,y),(x,y+1),(x+1,y),(x,y-1)):
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] > 0:
                                grid[nx][ny] = -1
                                node_list.append((nx,ny))
        return perimeter

s = Solution()
grid = [
 [0,1,0,0],
 [0,0,0,0]]
print(s.islandPerimeter(grid))