#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-28 18:29:25
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def maxDistance(self, grid):
        if not grid:
            return -1

        #multi-sorces BFS
        row = len(grid)
        col = len(grid[0])
        
        dis = [[-1 for _ in range(row)]for _ in range(col)]

        land = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dis[i][j] = 0
                    land.append((i,j))

        if not land or len(land) == col*row:
            return -1

        while land:
            #多源
            sx,sy = land.pop(0)
            for nx,ny in self.neigh(sx,sy,grid):
                #如果该节点还没有被访问过
                if dis[nx][ny] == -1:
                    dis[nx][ny] = dis[sx][sy] + 1
                    land.append((nx,ny))

        return max(max(row) for row in dis)



    def neigh(self,x,y,grid):
        for nx,ny in ((x-1,y),(x,y+1),(x+1,y),(x,y-1)):
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                yield nx,ny





s = Solution()
grid = [[1,0,0],[0,0,0],[0,0,0]]
print(s.maxDistance(grid))