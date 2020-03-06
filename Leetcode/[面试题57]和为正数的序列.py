#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-05 19:55:49
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def findContinuousSequence(self, target):
        if not target:
            return []
        sum_list = []
        def calculateStep(start):
            n = (-2*start + 1 + (4 * start ** 2 - 4 * start + 1 + 8*target) ** 0.5) * 0.5
            print(n)
            if n.is_integer() and n >= 2:
                return n
            else:
                False

        for i in range(1,int(target/2)+1):
            n = calculateStep(i)
            if n:
                sum_list.append([tem for tem in range(i,i+int(n))])
        return sum_list


s = Solution()
print(s.findContinuousSequence(15))