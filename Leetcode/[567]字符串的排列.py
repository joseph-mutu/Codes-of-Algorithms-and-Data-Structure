#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-22 18:07:56
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections

class Solution(object):
    def checkInclusion(self, s1, s2):
        
        if len(s1) > len(s2):
            return False

        target = collections.Counter(s1)
        contain = collections.Counter()

        l,r = 0,0
        match = 0

        while r < len(s2):
            if target[s2[r]] > 0:
                print(s2[r])
                contain[s2[r]] += 1
                if contain[s2[r]] == target[s2[r]]:
                    match += 1
            print(contain,match,target,s2[r])

            while match == len(target):
                if r-l +1 == len(s1):
                    return True
                # 缩小左边界
                if target[s2[l]] > 0:
                    contain[s2[l]] -= 1
                    if contain[s2[l]] < target[s2[l]]:
                        match -= 1
                l += 1
            r += 1

        return False

s = Solution()
print(s.checkInclusion("ab","eidboaoo"))
