#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-22 13:25:11
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):
    def nthUglyNumber(self, n):
        if n < 0:
            return 0
        dp = [1]

        p_2,p_3,p_5 = 0,0,0

        while len(dp) != n:
            dp.append(min(2*dp[p_2],3*dp[p_3],5*dp[p_5]))
            if dp[-1] == 2*dp[p_2]:
                p_2 += 1
            if dp[-1] == 3*dp[p_3]:
                p_3 += 1
            if dp[-1] == 5*dp[p_5]:
                p_5 += 1
        print(dp)
        return dp[n-1]
s = Solution()
print(s.nthUglyNumber(217))