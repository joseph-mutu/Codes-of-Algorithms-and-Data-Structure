#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-07 15:13:38
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def PredictTheWinner(self, nums):
        #using dynamic programming
        n = len(nums)

        dp = [[[0,0] for _ in range(n)]for _ in range(n)]

        #dp[i][i][0] denote the first player
        for i in range(n):
            dp[i][i][0] = nums[i]
        #traverse along with the diagonal
        for l in range(2,n+1):
            for start in range(n - l + 1):
                end = start + l - 1
                #first player
                left = nums[start] + dp[start + 1][end][1]
                right = nums[end] + dp[start][end-1][1]
                dp[start][end][0] = max(left,right)

                #if the first player chooses left
                if left > right:
                    dp[start][end][1] = dp[start +1 ][end][0]
                else:
                    dp[start][end][1] = dp[start][end-1][0]
        return dp[0][n-1][0] >= dp[0][n-1][1]

s = Solution()
print(s.PredictTheWinner([1,1]))
