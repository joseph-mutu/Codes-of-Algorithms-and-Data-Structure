#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-13 17:53:36
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        # 用两个栈，一个存储 mul，一个存储字符串
        strings = []
        res,mul = "",0
        for c in s:
            if c == '[':
                strings.append([res,mul])
                res,mul = "",0
            elif c == ']':
                prev,prev_mul = strings.pop()
                res = prev + res * prev_mul
            elif c in "1234567890":
                mul = mul *10 + int(c)
            else:
                res += c
        return res 

s = Solution()
print(s.decodeString("2[abc]3[cd]ef"))