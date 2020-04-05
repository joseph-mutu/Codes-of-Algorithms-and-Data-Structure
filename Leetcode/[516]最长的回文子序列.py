#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 14:30:55
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def longestPalindromeSubseq(self, s):
        # 中心扩展
        if not s:
            return 0
        max_length = 0

        for center in range(2*len(s) - 1):
            l = int(center / 2)
            r = l + (center&1)
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r - l + 1 > max_length:
                        max_length = r - l +1
                    l -= 1
                    r += 1
                else:
                    break

        return max_length

s = Solution()
print(s.longestPalindromeSubseq("bbbab"))
