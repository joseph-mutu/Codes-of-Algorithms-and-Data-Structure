#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-20 17:56:17
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return None
        return self.partition(0,len(nums) - 1,nums)
    def partition(self,s,e,nums):
        # s is the start index of the array
        # e is the ending index of the array
        if s == e:
            return nums[s]
        mid = (s+e)//2
        # left_max is [s,mid]
        left_max = self.partition(s,mid,nums)
        # right_max is (mid,e]
        right_max = self.partition(mid + 1,e,nums)

        # search the max sequence passing through the middle
        # from [s,mid]
        left_tem_sum = 0
        left_max_sum = float('-inf')
        left = mid
        while left >= s:
            left_tem_sum += nums[left]
            left -= 1
            if left_tem_sum > left_max_sum:
                left_max_sum = left_tem_sum
        # from (mid,e]
        right = mid + 1
        right_tem_sum = 0
        right_max_sum = float('-inf')
        while right <= e:
            right_tem_sum += nums[right]
            if right_tem_sum > right_max_sum:
                right_max_sum = right_tem_sum
            right += 1
        mid_max = right_max_sum + left_max_sum

        return max(left_max,right_max,mid_max)