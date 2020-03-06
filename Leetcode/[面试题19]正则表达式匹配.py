#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-06 09:44:05
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    # s is the query and p means pattern
    def isMatch(self, s, p):
        # 如果 p 为空 s 也为空，则为 True
        if not p and not s:
            return True
        elif not p:
            return False
        elif not s:
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s,p[2:])
            else:
                return False
        else:   
        # 如果 s 不为空 p 也不为空
            if len(p) > 1 and p[1] == '*':
                if s[0] != p[0] and p[0] != '.':
                    return self.isMatch(s,p[2:])
                else:
                    # 在这种情况下，无论当前字符是否相等，都有两种情况
                    # 可以匹配当前也可以不匹配
                    return self.isMatch(s[1:],p) or self.isMatch(s,p[2:])
            elif p[0] == '.' or p[0] == s[0]:
                return self.isMatch(s[1:],p[1:])
        return False



s = Solution()
print(s.isMatch("aa",".*"))


