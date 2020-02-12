#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-12 06:42:58
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import sys
class Solution():

    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        
        min_buy = sys.maxsize
        max_pro = -1
        for i in range(len(prices)):
            min_buy = min(min_buy,prices[i])
            max_pro = max(max_pro,prices[i] - min_buy)
        return max_pro

s = Solution()
print(s.maxProfit([7,6,4,3,1]))