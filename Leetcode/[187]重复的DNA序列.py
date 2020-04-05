#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-01 20:49:10
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os



class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if not s or len(s) < 10:
            return []
        # 使用滑动窗口，并开辟一个字典记录子串

        record = {}
        l,r = 0,10

        results = set()

        while r < len(s):

            r += 1

            if r - l == 10:
                if s[l:r] in record:
                    results.add(s[l:r])
                else:
                    record[s[l:r]] = 1
                l += 1
        return list(results)

s = Solution()
print(s.findRepeatedDnaSequences("AAAAAAAAAAAA"))