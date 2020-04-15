#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 07:18:27
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #维护一个单调栈
        mono_stack = []
        start,end = len(nums),-1
        for idx,num in enumerate(nums):
            while mono_stack and nums[mono_stack[-1]] > num:
                start = min(start,mono_stack.pop())
            mono_stack.append(idx)
        mono_stack.clear()
        for i in range(len(nums)-1,-1,-1):
            while mono_stack and nums[mono_stack[-1]] < nums[i]:
                end = max(end,mono_stack.pop())
            mono_stack.append(i)
        if start > end:
            return 0
        return end - start + 1

s = Solution()
print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
