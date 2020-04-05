#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 18:29:25
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def __init__(self):
        self.results = 0
    def totalNQueens(self, n):
        if not n:
            return 0

        cols,diag,anti_diag = [0] * n,[0] * n*2,[0] * 2*n
        self.backtrack(n,0,cols,diag,anti_diag)
        return self.results


    def backtrack(self,n,row,cols,diag,anti_diag):
        if row == n:
            self.results += 1

        for col in range(n):
            idx1 = row - col + n
            idx2 = row + col

            if cols[col] or diag[idx1] or anti_diag[idx2]:
                continue
            cols[col],diag[idx1],anti_diag[idx2] = 1,1,1
            self.backtrack(n,row+1,cols,diag,anti_diag)
            cols[col],diag[idx1],anti_diag[idx2] = 0,0,0
s = Solution()
print(s.totalNQueens(4))


