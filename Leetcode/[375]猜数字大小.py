#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-07 08:29:53
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def getMoneyAmount(self, n):
        #使用 dp
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        # # traverse from the end
        # for i in range(n-2,-1,-1):
        #     for j in range(i+1,n):
        #         for p in range(i,j+1):
        #             if p == i:
        #                 dp[i][j] = min(dp[i][j],i+1+dp[i+1][j])
        #             elif p == j:
        #                 dp[i][j] = min(dp[i][j],j+1+dp[i][j-1])
        #             else:
        #                 dp[i][j] =min(dp[i][j],p+1+max(dp[i][p-1],dp[p+1][j]))

        # traverse along with the diagonal
        for len in range(2,n+1):
            for start in range(n-len+1):
                end = start + len - 1
                for pivot in range(start, end + 1):
                    if pivot == start:
                        dp[start][end] = min(dp[start][end],pivot+1+dp[start + 1][end])
                    elif pivot == end:
                        dp[start][end] = min(dp[start][end],pivot+1+dp[start][end-1])
                    else:
                        dp[start][end] = min(dp[start][end],pivot+1 + max(dp[start][pivot - 1],dp[pivot + 1][end]))
        return dp[0][n-1]
s = Solution()
print(s.getMoneyAmount(5))
