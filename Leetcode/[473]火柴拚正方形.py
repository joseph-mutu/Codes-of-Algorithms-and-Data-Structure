#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-08 07:39:37
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
        nums = sorted(nums)

        memo = {}
        return self.backtrack(nums,side,0,0,0,memo)

    def backtrack(self,nums,target,count,tem_sum,stat,memo):

        if str(bin(stat)[2:]).count('1') == len(nums):
            if count == 4:
                return True
            return False

        if stat in memo:

            return memo[stat]

        for i,num in enumerate(nums):
            cur = 1<<i
            if cur & stat != 0:
                continue
            if tem_sum + num < target:
                if self.backtrack(nums,target,count,tem_sum + num,stat | cur,memo):
                    memo[stat] = True
                    return True
            elif tem_sum + num == target:
                if self.backtrack(nums,target,count + 1,0,stat|cur,memo):
                    memo[stat] = True
                    return True
            else:
                break
        memo[stat] = False
        return False

s = Solution()
print(s.makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))
