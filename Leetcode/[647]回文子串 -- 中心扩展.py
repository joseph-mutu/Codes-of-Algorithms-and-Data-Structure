#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 06:48:06
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

class Solution(object):
    def countSubstrings(self, s):
        if not s:
            return 0
        count = 0

        for center in range(2*len(s) - 1):
            left = int(center/2)
            right = left + (center&1)

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
        return count

s = Solution()
print(s.countSubstrings("abc"))
