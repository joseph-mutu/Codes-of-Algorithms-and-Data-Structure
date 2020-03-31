#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-30 10:28:30
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class NumArray(object):

    def __init__(self, nums):

        if not nums or nums is None:
            self.dp = None

        self.dp = [0]
        for i in range(len(numsl)):
            self.dp.append(self.dp[-1] + nums[i])
            
    def sumRange(self, i, j):
        if self.dp is None:
            return None
        return self.dp[j+1] - self.dp[i]

s = NumArray([-2, 0, 3, -5, 2, -1])
print(s.dp)
print(s.sumRange(0,5))


