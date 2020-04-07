#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-06 08:18:47
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def isMatch(self, s, p):
        dp =[[-1 for _ in range(len(s)+1)] for _ in range(len(p)+1)]

        dp[0][0] = True
        for i in range(1,len(s)+1):
            dp[0][i] = False
        for i in range(1,len(p) + 1):
            dp[i][0] = False

        if p[0] == '.':
            for i in range(len(s)+1):
                dp[0][i] = True



        for i in range(1,len(p)+1):
            for j in range(1,len(s)+1):
                if p[i-1] == '*':
                    if i - 2 >= 0 and (p[i-2] != s[j-1] or p[i-2] != '.'):
                        dp[i][j] = dp[i-2][j]
                    else:
                        dp[i][j] = dp[i-2][j] or dp[i-1][j] or dp[i][j-1]

                elif p[i-1] == '.' or p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    
                else:
                    dp[i][j] = False
        print(dp)
        return dp[-1][-1]

s = Solution()
print(s.isMatch('aab','c*a*b'))