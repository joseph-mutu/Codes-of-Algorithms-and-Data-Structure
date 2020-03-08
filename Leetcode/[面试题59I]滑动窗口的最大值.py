#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-07 08:03:32
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums or k < 0:
            return []

        max_deque = []
        left = 0
        right = 0

        index = []

        while right - left + 1 <= k:
            if not max_deque:
                max_deque.append(right)
            else:
                while max_deque and nums[right] > nums[max_deque[-1]]:
                    max_deque.pop()
                max_deque.append(right)
            right += 1
        # 保持滑动窗口的 k 值
        left += 1
        index.append(max_deque[0])
        while right < len(nums):

            while max_deque and right - max_deque[0] >= k:
                max_deque.pop(0)

            while max_deque and nums[right] >= nums[max_deque[-1]]:
                max_deque.pop()

            max_deque.append(right)
            index.append(max_deque[0])
            right += 1
            left += 1
        return [nums[i] for i in index]

s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))





