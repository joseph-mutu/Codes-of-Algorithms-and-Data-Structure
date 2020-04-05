#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-02 19:50:09
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


import re
class Solution(object):
    def myAtoi(self, string):
        INT_MAX = pow(2,31) - 1
        INT_MIN = -pow(2,31)
        string = string.lstrip()
        pattern = re.compile(r'[+-]?\d+')
        m = pattern.match(string)
        if not m:
            return 0

        num = m.group()
        return max(min(int(num),INT_MAX),INT_MIN)

s = Solution()
print(s.myAtoi("-91283472332"))