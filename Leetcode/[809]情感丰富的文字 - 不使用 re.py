#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-02 09:31:59
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import itertools
class Solution(object):
    def expressiveWords(self, S, words):
        # 提取 S 的词干

        p,c = self.Regular(S)

        count = 0
        for word in words:
            w_p,w_c = self.Regular(word)

            if len(w_p) != len(p):
                continue

            count += all(c1 >= max(c2,3) or c1 == c2 for c1,c2 in zip(c,w_c))
        return count



    def Regular(self,S):
        return zip(*[ (k,len(list(g))) for k,g in itertools.groupby(S)])

s = Solution()
print(s.expressiveWords(S = "heeellooo",words = ["hello", "hi", "helo"]))


