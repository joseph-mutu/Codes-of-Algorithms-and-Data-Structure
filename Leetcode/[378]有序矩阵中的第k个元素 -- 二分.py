#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-09 09:14:33
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def kthSmallest(self, matrix, k):
        if not matrix:
            return 0
        n = len(matrix)
        #找出最大值，最小值
        l,r = matrix[0][0],matrix[n-1][n-1]+1
        #第 k 小的值一定在最大值最小值之间，缩减区间的凭据为 mid 数在数组中为 第几大的

        while l < r:
            count = 0
            mid = (l+r) // 2
            for nums in matrix:
                count += self.search_row(nums,mid)
            if count < k:
                l = mid + 1
            else:
                r = mid
        return r

    def search_row(self,nums,target):
        n = len(nums)
        # find the first num that is larget than mid
        l,r = 0,n
        while l < r:
            mid = (l +r)//2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return r
            


s = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
print(s.kthSmallest(matrix,9))