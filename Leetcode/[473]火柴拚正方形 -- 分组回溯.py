#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-08 08:24:28
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

    class Solution(object):
        def makesquare(self, nums):
            if not nums or len(nums) < 4:
                return False
            target = sum(nums)
            if target % 4 != 0:
                return False

            side = target // 4
            nums = sorted(nums,reverse = True)

            buckets = [0,0,0,0]
            return self.dfs(nums,side,0,buckets)

        def dfs(self,nums,target,start,buckets):
            if start == len(nums):
                if buckets[0] == buckets[1] == buckets[2] == target:
                    return True
                return False

            for i in range(4):
                if buckets[i] +nums[start] <= target:
                    buckets[i] += nums[start]
                    if self.dfs(nums,target, start + 1, buckets):
                        return True
                    buckets[i] -= nums[start]
                else:
                    continue
            return False

s = Solution()
print(s.makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))


