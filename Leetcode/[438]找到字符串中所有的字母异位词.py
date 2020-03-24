#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-22 08:39:46
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
        l,r = 0,0

        contain = collections.Counter()
        target = collections.Counter(p)

        match = 0

        #use sliding window
        while r < len(s):
            # r points to the last pos of a feasible solution
            if target[s[r]] > 0:
                contain[s[r]] += 1
                if contain[s[r]] == target[s[r]]:
                    match += 1
            print(contain,target,l,r)
            while match == len(target):
                if r + 1 - l == len(p):
                    start.append(l)
                # shrink the left border
                if target[s[l]] > 0:
                    contain[s[l]] -= 1
                    if contain[s[l]] < target[s[l]]:
                        match -= 1
                l += 1
            r += 1
        return start

s = Solution()
print(s.findAnagrams("baa","aa"))
