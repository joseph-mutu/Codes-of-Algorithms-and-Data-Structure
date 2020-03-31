#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-31 20:23:29
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1:
            return 1
        if N <= 0:
            return -1
        
        trusts = [0] * N

        trust_nobody = set(i for i in range(N))

        for a,b in trust:
            trusts[b-1] += 1
            if a-1 in trust_nobody:
                trust_nobody.remove(a-1)
        print(trust_nobody)
        for people in trust_nobody:
            if trusts[people] == N-1:
                return people+1
        return -1
s= Solution()
print(s.findJudge(3,[[1,3],[2,3],[3,1]]))