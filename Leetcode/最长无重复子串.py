#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-13 06:42:04
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        lookup = set()

        max_len = 0
        tem_len = 0

        left = 0
        right = -1

        for token in s:
            right += 1
            while token in lookup:
                lookup.remove(s[left])
                left += 1
            lookup.add(token)
            tem_len = right - left + 1
            if tem_len > max_len:
                max_len = tem_len
        return max_len

s = Solution()
data = "pwwkew"
print(s.lengthOfLongestSubstring(data))
