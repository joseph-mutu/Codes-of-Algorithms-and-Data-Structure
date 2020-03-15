#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-14 18:14:13
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
        fin_list = []
        for s in S:

            if s.isalpha():
                if not fin_list:
                    fin_list.append(s.upper())
                    fin_list.append(s.lower())
                else:
                    n = len(fin_list)
                    for i in range(n):
                        fin_list.append(fin_list[i] + s.upper())
                        fin_list[i] += s.lower() 
            else:
                if not fin_list:
                    fin_list.append(s)
                else:
                    n = len(fin_list)
                    for i in range(n):
                        fin_list[i] += s
        return fin_list

s = Solution()
print(s.letterCasePermutation("3z4"))