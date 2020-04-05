#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 15:17:11
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def minAreaRect(self, points):
        if not points:
            return 0

        points_hash = set(map(tuple,points))

        area = float('inf')

        for idx1,p1 in enumerate(points):
            for idx2 in range(idx1):
                p2 = points[idx2]

                if p2[0] != p1[0] and p2[1] != p1[1] and \
                (p1[0],p2[1]) in points_hash and \
                (p2[0],p1[1]) in points_hash:
                    tem_area = abs(p2[0] - p1[0]) * abs(p2[1] - p1[1])
                    if tem_area < area:
                        area = tem_area
        return area

s = Solution()
print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))
