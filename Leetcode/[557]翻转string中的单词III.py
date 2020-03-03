#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-02 20:29:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def reverseWords(self, s):
        if not s:
            return ""
        word_list = s.split()
        print(word_list)
        for i in range(len(word_list)):
            word_list[i] = word_list[i][::-1]
        return " ".join(word_list)

s = Solution()
print(s.reverseWords(""))