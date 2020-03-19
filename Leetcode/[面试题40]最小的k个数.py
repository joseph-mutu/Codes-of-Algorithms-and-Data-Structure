#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-16 09:04:09
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def getLeastNumbers(self, arr, k):
        # 使用 partition 函数寻 k
        start,end = 0,len(arr) - 1
        index = self.partition(start,end,arr)
        while index != k:
            if index > k:
                end = index - 1
                index = self.partition(start,end,arr)
            elif index < k:
                start = index + 1
                index = self.partition(start,end,arr)
        return arr[:k]

    def partition(self,start,end,arr):
        p = self.median3(start,end,arr)

        l,r = start, end - 1
        print(arr)
        while 1:
            while arr[r] > p:
                r -= 1
            while arr[l] < p:
                l += 1
            if l < r:
                arr[l],arr[r] = arr[r],arr[l]
                l+=1
                r-=1
            else:
                break
        arr[l],arr[end] = arr[end],arr[l]
        return l


    def median3(self,start,end,arr):
        print(start,end)
        l,r = start,end
        mid = (l+r)//2
        # 把 3 个数按照从小到大排列好
        if arr[l] > arr[mid]:
            arr[mid],arr[l] = arr[l],arr[mid]
        if arr[l] > arr[r]:
            arr[l],arr[r] = arr[r],arr[l]
        if arr[mid] > arr[r]:
            arr[r],arr[mid] = arr[mid],arr[r]
        arr[mid],arr[r] = arr[r],arr[mid]
        return arr[r]

s = Solution()
print(s.getLeastNumbers([0,0,2,3,2,1,1,2,0,4],10))