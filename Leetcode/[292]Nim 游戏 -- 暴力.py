#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-06 15:04:18
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def canWinNim(self, n):
        memo = {}
        self.dfs(1,4,memo)
        print(memo)
        return memo[n]


    def dfs(self,turn,n,memo):
        print(memo)
        if n in memo:
            return memo[n]
        next = (turn+1) %2
        for i in range(1,4):
            if n-i == 0:
                print(n,i,turn)
                if turn == 1:
                    ans = True
                else:
                    ans = False
                memo[n] = ans
                return ans
            if n - i > 0 and self.dfs(next,n-i,memo):  
                memo[n] = True
                return True
        memo[n] = False 
        return False
s = Solution()
print(s.canWinNim(4))