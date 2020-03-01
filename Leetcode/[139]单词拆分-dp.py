#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-29 18:02:12
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):
    def wordBreak(self, s, wordDict):
        if not wordDict:
            return False
        dp = [False for _ in range(len(s)+1)]

        dp[0] = True

        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    print(i,j,s[j:i])
                    dp[i] = True
                    break
        return dp[-1]
s = Solution()
print(s.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))