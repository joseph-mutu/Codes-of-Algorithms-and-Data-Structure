#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-17 09:29:22
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s:
            return []
        left = 0
        right = len(s) - 1

        while left < right:
            tem =  s[left]
            s[left] = s[right]
            s[right] = tem
            left += 1
            right -= 1
        return s
s = ["h"]

a = Solution()
print(a.reverseString(s))
