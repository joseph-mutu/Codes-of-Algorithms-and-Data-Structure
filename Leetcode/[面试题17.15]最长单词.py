#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-26 20:53:49
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def longestWord(self, words):
        if not words:
            return ""
        
        check = set(words)
        words = sorted(words,key = lambda x:(-len(x),x))

        def dfs(word,depth):
            if word in check and depth > 0:
                return True
            for i in range(len(word)):
                if word[:i+1] in check and dfs(word[i+1:],depth + 1):
                    return True
            return False
        
        for word in words:
            if dfs(word,0):
                return word
        return ""

s = Solution()
print(s.longestWord(["cat","banana","dog","nana","walk","walker","dogwalker"]))
