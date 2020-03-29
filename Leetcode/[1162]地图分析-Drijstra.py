#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-29 08:05:54
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


from heapq import heappush,heappop

class Solution(object):
    def maxDistance(self, grid):
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])

        dis = [[float('inf') for _ in range(col)] for _ in range(row)]

        heap = []

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dis[i][j] = 0
                    heappush(heap,(0,i,j))

        if len(heap) == 0 or len(heap) == col * row:
            return -1

        while heap:
            distance,sx,sy = heappop(heap)
            if grid[sx][sy] >= 0:
                #collected 
                grid[sx][sy] = -1
                dis[sx][sy] = distance

                for nx, ny in ((sx-1,sy),(sx,sy+1),(sx+1,sy),(sx,sy-1)):
                    if 0 <= nx < row and 0 <= ny < col:
                        heappush(heap,(dis[sx][sy] + 1,nx,ny))

        return max(max(row) for row in dis)


s = Solution()
grid = [[1,0,0],[0,0,0],[0,0,0]]
print(s.maxDistance(grid))



