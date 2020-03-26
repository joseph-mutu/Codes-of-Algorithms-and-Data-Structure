#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-26 19:57:33
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
class Solution(object):
    def hasGroupsSizeX(self, deck):
        card = collections.Counter(deck)

        # 求 n 个数的最大公约数
        if self.gcdN(list(card.values())) < 2:
            return False
        return True

    def gcdN(self,nums):
        if len(nums) == 1:
            return nums[0]
        return gcd(nums[len(nums) - 1], gcdN(nums[0:-1]))

    def gcd(self,num1,num2):
        if num2 == 0:
            return num1
        return self.gcd(num2,num1%num2)

s = Solution()
print(s.hasGroupsSizeX( [1,2,3]))
