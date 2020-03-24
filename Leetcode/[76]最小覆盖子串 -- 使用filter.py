#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-22 09:16:25
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
class Solution(object):
    def findAnagrams(self, s, p):

        if not s or not p:
            return []
        start = []

        contain = collections.Counter()
        target = collections.Counter(p)

        filter_s = []
        for i,letter in enumerate(s):
            if target[letter] > 0:
                filter_s.append((letter,i))

        # filter_s 只保存与 target 相关的字母
        l,r = 0,0
        match = 0
        min_len = float('inf')
        start = 0

        print(filter_s,target)
        while r < len(filter_s):    
            if target[filter_s[r][0]] > 0:
                contain[filter_s[r][0]] += 1
                if contain[filter_s[r][0]] == target[filter_s[r][0]]:
                    match += 1

            while match == len(target):
                if filter_s[r][1] - filter_s[l][1] + 1 < min_len:
                    min_len = filter_s[r][1] - filter_s[l][1] + 1
                    start = filter_s[l][1]
                # start to shrink the left border
                if target[filter_s[l][0]] > 0:
                    contain[filter_s[l][0]] -= 1
                    if contain[filter_s[l][0]] < target[filter_s[l][0]]:
                        match -= 1
                l += 1
            r += 1
        if min_len == float('inf'):
            return ""
        return s[start:start + min_len]
s = Solution()
print(s.findAnagrams("ADOBECODEBANC","ABC"))


