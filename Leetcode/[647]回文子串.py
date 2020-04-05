#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-02 20:37:24
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):
    def __init__(self):
        self.results = 0
    def countSubstrings(self, s):
        if not s:
            return 0
        for start in range(len(s)):
            self.backtrack(start,s,[])
        return self.results
    
    def backtrack(self,start,string,path):
        if start == len(string):
            return
        path.append(string[start])
        if self.check(path):
            print(path)
            self.results += 1
        self.backtrack(start + 1,string,path)
        path.pop()
        
    
    def check(self,string):
        # check if the string is plaindromic 
        if string == string[::-1]:
            return True
        return False
s = Solution()
print(s.countSubstrings("aaaa"))