#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 14:05:36
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        #维护一个单调递减栈
        res = [0]
        temp = [len(T)-1]
        for i in range(len(T)-2,-1,-1):
            while temp and T[i] >= T[temp[-1]]:
                temp.pop()
            if not temp:
                res.append(0)
            else:
                res.append(temp[-1]-i)
            temp.append(i)
        return res[::-1]
s = Solution()
print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))


