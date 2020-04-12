#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-12 10:05:23
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0
        nrow = len(matrix)
        ncol = len(matrix[0])

        dp = [[0 for _ in range(ncol)]for _ in range(nrow)]
        max_area = 0
        for i in range(ncol):
            if matrix[0][i] == '1':
                dp[0][i] = 1
        for j in range(nrow):
            if matrix[j][0] == '1':
                dp[j][0] = 1
        for i in range(1,nrow):
            for j in range(1,ncol):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1
                    max_area = max(max_area,dp[i][j] ** 2)
        return max_area

s = Solution()
matrix = [["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]
print(s.maximalSquare(matrix))