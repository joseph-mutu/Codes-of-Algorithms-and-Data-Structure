#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-08 11:18:54
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$




class Solution(object):
    def maxCoins(self, nums):

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        nums = [1] + nums + [1]
        n = len(nums)
        # define dp array: the maximal scores after bursting all bullons within i and j
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(1,n-1):
            dp[i][i] = nums[i]*nums[i-1]*nums[i+1]

        for l in range(2,n):
            for s in range(1,n-l):
                e = s + l - 1
                for k in range(s,e+1):
                    # traverse elements within s and e
                    dp[s][e] = max(dp[s][e],dp[s][k-1] + dp[k+1][e] + nums[k]*nums[s-1]*nums[e+1])
        return dp[1][n-2]


s = Solution()
print(s.maxCoins([3,1,5,8]))