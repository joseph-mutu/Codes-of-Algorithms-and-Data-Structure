#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-02 08:03:15
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


import re
class Solution(object):
    def expressiveWords(self, S, words):
        # 使用正则表达式
        pattern = '^'

        # 记录每单个字符的起始位置
        pos = [idx for idx in range(len(S)) if idx == 0 or S[idx-1]!= S[idx]]
        pos.append(len(S))

        for i in range(1,len(pos)):
            pattern += S[pos[i-1]]

            length = pos[i] - pos[i-1]

            if length < 3:
                pattern += '{'+'{}'.format(length)+'}'
            else:
                pattern += '{'+ '{},{}'.format(1,length) + '}'

        pattern += '$'
        count = 0
        for word in words:
            if re.match(pattern,word):
                count += 1
        return count


s = Solution()
print(s.expressiveWords(S = "heeellooo",words = ["hello", "hi", "helo"]))


