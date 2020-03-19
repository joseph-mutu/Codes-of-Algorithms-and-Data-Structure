#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-18 15:44:44
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # 找到第一个大于等于 x 的数
        if not arr or not k:
            return []
        elif k >= len(arr):
            return arr
        l,r = 0,len(arr)
        while l < r:
            mid = (l+r)//2
            if arr[mid] < x:
                l = mid +1
            else:
                r = mid
        # r is the index of the first number that > x
        if r == len(arr):
            return arr[len(arr) - k:]
        elif r == 0:
            return arr[:k]
        start,end = r,r
        # start denotes the index of the first number in K closet number to x
        # end denote the index of the last number + 1
        for _ in range(k):
            if start == 0:
                end += 1
            elif end == len(arr):
                start -= 1
            elif abs(arr[start-1] - x) > abs(arr[end] - x):
                end += 1
            else:
                start -= 1
        print(start,end)
        return arr[start:end]

        
s = Solution()
print(s.findClosestElements([1],k = 1,x = 0))
