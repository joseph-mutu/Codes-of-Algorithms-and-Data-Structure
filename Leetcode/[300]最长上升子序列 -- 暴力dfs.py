#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-14 08:47:15
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        self.max_length = 0

        for start in range(len(nums)):
            self.dfs(start,[nums[start]],nums[start],nums)
        return self.max_length
    
    def dfs(self,start,path,tem_max,nums):
        if len(path) > self.max_length:
            self.max_length = len(path)
        for cur in range(start + 1,len(nums)):
            if nums[cur] <= tem_max:
                continue
            path.append(nums[cur])
            self.dfs(cur,path,nums[cur],nums)
            path.pop()
        

s = Solution()
print(s.lengthOfLIS([2]))