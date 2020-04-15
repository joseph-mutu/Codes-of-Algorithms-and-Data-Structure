#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-14 07:53:33
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < k:
            return False

        total = sum(nums)
        target = total/k
        if not target.is_integer():
            return False
        target = int(target)
        print(target)
        nums = sorted(nums,reverse = True)
        return self.backtrack(nums,0,target,k,0,0)

    def backtrack(self,nums,cur_sum,target,match,stat,start):
        if match == 0: 
            return True
        if cur_sum == target:
            return self.backtrack(nums,0,target,match-1,stat,0)

        for i in range(start,len(nums)):
            cur = 1 << i
            if stat & cur == 0 and cur_sum + nums[i] <= target:
                if self.backtrack(nums,cur_sum + nums[i],target,match,stat | cur,i+1):
                    return True
        return False 

s = Solution()
print(s.canPartitionKSubsets([85,35,40,64,86,45,63,16,5364,110,5653,97,95],7))
