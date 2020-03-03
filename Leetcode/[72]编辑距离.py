#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-03 06:54:50
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def minDistance(self, word1, word2):
        if not word1 and not word2:
            return 0
        elif not word1 and word2:
            return len(word2)
        elif word1 and not word2:
            return len(word1)

        word1_len = len(word1)
        word2_len = len(word2)

        dp = [[0 for _ in range(word2_len+1)] for _ in range(word1_len+1)]
        for j in range(1,word2_len + 1):
            dp[0][j] = j
        for i in range(1,word1_len + 1):
            dp[i][0] = i

        for i in range(1,word1_len+1):
            for j in range(1,word2_len+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j-1] + 1,
                        dp[i-1][j] + 1,
                        dp[i][j-1] + 1)
        return dp[word1_len][word2_len]

s = Solution()
print(s.minDistance("b",""))

