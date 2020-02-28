#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-27 07:25:53
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = pow(2,31) - 1
        min_int = -pow(2,31)
        index_0 = 0
        list_x = str(x)
        pos_symbol = 1
        if list_x[0] == '-':
            pos_symbol = -1
            list_x = list_x[1:]
        for i in range(len(list_x)-1,-1,-1):
            if list_x[i] != '0':
                list_x = list_x[i::-1]
                break
        ans = pos_symbol * int("".join(list_x))
        if ans > max_int or ans < min_int:
            return 0
        else:
            return ans

s = Solution()
print(s.reverse(123))

            
