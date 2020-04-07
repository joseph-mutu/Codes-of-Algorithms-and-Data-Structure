#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-06 10:03:06
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def maxUncrossedLines(self, A, B):
        if not A or not B:
            return 0
        
        dp = [0] * (len(A)+1)
        # row moves 
        for i in range(1,len(B)+1):
            tem = [0] * (len(A) + 1)
            for j in range(1,len(A)+1):
                if B[i-1] == A[j-1]:
                    tem[j] = dp[j-1] + 1
                else:
                    tem[j] = max(tem[j-1],dp[j])

            dp = tem[:]
        return dp[-1]

s = Solution()
a = [2,5,1,2,5]
b = [10,5,2,1,5,2]
print(s.maxUncrossedLines(a,b))

