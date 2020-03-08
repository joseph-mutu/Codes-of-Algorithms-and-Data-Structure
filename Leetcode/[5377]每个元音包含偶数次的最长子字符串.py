#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-07 16:21:14
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def findTheLongestSubstring(self, s):
        length = len(s)
        vowel = {'a':0,'e':0,'i':0,'o':0,'u':0}
        while length:
            left = 0
            right = left + length
            while right < len(s) + 1:
                print(s[left:right])
                if self.is_match(s[left:right]):

                    return length
                right += 1
                left += 1
            length -= 1
        return 0

    def is_match(self,list):
        vowel = {'a':0,'e':0,'i':0,'o':0,'u':0}
        for term in list:
            if term in vowel:
                vowel[term] += 1
        for term, times in vowel.items():
            if times%2 != 0:
                return False
        return True

s = Solution()
print(s.is_match("bcbcbc"))
# print(s.findTheLongestSubstring("bcbcbc"))