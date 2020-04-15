#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 15:10:05
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x//10 == 0:
            return True
        if x < 0 or x%10 == 0:
            return False
        r_x = 0
        while x > r_x:
            r_x = r_x*10 + x%10
            x //= 10
        print(r_x,x)
        return x == int(r_x) or x == int(r_x//10)
s = Solution()
print(s.isPalindrome(10))
