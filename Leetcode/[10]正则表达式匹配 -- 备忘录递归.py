#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-06 07:44:53
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def isMatch(self, s, p):
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(s) and j == len(p):
                ans = True
            elif i != len(s) and j == len(p):
                ans = False
            elif i == len(s):
                #如果当前 s 为空，但是 p 不为空
                if j + 2 <= len(p) and p[j+1] == '*':
                    ans = dp(i,j+2)
                else:
                    ans = False
            else:
                # 如果当前 s 和 p 都不为空,且 p 存在通配符
                if j+2 <= len(p) and p[j+1] == '*':
                    if s[i] != p[j] and p[j] !='.':
                        ans = dp(i,j+2)
                    else:
                        ans = dp(i+1,j) or dp(i,j+2)

                elif s[i] == p[j] or p[j] == '.':
                    ans = dp(i+1,j+1)
                else:
                    ans = False
            memo[(i,j)] = ans

            return ans

        return dp(0,0)

s = Solution()
print(s.isMatch("aaa","a*a"))