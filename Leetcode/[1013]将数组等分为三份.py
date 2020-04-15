#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-11 10:06:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
from typing import List
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if not A:
            return False
        total = sum(A)
        target = total/3
        if not target.is_integer():
            return False
        tem_sum = 0
        cnt = 0
        for num in A[:-1]:
            tem_sum += num
            if tem_sum == target:
                target *= 2
                cnt += 1
            if cnt == 2:
                return True
        return False

s = Solution()
print(s.canThreePartsEqualSum([1,-1,1,-1]))