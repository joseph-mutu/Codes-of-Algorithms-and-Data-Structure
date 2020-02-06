#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-12 07:24:56
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def maxSubArray(self, nums):
		if not nums:
			return None
		return self.divide(nums,0,len(nums)-1)

	def divide(self,nums,left,right):
		if left == right:
			return nums[left]

		leftBorderSum = float('-inf')
		leftBorderTem = 0
		rightBorderSum = float('-inf')
		rightBorderTem = 0

		mid = int((left + right) / 2) 

		leftMaxSum = self.divide(nums,left,mid)
		rightMaxSum = self.divide(nums,mid + 1,right)

		for i in range(mid,left-1,-1):
			leftBorderTem += nums[i]
			if leftBorderSum < leftBorderTem:
				leftBorderSum = leftBorderTem

		for i in range(mid+1,right+1):
			rightBorderTem += nums[i]
			if rightBorderSum < rightBorderTem:
				rightBorderSum = rightBorderTem

		return max(leftBorderSum+rightBorderSum,max(leftMaxSum,rightMaxSum))


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))