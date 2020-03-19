#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-15 21:19:23
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if not word:
            return []
        abb_list = [""]
        for w in word:
            n = len(abb_list)
            for i in range(n):
                if abb_list[i] and abb_list[i][-1].isdigit():
                    abb_list.append(abb_list[i][:-1] + str(int(abb_list[i][-1])+1))
                else:
                    abb_list.append(abb_list[i]+'1')
            for i in range(n):
                abb_list[i] += w
            print(abb_list)
        return abb_list
s = Solution()
print(s.generateAbbreviations("word"))