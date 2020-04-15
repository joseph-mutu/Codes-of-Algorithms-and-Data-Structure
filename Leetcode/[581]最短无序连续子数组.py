#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-14 20:07:34
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

from heapq import heappop,heappush
from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heap = []
        for num in nums:
            heappush(heap,num)
        pos = 0
        rank = {}
        while heap:
            rank[heappop(heap)] = pos
            pos += 1
        print(rank)
        start,end = -1,-1
        for idx,num in enumerate(nums):
            if idx != rank[num]:
                if start == -1:
                    start = idx
                else:
                    end = idx
        return end - start + 1
s = Solution()
print(s.findUnsortedSubarray([1,1,1,0,1]))