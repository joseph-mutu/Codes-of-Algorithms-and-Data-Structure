#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-21 15:36:49
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        if not arr2:
            return len(arr1)
        if not arr1:
            return 0
        arr2 = sorted(arr2)
        n_com = 0
        for num in arr1:
            l,r = 0,len(arr2)
            while l < r:
                mid = (l + r)//2
                if arr2[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            if r == len(arr2):
                if abs(arr2[-1] - num) > d:
                    n_com += 1
            elif r == 0:
                if abs(arr2[0] - num) > d:
                    n_com += 1
            else:
                if abs(arr2[r-1] - num) > d and abs(arr2[r] - num) > d:
                    n_com += 1
        return n_com

s = Solution()
print(s.findTheDistanceValue([1,4,2,3],  [-4,-3,6,10,20,30],  3))

