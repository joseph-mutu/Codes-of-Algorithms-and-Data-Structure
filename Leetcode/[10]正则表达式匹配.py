#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-06 06:51:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def isMatch(self, s, p):

        if not s and not p:
            return True
        if s and not p:
            return False

        if not s:
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s,p[2:])
            else:
                return False
        if s:
            if len(p) > 1 and p[1] == '*':
                if s[0] != p[0] and p[0] != '.':
                    return self.isMatch(s,p[2:])
                else:
                    #匹配当前字符或者直接不匹配当前字符
                    return self.isMatch(s[1:],p) or self.isMatch(s,p[2:])
            elif s[0] == p[0] or p[0] == '.':
                return self.isMatch(s[1:],p[1:])
        return False

s = Solution()
print(s.isMatch("aaa","a*a"))

