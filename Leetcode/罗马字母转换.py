#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-16 07:55:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def __init__(self):

        self.roman_dic = {"I":1,'V':5,'X':10,'L':50,'C':100,\
        'D':500,'M':1000}
        self.roamn_sub_dic = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,\
        'CM':900,}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        val = 0
        loc = 0
        while loc < len(s):
            if s[loc:loc+2] in self.roamn_sub_dic:
                val += self.roamn_sub_dic.get(s[loc:loc+2])
                loc += 2
            elif s[loc] in self.roman_dic:
                val += self.roman_dic.get(s[loc])
                loc += 1
            else:
                raise KeyError("the input is not allowed")

        return val

s = Solution()
string = "MCMXCIV"
print(s.romanToInt(string))


