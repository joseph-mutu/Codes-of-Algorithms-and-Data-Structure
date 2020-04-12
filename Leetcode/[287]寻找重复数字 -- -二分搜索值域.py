#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-12 20:37:49
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return None
        length = len(nums)
        l,r = 1,length

        while l < r:
            count = 0
            mid = (l + r)//2
            for idx,num in enumerate(nums):
                if num <= mid:
                    count += 1

            if count <= mid:
                l = mid + 1
            else:
                r = mid
        return r





s = Solution()
print(s.findDuplicate([1,2,2,4,5,6,2]))
