#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 10:48:01
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import collections 
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        n_buckets = counter.most_common(1)[0][1] - 1
        print(counter)
        last_bucket_size =  sum([1 for cnt in counter.values() if cnt - n_buckets > 0 ])
        cost = n_buckets * (n+1) + last_bucket_size
        return max(cost,len(tasks))

s = Solution()
print(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))