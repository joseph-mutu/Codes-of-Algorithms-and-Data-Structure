#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-28 06:47:44
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):
    def minimumLengthEncoding(self, words):

        if not words:
            return 0

        # 首先对单词进行翻转排序
        words = [word[::-1] for word in words]
        words = sorted(words)

        length = 0
        for i in range(len(words)):
            if i+1 < len(words) and words[i+1].startswith(words[i]):
                continue
            else:
                length += len(words[i]) + 1

        return length

s = Solution()
print(s.minimumLengthEncoding(["time", "me", "bell"]))

