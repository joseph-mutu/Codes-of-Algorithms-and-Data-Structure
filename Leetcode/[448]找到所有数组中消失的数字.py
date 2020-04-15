#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-14 16:38:39
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        #首先将数组中的每个数字放到其应该在的地方
        res = []
        #replace nums
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] >= 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
        
        for i,num in enumerate(nums):
            if num > 0:
                res.append(i+1)
        return res

s = Solution()
nums =[4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(nums))