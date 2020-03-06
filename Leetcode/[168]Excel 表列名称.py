#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-06 07:25:59
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def convertToTitle(self, n):
        if not n or n <= 0:
            return ""
        str_list = []

        while n:
            n -= 1
            tem = n%26
            str_list.append(chr(tem + ord('A')))
            n //= 26

        return "".join(str_list[::-1])
s = Solution()
print(s.convertToTitle(28))