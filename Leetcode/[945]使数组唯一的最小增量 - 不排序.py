#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-21 20:09:33
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections 
class Solution(object):
    def minIncrementForUnique(self, A):
        if not A:
            return 0

        count = collections.Counter(A)
        steps = 0
        n_repeat = 0
        # 线性探测
        for i in range(80000):
            if count[i] >= 2:
                n_repeat += count[i] - 1
                steps -= i*(count[i]-1)
            elif count[i] == 0  and n_repeat > 0:
                n_repeat -= 1
                steps += i
        return steps
s = Solution()
print(s.minIncrementForUnique([3,2,1,2,1,7]))
