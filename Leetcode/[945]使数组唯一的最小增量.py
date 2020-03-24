#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-21 19:50:39
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def minIncrementForUnique(self, A):
        if not A:
            return 0
        A = sorted(A)
        steps = 0
        print(A)
        for i in range(1,len(A)):
            if A[i] <= A[i-1]:
                steps += (A[i-1] - A[i] + 1)
                A[i] = A[i- 1] + 1 
                
        return steps

s = Solution()
print(s.minIncrementForUnique( [3,2,1,2,1,7]))
