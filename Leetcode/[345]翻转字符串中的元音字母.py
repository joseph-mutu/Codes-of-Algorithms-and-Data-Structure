#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-02 10:37:57
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def reverseVowels(self, s):
        if not s:
            return ""
        s_list = list(s)
        pos = [i for i in range(len(s)) if s[i].lower() in 'aeiou']
        
        l,r = 0,len(pos) -1 

        while l < r:
            s_list[pos[l]],s_list[pos[r]] = s_list[pos[r]],s_list[pos[l]]
            r -= 1
            l += 1
        return "".join(s_list)

