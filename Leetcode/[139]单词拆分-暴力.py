#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-01 06:51:42
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def wordBreak(self, s, wordDict):
        if not wordDict:
            return False
        if self.word_seperate(s,wordDict,0):
            return True
        return False

    def word_seperate(self,s,wordDict,start):
        if start == len(s):
            return True
        for end in range(start+1,len(s)+1):
            # s[start:end] 表示从 start 开始到 end 之前的子串
            if s[start:end] in wordDict and self.word_seperate(s,wordDict,end):
                return True
        return False

x = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
dic = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
s = Solution()
print(s.wordDict(x,dic))
