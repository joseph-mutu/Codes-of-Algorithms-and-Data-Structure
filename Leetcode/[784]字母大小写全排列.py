#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-14 18:04:48
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return []
        self.fin_list = []
        self.dfs(S,[])
        return self.fin_list

    
    def dfs(self,S,tem_path):
        if not S:
            self.fin_list.append("".join(tem_path[:]))
            return
        if S[0] in "1234567890":
            tem_path.append(S[0])
            self.dfs(S[1:],tem_path)
            tem_path.pop()
        else:
            tem_path.append(S[0].lower())
            self.dfs(S[1:],tem_path)
            tem_path.pop()
            tem_path.append(S[0].upper())
            self.dfs(S[1:],tem_path)
            tem_path.pop()
        return  
s = Solution()
print(s.letterCasePermutation("12345"))