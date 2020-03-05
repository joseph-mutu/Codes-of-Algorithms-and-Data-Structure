#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-05 07:28:23
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import math
class Solution(object):
    def distributeCandies(self, candies, num_people):

        step = int(math.sqrt(2 * candies + 1/4) - 1/2 )

        rows, col = step // num_people , step%num_people 

        distribution = [0] * num_people

        remain_candies = candies - int(step*(1+step)/2)

        for i in range(num_people):

            distribution[i] = rows*(i+1) + int((rows*(rows - 1) * num_people)/2)
            if i < col: 
                distribution[i] += int(rows * num_people + i + 1)
        distribution[col] += remain_candies

        return distribution
s = Solution()
print(s.distributeCandies(90,4))
