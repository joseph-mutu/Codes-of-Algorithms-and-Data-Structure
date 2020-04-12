#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-12 11:48:55
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import math
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0

        dp = [float('inf')] *(n+1)
        dp[1]= 1
        dp[0] = 0
        square_num = [i**2 for i in range(int(math.sqrt(n))+1)]
        min_num = float('inf')

        for i in range(2,n+1):
            for num in square_num:
                if i - num >= 0:
                    dp[i] = min(dp[i],dp[i-num] + 1)
                else:
                    break
        return dp[n]

s = Solution()
print(s.numSquares(0))


