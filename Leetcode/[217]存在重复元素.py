#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-30 21:11:30
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
class Solution(object):
    def containsDuplicate(self, nums):
        if not nums:
            return False
        count = collections.Counter(nums)
        if max(count.values()) > 1:
            return True

        return False
        
s = Solution()
print(s.containsDuplicate([1,3]))
