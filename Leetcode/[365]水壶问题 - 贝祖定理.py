#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-21 08:11:10
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def canMeasureWater(self, x, y, z):
        def gcd(x,y):
            if x%y == 0:
                return y
            return gcd(y,x%y)
        if z%gcd(x,y) == 0:
            return True
        return False
s = Solution()
print(s.canMeasureWater(3,5,4))

