#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-10 10:18:49
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if k >= len(nums):
            return [max(nums)]
        max_stack = []

        res = []

        for idx,num in enumerate(nums):
            # 保证数组头部元素永远在 k 的区间内
            if max_stack and idx - max_stack[0] + 1 > k:
                max_stack.pop(0)
            if not max_stack or num <= nums[max_stack[-1]]:
                max_stack.append(idx)

            if num > nums[max_stack[-1]]:
                while max_stack and num > nums[max_stack[-1]]:
                    max_stack.pop()
                max_stack.append(idx)

            if idx >= k-1:
                res.append(nums[max_stack[0]])
        return res
s = Solution()
nums = [1,3,1,2,0,5]
k = 3
print(s.maxSlidingWindow(nums,k))
