#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-08 19:34:13
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def __init__(self):
        self.results = []
        self.left_count = 1
        self.right_count = 0

    def generateParenthesis(self, n):
        self.backtrack(n,['('])
        return self.results
    
    def backtrack(self,n,path):
        if self.left_count == n and self.right_count == n:
            self.results.append("".join(path[:]))
            return

        for c in ('(',')'):
            if self.left_count <= self.right_count and c == ')':
                continue
            if c == '(':
                if self.left_count < n:
                    self.left_count += 1
                else:
                    continue
            if c == ')':
                if self.right_count < n:
                    self.right_count += 1
                else:
                    continue

            path.append(c)
            self.backtrack(n,path)
            if c == '(':
                self.left_count -= 1
            else:
                self.right_count -= 1
            path.pop()
        return
            
s = Solution()
print(s.generateParenthesis(2))
