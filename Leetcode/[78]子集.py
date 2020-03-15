#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-14 07:30:46
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.fin_set = []
        nums = sorted(nums)
        self.dfs(0,[],nums)
        return self.fin_set

    
    def dfs(self,index,tem_path,nums):
        self.fin_set.append(tem_path[:])
        for j in range(index,len(nums)):
            tem_path.append(nums[j])
            self.dfs(j+1,tem_path,nums)
            tem_path.pop()

s = Solution()
print(s.subsets([1,2,3,3]))