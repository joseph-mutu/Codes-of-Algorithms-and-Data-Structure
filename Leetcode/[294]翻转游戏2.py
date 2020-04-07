#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-06 16:28:52
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def canWin(self, s):
        memo = {}
        return self.backtrack(s,memo,0)

    def backtrack(self,s,memo,turn):
        if (s,turn) in memo:
            return memo[(s,turn)]
        num = (turn+1)%2
        for i in range(len(s)-1):
            if s[i] == '+' and s[i+1] == '+':
                tem  = s[:i] +"--" +s[i+2:]
                if not self.backtrack(tem,memo,num):
                    memo[(s,turn)] = True
                    return True
        memo[(s,turn)] = False
        return False



s = Solution()
print(s.canWin("+++++++++"))

