#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-12 07:15:51
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution():

    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit
