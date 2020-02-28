#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-25 20:48:44
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals = sorted(intervals)
        new_internval = []
        for interval in intervals:
            if not new_internval:
                new_internval.append(interval)
                continue

            if interval[0] <= new_internval[-1][1]:
                new_internval[-1][0] = min(interval[0],new_internval[-1][0])
                new_internval[-1][1] = max(interval[1],new_internval[-1][1])
            else:
                new_internval.append(interval)
        return new_internval

s = Solution()
print(s.merge([[2,6],[1,3],[8,10],[15,18]]))