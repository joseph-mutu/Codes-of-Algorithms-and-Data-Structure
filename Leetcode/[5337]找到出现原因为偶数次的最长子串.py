#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-08 06:28:20
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

from collections import Counter
class Solution(object):
    def findTheLongestSubstring(self, s):

        vowel = Counter(a = 0,e = 1,i = 2,o = 3,u = 4)
        dic = {}
        res = [0,0,0,0,0]

        dic[(0,0,0,0,0)] = -1
        for length, term in enumerate(s):
            if term in vowel:
                res[vowel[term]] ^= 1
            dic[tuple(res)] = length
        # (0,0,0,0,0)表示从零开始的子串最大长度 - 1
        print(dic)
        res = [0,0,0,0,0]
        ans = dic[tuple(res)] + 1
        print(dic)
        for length, term in enumerate(s):
            if term in vowel:
                res[vowel[term]] ^= 1
                ans = max(ans,dic[tuple(res)] - length)

        return ans



s = Solution()
print(s.findTheLongestSubstring("eleetminicoworoep"))


