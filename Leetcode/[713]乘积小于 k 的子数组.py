#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-01 10:52:34
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def __init__(self):
        self.results = []
    def numSubarrayProductLessThanK(self, nums, k):
        #递归，遍历所有子集
        for i in range(len(nums)):
            self.backtrack(i,nums,1,k,[])
        return self.results

    
    def backtrack(self,start,nums,product,k,path):
        if product >= k:
            return
        if path: 
            self.results.append(path[:])
        if start == len(nums):
            return 
        path.append(nums[start])
        product *= nums[start]
        print(path,product,start)
        self.backtrack(start+1,nums,product,k,path)
        product /= nums[start]
        path.pop()

s = Solution()
print(s.numSubarrayProductLessThanK([10,5,2,6],100))
