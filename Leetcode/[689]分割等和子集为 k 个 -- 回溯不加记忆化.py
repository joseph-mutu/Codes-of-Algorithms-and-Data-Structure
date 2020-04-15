#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-14 11:59:14
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < k:
            return False

        total = sum(nums)
        target = total/k
        if not target.is_integer():
            return False
        target = int(target)
        nums = sorted(nums)
        memo = {}
        buckets = [0] * k

        return self.backtrack(nums,buckets,target,0)

    def backtrack(self,nums,buckets,target,match):
        if not nums and match == len(buckets):
            return True
        elif not nums:
            return False
        num = nums.pop()
        for i in range(len(buckets)):
            if buckets[i] + num <= target:
                buckets[i] += num
                if buckets[i] == target:
                    match += 1
                if self.backtrack(nums,buckets,target,match):
                    return True
                if buckets[i] == target:
                    match -= 1
                buckets[i] -= num
                
        nums.append(num)
        return False 9