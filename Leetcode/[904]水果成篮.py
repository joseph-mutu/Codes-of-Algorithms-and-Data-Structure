#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-20 18:26:04
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def totalFruit(self, tree):
        N = len(tree)
        max_len = 0
        # left border
        for i in range(N):
            # right border
            for j in range(i,N):
                tem_len = len(set(tree[i:j+1]))
                if tem_len <= 2 and (j+1-i)  > max_len:
                    max_len = j+1-i
        return max_len

s = Solution()
print(s.totalFruit([0]))