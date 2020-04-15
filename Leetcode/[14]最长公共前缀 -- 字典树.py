#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 16:41:14
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

from typing import List

class Solution:
    def __init__(self):
        self.tire = {}
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #build the tire
        for i in range(len(strs)):
            word = strs[i]
            if not word:
                return ""
            root = self.tire
            for c in word:
                if c not in root:
                    root[c] = {}
                root = root[c]
        
        # find the first node that has two or more children
        root = self.tire
        res = ""
        while len(root) == 1:
            for child in root.keys():
                res += child
                root = root[child]
        return res
s = Solution()
print(s.longestCommonPrefix(["","racecar"]))
