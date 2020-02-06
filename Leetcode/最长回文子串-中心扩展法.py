#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-02 18:58:36
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution():
	def longestPalindrome(self, s):
		start = -1
		cur_len = -1
		end = -1
		for i in range(len(s)):
			len1 = self.expandAroundCenter(s,i,i)
			len2 = self.expandAroundCenter(s,i,i+1)
			max_len = max(len1,len2)
			if max_len > cur_len:
				start = i - int((max_len-1)/2)
				end = i + int(max_len/2)
				cur_len = max_len
		return s[start:end+1]


	def expandAroundCenter(self,s,left,right):
		while left >= 0 and right < len(s) and s[left] == s[right]:
			left -= 1
			right += 1
		return right - left - 1

s = Solution()
print(s.longestPalindrome('babad'))