#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-10 21:36:07
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def numTrees(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for idx in range(3,n+1):
            #表示当前在求解第几个数的情况
            tem_sum = 0
            for cur in range(1,idx+1):
                left = cur - 1
                right = idx - cur
                tem_sum += dp[left]*dp[right]
            dp[idx] = tem_sum
        return dp[n]
s = Solution()
print(s.numTrees(3))
