#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-13 15:19:18
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False
        counter = collections.Counter(nums)
        need = collections.Counter()

        for num in nums:
            if counter[num] == 0:
                continue
            elif need[num] > 0:
                need[num] -= 1
                need[num+1] += 1
            elif counter[num+1] > 0 and counter[num+2] > 0:
                counter[num+1],counter[num+2] = counter[num+1] - 1,counter[num+2]-1
                need[num+3] += 1
            else:
                return False
            counter[num] -= 1
        return True
