#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-02 17:30:05
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution():
	def isPalindromic(self,s):
		for i in range(int(len(s)/2)):
			if s[i] != s[-(i+1)]:
				return False
		return True
	def longestPalindrome(self, s):
		if 
		length = -1
		palindrome_string = ""
		for i in range(len(s)):
			for j in range(i,len(s)):
				if self.isPalindromic(s[i:j+1]):
					# print(s[i:j+1])
					if len(s[i:j+1]) > length:
						length = len(s[i:j+1])
						palindrome_string = s[i:j+1]
		return palindrome_string

s = Solution()
print(s.longestPalindrome('cbbd'))