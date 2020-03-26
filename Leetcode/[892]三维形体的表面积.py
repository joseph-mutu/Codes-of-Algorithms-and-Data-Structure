#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-24 19:53:42
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):
    def surfaceArea(self, grid):
        if not grid:
            return 0
        surface = 0
        
        def neighbour(x,y):
            for nx,ny in ((x-1,y),(x,y+1),(x+1,y),(x,y-1)):
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    yield min(grid[x][y],grid[nx][ny])

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    continue
                surface += (6 * grid[x][y] - (grid[x][y] - 1 )* 2)
                for nei in neighbour(x,y):
                    surface -= nei
        return surface
s = Solution()
print(s.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))
