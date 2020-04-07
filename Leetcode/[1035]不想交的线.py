#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-06 10:01:03
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def maxUncrossedLines(self, A, B):
        if not A or not B:
            return 0
        dp = [[0 for _ in range(len(A)+1)]for _ in range(len(B)+1)]

        for i in range(1,len(B)+1):
            for j in range(1,len(A)+1):
                if B[i-1] == A[j-1]:
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

s = Solution()
a = [2,5,1,2,5]
b = [10,5,2,1,5,2]
print(s.maxUncrossedLines(a,b))
