#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-22 06:52:36
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections 
class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        ans_start,min_len = 0,float('inf')
        #使用滑动窗口
        l,r = 0,0
        contain = collections.Counter()
        target = collections.Counter(t)

        match = 0 # how many letters match
        #从 0 位置开始，扩展右边界，直到其包含所有的 target
        while r < len(s):
            if target[s[r]] > 0:
                contain[s[r]] += 1
                if contain[s[r]] == target[s[r]]:
                    match += 1
            # r 保存的是覆盖target子串右边界的下一位
            r += 1
            while match == len(target):
                if r - l < min_len:
                    ans_start = l
                    min_len = r - l
                #开始移动左边界，直到当前子串不覆盖 target为止
                if target[s[l]] > 0:
                    contain[s[l]] -= 1
                    if contain[s[l]] < target[s[l]]:
                        match -= 1
                l += 1  
        if min_len == float('inf'):
            return ""
        return s[ans_start:ans_start + min_len]
s = Solution()
print(s.minWindow( "aaaaaaaaaaaabbbbbcdd","abcdd"))
    