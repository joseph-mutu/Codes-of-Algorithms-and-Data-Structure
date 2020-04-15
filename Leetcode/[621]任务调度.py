#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 09:41:09
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = [0] *26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        freq.sort(reverse = True)

        count = len(tasks)
        cost = 0
        while 1:
            pos = 0
            for epoc in range(n+1):
                if count == 0:
                    return cost
            
                cost += 1
                if freq[pos] == 0:
                    continue
                freq[pos] -= 1
                pos += 1

                count -= 1
            freq.sort(reverse = True)

s  = Solution()
print(s.leastInterval(["A","A","A","B","B","B"],n= 2))
