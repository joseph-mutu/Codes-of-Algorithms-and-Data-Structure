#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-13 16:20:36
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0]
        cnt = 0
        while cnt != n:
            length = len(res)
            for i in range(length-1,-1,-1):
                num = res[i] | 1 << cnt
                res.append(num)
            cnt += 1
        return res

s = Solution()
print(s.grayCode(3))