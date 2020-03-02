#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-01 10:26:35
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def __init__(self):
        self.permutation = []

    def permute(self, nums):
        if not nums:
            return []

        self.permute_act(0,nums)
        return self.permutation


    def permute_act(self,start,nums):
        if start ==  len(nums):
            self.permutation.append(nums[:])
            return 

        for pos in range(start+1,len(nums)):
            nums = self.swap(start,pos,nums)
            self.permute_act(start + 1,nums)
            nums = self.swap(start,pos,nums)

    def swap(self,pos1,pos2,nums):
        tem = nums[pos1]
        nums[pos1] = nums[pos2]
        nums[pos2] = tem
        return nums

s = Solution()
print(s.permute([1,2,3]))