#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-05 07:12:28
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

# 暴力解法，模拟糖果分发过程
class Solution(object):
    def distributeCandies(self, candies, num_people):
        if candies <= 0 or num_people <= 0:
            return [0 for _ in range(num_people)]

        distribution = [0 for _ in range(num_people)]
        i = 1

        while candies:
            distribution[(i%num_people) - 1] += i
            candies -= i
            i += 1
            if candies <= i:
                distribution[(i%num_people)-1] += candies
                break
        return distribution

s = Solution()
print(s.distributeCandies(10,3))