#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-08 14:23:12
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import collections
class Solution(object):
    def wordBreak(self, s, wordDict):
        memo = collections.defaultdict(list)
        return self.backtrack(s,set(wordDict),memo)
    def backtrack(self,s,words,memo):
        if not s:
            return True
        if s in memo:
            return memo[s]
        res = []
        for i , _ in enumerate(s):
            word = s[:i+1]
            if word in words:
                rest = self.backtrack(s[i+1:],words,memo)
                if rest is True:
                    res.append(word)
                elif not rest:
                    continue
                else:
                    for term in rest:
                        res.append(word +" " + term)
        memo[s] = res
        return res

                    
s = Solution()
print(s.wordBreak(s = "catsandog",wordDict =  ["cats", "dog", "sand", "and", "cat"]))

