#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 16:12:51
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

from typing import List

import itertools
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return 0
        res = ""
        for prefix in itertools.zip_longest(*strs):
            prefix = set(prefix)
            if len(prefix) == 1:
                res += prefix.pop()
            else:
                break
        return res
s = Solution()
print(s.longestCommonPrefix(["dog","racecar","car"]))

