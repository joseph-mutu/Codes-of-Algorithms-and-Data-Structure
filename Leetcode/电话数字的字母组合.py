#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-11 07:21:53
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution():
    def __init__(self):

        self.lookup = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],\
        '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],\
        '9':['w','x','y','z']}
        self.fin_comb = []

    def letterCombinations(self, digits):
        if not digits:
            return []

        comb_cand = []

        for dig in digits:
            if dig == '1':
                continue
            tem = self.lookup.get(dig,"{} is not allowed".format(dig))
            comb_cand.append(tem)
        if comb_cand:
            self.combine(comb_cand,[])
        return self.fin_comb

    def combine(self,comb_cand,cur_comb):
        if not comb_cand:
            self.fin_comb.append("".join(cur_comb[:]))
            return
        for term in comb_cand[0]:
            cur_comb.append(term)
            self.combine(comb_cand[1:],cur_comb)
            cur_comb.pop()
        return
s = Solution()
print(s.letterCombinations("1111"))





