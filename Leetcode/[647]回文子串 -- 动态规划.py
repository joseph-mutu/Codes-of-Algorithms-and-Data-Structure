#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 08:18:50
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def countSubstrings(self, s):
        # 使用 dp
        if not s:
            return 0
        
        count = 0

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        # dp[i][j] denotes if the substring s[i:j] is palindrome
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    print(i,j)
                    dp[i][j] = True
                    count += 1
        return count

s = Solution()
print(s.countSubstrings("ababa"))