#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-05 09:29:56
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        if len(sweetness)  == K+1:
            return min(sweetness)

        # use binary search to search for the solution
        l,r = 1,sum(sweetness) // (K+1)+1
        while l < r-1:
            mid = (l+r)//2
            if self.is_valid(sweetness,mid,K):
                l = mid
            else:
                r = mid
        return l

    def is_valid(self,sweetness,val,k):
        count = 0
        s = 0
        for i in sweetness:
            s += i
            if s >= val:
                s = 0
                count += 1
        if count < k+1:
            return False
        return True

s = Solution()
print(s.maximizeSweetness( [1,2,2,1,2,2,1,2,2],2))

