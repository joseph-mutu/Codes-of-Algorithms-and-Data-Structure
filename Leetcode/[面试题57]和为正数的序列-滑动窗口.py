#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-05 20:42:24
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def findContinuousSequence(self, target):
        # 使用滑动窗口进行求解
        # 在任意时间段，滑动窗口的左右边界都只能向右移动
        if target < 0:
            return []

        left = 1
        right = 1
        ans_list = []

        tem_sum = left

        while left <= target//2:
            if tem_sum == target:
                ans_list.append([i for i in range(left,right + 1)])
                tem_sum -= left
                left += 1
            elif tem_sum > target:
                tem_sum -= left
                left += 1
            elif tem_sum < target:
                right += 1
                tem_sum += right
        return ans_list

s = Solution()
print(s.findContinuousSequence(15))