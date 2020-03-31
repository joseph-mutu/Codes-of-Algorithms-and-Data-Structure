#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-30 13:46:09
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums or nums is None:
            return None
        self._nums = [0] * len(nums)
        # start from 1
        self.ft = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.update(i,nums[i])
            self._nums[i] = nums[i]
        

    def update(self, i, val):
        pos = i + 1
        delta = val - self._nums[i]
        while pos < len(self.ft):
            self.ft[pos] += delta
            pos += self.lowbit(pos)
        self._nums[i] = val

        
    def lowbit(self,x):
        return x & -x

    def sumRange(self, i, j):
        end = j + 1
        start = i

        sum_end = 0
        while end > 0:
            sum_end += self.ft[end]
            end -= self.lowbit(end)

        sum_start = 0
        while start > 0:
            sum_start += self.ft[start]
            start -= self.lowbit(start)

        return sum_end - sum_start 

s = NumArray([1,3,5])
print(s.ft)
print(s.sumRange(0,2))
s.update(1,2)
print(s.ft)
print(s.sumRange(0,2))