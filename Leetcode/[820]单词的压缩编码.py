#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-28 06:40:47
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def minimumLengthEncoding(self, words):
        if not words:
            return 0
        word_set = set(words)
        for word in words:
            for i in range(1,len(word)-1):
                word_set.discard(word[i:])
        return sum(len(word)+ 1 for word in word_set)
        
s = Solution()
print(s.minimumLengthEncoding(["time", "me", "bell"]))
