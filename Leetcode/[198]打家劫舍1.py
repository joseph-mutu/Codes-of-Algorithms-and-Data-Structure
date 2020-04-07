#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-07 18:12:14
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$l



class Solution(object):
    def rob(self, nums):
        #使用搜索
        memo = {}
        return self.backtrack(0,nums,memo)

    def backtrack(self,start,nums,memo):
        if start >= len(nums):
            return 0
        if start in memo:
            return memo[start]

        first = self.backtrack(start+1,nums,memo)
        second = self.backtrack(start +2 ,nums,memo) + nums[start]
        memo[start] = max(first,second)

        return memo[start]
s = Solution()
print(s.rob([2,7,9,3,1]))