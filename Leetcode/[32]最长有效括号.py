#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-10 14:28:29
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def longestValidParentheses(self, s):
        #use dp

        res = 0

        if not s:
            return 0
        dp = [0] * len(s)
        for i in range(1,len(s)):
            if s[i] == '(':
                continue
            else:
                if s[i-1] == '(':
                    dp[i] = dp[i-2]+2 if i -2 >= 0 else 2
                elif s[i-1] == ')':
                    if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1]-1] == '(':
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2 if i - dp[i-1] - 2 >= 0 else dp[i-1] + 2
            res = max(dp[i],res)
        return res

s = Solution()
print(s.longestValidParentheses("(()))())("))
