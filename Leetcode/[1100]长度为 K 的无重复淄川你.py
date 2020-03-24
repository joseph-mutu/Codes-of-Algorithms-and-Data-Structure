#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-24 18:33:21
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        if K > len(S):
            return 0
        
        contain = collections.Counter()
        l,r = 0,0
        num = 0
        
        while r< len(S):

            contain[S[r]] += 1
            r += 1

            while r - l == K:
                
                max_val = max(contain.values())
                if max_val == 1:
                    num += 1
                contain[S[l]] -= 1
                if contain[S[l]] == 0:
                    del contain[S[l]]
                l += 1
        return num

s= Solution()
print(s.numKLenSubstrNoRepeats("havefunonleetcode",5))
