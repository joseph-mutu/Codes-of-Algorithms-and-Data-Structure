#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-26 06:47:35
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def __init__(self):
        self.results = []
    def permutation(self, S):
        S = list(S)
        self.search(S,[])
        return self.results

    def search(self,S,path):
        #S is a list
        if not S:
            self.results.append("".join(path[:]))
            return
        for i in range(len(S)):
            S[0],S[i] = S[i],S[0]
            path.append(S[0])
            self.search(S[1:],path)
            path.pop()

s = Solution()
print(s.permutation("qwe"))