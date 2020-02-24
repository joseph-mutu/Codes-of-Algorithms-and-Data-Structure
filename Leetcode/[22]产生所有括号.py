#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-24 07:03:49
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):

    def __init__(self):
        self.ans_list = []
        self.tem_list = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n is not None:
            self.dfs(n,n)
        return self.ans_list

    def dfs(self,left,right):
        if left == 0 and right == 0:
            self.ans_list.append("".join(self.tem_list[:]))
            return
        if left > right:
            return 
        if left > 0:
            self.tem_list.append('(')
            left -= 1
            self.dfs(left, right)
            left += 1
            self.tem_list.pop()
        if right > 0:
            self.tem_list.append(')')
            right -= 1
            self.dfs(left,right)
            right += 1
            self.tem_list.pop()
        return

s = Solution()
print(s.generateParenthesis(3))