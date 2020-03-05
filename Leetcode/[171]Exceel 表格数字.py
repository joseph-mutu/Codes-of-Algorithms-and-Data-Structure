#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-05 14:11:39
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def titleToNumber(self, s):
        if not s:
            return 0

        num = 0
        for letter in s:
            num *= 26

            num += (ord(letter) - ord('A') + 1)
        return num

s = Solution()
print(s.titleToNumber("ZY"))