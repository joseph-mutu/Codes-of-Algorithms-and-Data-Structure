#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-29 16:00:30
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def wordBreak(self, s, wordDict):
        if not wordDict:
            return False

        is_separable = [-1 for _ in range(len(s))]

        if self.word_check(s,wordDict,0,is_separable):
            return True
        return False

    def word_check(self,s,wordDict,start,is_separable):
        print(start,is_separable)
        if start == len(s):
            return True
        if is_separable[start] != -1:
            return is_separable[start]

        # 将字符串按照 start 分为两部分
        for i in range(start + 1,len(s)+1):
            #只有当第一个部分存在于 worddict 中时，才去查找第二部分
            if s[start:i] in wordDict and self.word_check(s,wordDict,i,is_separable):
                is_separable[start] = 1
                return True
        is_separable[start] = 0
        return False

s = Solution()
x = "aaaab"
dic = ["a","aa","aaa","aaaa"]
s = Solution()
print(s.wordBreak(x,dic))
# print(s.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))