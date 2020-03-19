#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-18 20:24:30
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
        # 直接搜寻最优边界的左边界
        if not arr or not k:
            return []
        l,r = 0,len(arr) - k
        while l < r:
            mid = (l+r)//2
            if x-arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[r:r+k]