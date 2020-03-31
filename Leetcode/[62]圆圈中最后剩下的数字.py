#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-29 18:41:57
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def lastRemaining(self, n, m):
        pos = 0
        for i in range(2,n+1):
            pos = (pos + (m-1)%i + 1 )%i
        return pos



s = Solution()
print(s.lastRemaining(10,17))

            



