#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-05 06:57:47
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
import re

INT_MAX = 2147483647
INT_MIN = -2147483648
class Solution():
    def myAtoi(self,str):
        if not str:
            return 0
        str_int = str.lstrip()
        p1 = r"[+-]?\d+"
        pattern = re.compile(p1)
        if pattern.match(str_int) is not None:
            value = pattern.match(str_int).group()
            return max(min(int(value),INT_MAX),INT_MIN)
        else:
            return 0

s = Solution()
string = "42"
print(s.myAtoi(string))
