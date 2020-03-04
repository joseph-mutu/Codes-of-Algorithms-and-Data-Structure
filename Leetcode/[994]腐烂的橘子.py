#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-04 07:29:58
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def orangesRotting(self, grid):
        if not grid:
            return -1

        row_len = len(grid)
        col_len = len(grid[0])

        node_list = []

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 2:
                    node_list.append([i,j,0])

        direct_list = [[-1,0],[0,1],[1,0],[0,-1]]
        
        layer = 0

        while node_list:

            node_x,node_y,layer = node_list.pop(0)    

            for x,y in direct_list:

                new_x = node_x + x
                new_y = node_y + y

                if new_x >= 0 and new_x < row_len and \
                new_y >= 0 and new_y < col_len and \
                grid[new_x][new_y] == 1:

                    grid[new_x][new_y] = 2
                    node_list.append([new_x,new_y,layer + 1])

        if any(1 in row for row in grid):
            return -1
        return layer

s = Solution()
print(s.orangesRotting([[1,2]]))




