#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-02 10:28:48
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import re
class Solution(object):
    def removeVowels(self, S):
        return re.sub(r'[aeiou]',"",S)

s = Solution()
print(s.removeVowels(""))
