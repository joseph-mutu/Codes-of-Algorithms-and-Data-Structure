#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-24 07:35:10
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def __init__(self):
        # dp[i] stores the number of combinations when n is i
        self.dp = {0:[None],1:["()"]}
    def generateParenthesis(self, n):
        for i in range(2,n+1):
            self.dp[i] = []
            for j in range(i):
                left_list = self.dp[j]
                right_list = self.dp[i-1-j]

                for left in left_list:
                    left = "" if left is None else left
                    for right in right_list:
                        right = "" if right is None else right
                        self.dp[i].append("(" + left + ")" + right)

        return self.dp[n]
s = Solution()
print(s.generateParenthesis(2))