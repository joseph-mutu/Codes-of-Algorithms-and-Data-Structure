#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-03 09:24:40
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def merge(self, A, m, B, n):
        end_A = m - 1
        end_B = n - 1
        # first merge A with B
        end_merge = m+n-1

        while end_A >= 0 or end_B >= 0:
            if end_A == -1:
                A[end_merge] = B[end_B]
                end_B -= 1
            elif end_B == -1:
                A[end_merge] = A[end_A]
                end_A -= 1
            elif A[end_A] >= B[end_B]:
                A[end_merge] = A[end_A]
                end_A -= 1
            elif A[end_A] < B[end_B]:
                A[end_merge] = B[end_B]
                end_B -= 1
            end_merge -= 1
        print(A)
s = Solution()
print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))
