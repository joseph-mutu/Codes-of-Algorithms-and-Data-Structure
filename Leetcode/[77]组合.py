#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-27 10:56:03
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def __init__(self):
        self.results = []

    def combine(self, n, k):
        if k >= n:
            return [[i for i in range(1,n+1)]]

        if n <=0:
            return []

        self.backtrack(1,n,[],k)
        return self.results

    def backtrack(self,start,n,path,k):
        if len(path) == k:

            self.results.append(path[:])
            return 
        for i in range(start,n+1):
            path.append(i)
            self.backtrack(i + 1,n,path,k)
            path.pop()

s = Solution()
print(s.combine(1,1))