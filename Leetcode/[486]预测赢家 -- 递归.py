#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-07 15:22:12
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

class Solution(object):
    def PredictTheWinner(self,nums):
        s,e = 0,len(nums)-1
        return self.backtrack(nums,1,s,e) > 0


    def backtrack(self,nums,turn,s,e):
        if s == e:
            return turn * nums[s]
        left = turn*nums[s] + self.backtrack(nums,-turn,s+1,e)
        right = turn * nums[e] + self.backtrack(nums,-turn,s,e-1)
        return turn * max(turn*left,turn*right)


s = Solution()
print(s.PredictTheWinner([1,5,2]))

