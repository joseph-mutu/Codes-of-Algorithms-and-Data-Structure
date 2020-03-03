#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-02 20:03:01
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        first = 0
        second = 0

        while second < len(nums):
            if nums[first] == nums[second]:
                second += 1
            else:
                first += 1
                nums[first] = nums[second]
        return first+1

s = Solution()
print(s.removeDuplicates([1,1,2]))
