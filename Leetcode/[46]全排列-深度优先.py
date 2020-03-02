#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-01 13:57:03
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

class Solution(object):
    def permute(self, nums):
        visited = [False for _ in range(len(nums))]
        tem_path = []
        permutation = []

        def dfs(depth):
            if depth == len(nums):
                permutation.append(tem_path[:])

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    tem_path.append(nums[i])
                    dfs(depth + 1)
                    tem_path.pop()
                    visited[i] = False
        dfs(0)

        return permutation

s = Solution()
print(s.permute([1,2,3]))