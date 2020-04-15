#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-13 14:26:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

from typing import List
from heapq import heappush,heappop
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        counter = collections.Counter(nums)
        heap = []
        for num,count in zip(counter.keys(),counter.values()):
            heappush(heap,(-count,num))
        
        res = []
        for _ in range(k):
            _,num = heappop(heap)
            res.append(num)
        return res

s = Solution()
print(s.topKFrequent(nums = [1], k = 1))
