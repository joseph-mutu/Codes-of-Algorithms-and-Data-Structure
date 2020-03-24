#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-21 16:41:59
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        if not reservedSeats:
            return n*2
        seats = collections.defaultdict(list)
        for line,seat in reservedSeats:
            seats[line].append(seat)
        seats = {item:sorted(seats[item]) for item in seats.keys()}
        family = 0
        for i in range(1,n+1):
            if seats.get(i) is None:
                family += 2
                continue
            print(seats[i],family)
            for j in range(len(seats[i])):
                if j == 0:
                    family += ((seats[i][j] - 1)//4)
                    continue
                family += ((seats[i][j] - seats[i][j-1]-1)//4)
            family += ((11 - seats[i][-1] - 1)//4)
            print(family)
        return family
s = Solution()
print(s.maxNumberOfFamilies(3,[[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))


