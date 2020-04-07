#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-06 10:40:12
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def countServers(self, grid):
        nrow = len(grid)
        ncol = len(grid[0])
        row_flag = [0] * nrow
        col_flag = [0] * ncol

        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    row_flag[i] += 1
                    col_flag[j] += 1s

        count = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] > 0 and (row_flag[i] > 1 or col_flag[j] > 1):
                    count += 1
        return count
s = Solution()
grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
print(s.countServers(grid))