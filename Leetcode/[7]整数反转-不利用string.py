#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-27 09:25:00
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def reverse(self, x):
        
        boundary = (1<<31) - 1 if x>0 else (1<<31)

        y = abs(x)

        res = 0
        while y:
            # pop simulation to take out the last digit of x 
            pop = y%10
            y //= 10 
            # pus simulation
            res = res * 10 + pop
            if res > boundary:
                return 0
        return res if x > 0  else -res

s = Solution()
print(s.reverse(-1230))