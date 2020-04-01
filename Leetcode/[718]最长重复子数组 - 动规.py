#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-01 18:48:44
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def findLength(self, A, B):
        dp = [[0 for _ in range(len(A)+1)]for _ in range(len(B)+1)]

        for i in range(1,len(B)+1):
            for j in range(1,len(A)+1):
                if B[i-1] == A[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1

        return max(max(row) for row in dp)
s = Solution()
print(s.findLength([0,1,1,1,1],[1,0,1,0,1]))

