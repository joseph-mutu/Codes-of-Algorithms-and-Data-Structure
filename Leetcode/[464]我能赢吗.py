#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-07 10:04:27
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if maxChoosableInteger >= desiredTotal:
            return True
        elif maxChoosableInteger * (1+maxChoosableInteger) / 2 < desiredTotal:
            return False
        memo = {}
        return self.backtrack(0,desiredTotal,memo,maxChoosableInteger)

    def backtrack(self,stat,target,memo,n):
        if stat in memo:
            return memo[stat]  
        for i in range(1,n+1):
            cur = 1 << (i-1)
            if cur & stat != 0:
                continue
            if target <= i or  not self.backtrack(cur | stat, target -i,memo,n):
                memo[stat] = True
                return True
        memo[stat] = False
        return False
s = Solution()
print(s.canIWin(4,6))