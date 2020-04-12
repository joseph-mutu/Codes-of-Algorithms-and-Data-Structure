#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-12 11:00:42
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

        dp = [[0 for _ in range(ncol)] for _ in range(2)]
        max_area = 0

        for i in range(ncol):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                max_area = 1

        for i in range(1,nrow):
            if matrix[i][0] == '1':
                dp[1][0] = 1
                max_area = max(max_area,1)

            for j in range(1,ncol):
                if matrix[i][j] == '1':
                    dp[1][j] = min(dp[1][j-1],dp[0][j-1],dp[0][j]) + 1
                    max_area = max(max_area,dp[1][j] ** 2)
            dp[0] = dp[1]
            dp[1] = [0] * ncol
        return max_area

s = Solution()
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
print(s.maximalSquare(matrix))