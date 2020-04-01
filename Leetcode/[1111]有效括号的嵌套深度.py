#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-01 15:49:01
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def maxDepthAfterSplit(self, seq):
        if not seq:
            return []
        labels = [0] *len(seq)
        depth = 0
        for idx, paren in enumerate(seq):
            if paren == '(':
                depth += 1
                labels[idx] = depth & 1
            elif paren == ')':
                
                labels[idx] = depth & 1
                depth -= 1

        return labels

s = Solution()
print(s.maxDepthAfterSplit("()(())()"))


