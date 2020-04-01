#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-01 18:16:20
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def findLength(self, A, B):
        # 暴力
        A = "".join([str(x) for x in A])
        B = "".join([str(x) for x in B])
        length = 0
        for i in range(len(A)-1):
            for j in range(1,len(A)+1):
                if A[i:j] in B:
                    if j - i > length:
                        print(A[i:j])
                        length = j - i
        return length


s = Solution()
print(s.findLength([0,1,1,1,1],[1,0,1,0,1]))
