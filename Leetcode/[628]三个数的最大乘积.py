#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-08 06:46:15
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def maximumProduct(self, nums):
        big = []
        small = []

        for i,num in enumerate(nums):
            # 维护最大的三个值
            if len(big)<3:
                big.append(num)
            elif len(big) == 3:
                if big[0] > big[1]:
                    big[0],big[1] = big[1],big[0]
                if big[1] > big[2]:
                    big[1],big[2] = big[2],big[1]
                if big[0] > big[1]:
                    big[0],big[1] = big[1],big[0]
                if num > big[2]:
                    big.append(num)
                    big.pop(0)
                elif big[1] < num <= big[2]:
                    big[0] = big[1]
                    big[1] = num
                elif big[0] < num <= big[1]:
                    big[0] = num
            if len(small) < 2:
                small.append(num)
            elif len(small) == 2:
                if small[0] > small[1]:
                    small[0],small[1] = small[1],small[0]
                if num < small[0]:
                    small[1] = small[0]
                    small[0] = num
                elif num >= small[0] and num <small[1]:
                    small[1] = num
        max_1 = big[0] * big[1] *big[2]
        max_2 = big[2] * small[0] *small[1]

        return max(max_1,max_2)
s = Solution()
print(s.maximumProduct([1,2,3,4,-2,-3,6]))
