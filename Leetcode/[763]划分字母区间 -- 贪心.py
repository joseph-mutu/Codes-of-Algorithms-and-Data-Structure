#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-05 15:31:32
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def partitionLabels(self, S):
        # 记录每个字符串出现的末尾值
        last = {c:i for i,c in enumerate(S)}

        l,r = 0,0
        results = []
        for i,c in enumerate(S):
            r = max(r,last[c])
            if r == i:
                results.append(r-l+1)
                l = r + 1
        return results

s = Solution()
print(s.partitionLabels('ababcbacadefegdehijhklij'))
