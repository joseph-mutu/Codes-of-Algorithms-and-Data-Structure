#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-05 14:22:53
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def titleToNumber(self, s):
        if not s:
            return 0
        num = 0
        mul = 1
        for letter in s[::-1]:
            num += (ord(letter) - ord('A') + 1) * mul
            mul *= 26
        return num

s = Solution()
print(s.titleToNumber('ZY'))