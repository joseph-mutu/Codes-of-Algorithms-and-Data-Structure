#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-05 15:11:28
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
class Solution(object):
    def partitionLabels(self, S):
        if not S:
            return []
        total = collections.Counter(S)
        l,r = 0,0
        results = []

        counter = collections.Counter()
        target = 0
        match = 0
        while r < len(S):
            if counter[S[r]] == 0:
                target += 1
            counter[S[r]] += 1
            if counter[S[r]] == total[S[r]]:
                match += 1
            if match and target == match:
                results.append(r - l + 1)
                l = r+1
                counter = collections.Counter()
                target = 0
                match = 0
            r += 1
        return results

s = Solution()
print(s.partitionLabels('ababcbacadefegdehijhklij'))


