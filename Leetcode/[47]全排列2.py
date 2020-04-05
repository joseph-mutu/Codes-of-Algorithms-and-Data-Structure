#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-04 16:04:17
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def __init__(self):
        self.results = []
        self.visited = []

    def permuteUnique(self, nums):
        if not nums:
            return []
        nums = sorted(nums)
        self.visited = [False] * len(nums)
        self.backtrack(nums,0,[])
        return self.results
    
    def backtrack(self,nums,count,path):
        if count == len(nums):
            self.results.append(path[:])
            return 
        for i in range(len(nums)):
            if not self.visited[i]:
                if i and nums[i]== nums[i-1] and not self.visited[i-1]:
                    continue
                path.append(nums[i])
                self.visited[i] = True
                count += 1
                self.backtrack(nums,count,path)
                path.pop()
                self.visited[i] = False
                count -= 1


s = Solution()
print(s.permuteUnique([2,2,1,1]))
# [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
