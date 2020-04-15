#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 14:47:20
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x//10 == 0:
            return True
        # get the length of the integer
        tem = x
        length = 0
        while tem:
            tem//=10
            length += 1
        times = length // 2
        r_x = 0
        mul = pow(10,times-1)
        tem = x
        while times:
            times -= 1

            r_x += mul* (tem%10)
            tem //= 10
            mul /= 10
        if length & 1 == 1:
            tem //= 10
        r_x,tem = int(r_x),int(tem)
        return r_x == tem

s = Solution()
print(s.isPalindrome(10))
