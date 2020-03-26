#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-26 18:00:47
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):

        def search(text1,text2):
            if not text1 or not text2:
                return 0
            if text1[-1] == text2[-1]:
                print(text1,text2,text1[0:len(text1)-1],text2[0:len(text2)-1])
                return search(text1[0:len(text1)-1],text2[0:len(text2)-1]) + 1

            else:
                return max(search(text1,text2[0:len(text2)-1]),
                    search(text1[0:len(text1)-1],text2) )
        return search(text1,text2)

s = Solution()
print(s.longestCommonSubsequence("abc","ab"))
