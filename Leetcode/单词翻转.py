#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-03 13:39:17
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
	def reverseWords(self, s):
		if not s:
			return ""
		str_list = s.split()
		return ' '.join(str_list[::-1])

s = Solution()
print(s.reverseWords("a good   example"))



