#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-15 07:54:07
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        pos = -1
        min_num,max_num = float('inf'),float('-inf')

        for idx,num in enumerate(nums):
            # 找到最小的需要



