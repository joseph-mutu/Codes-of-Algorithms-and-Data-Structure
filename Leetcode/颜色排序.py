#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-23 07:09:33
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def sortColors(self, nums):
        """
        [0:one_interval) = 0
        [one_interval:i) = 1
        [two_interval:] = 2
        """
        one_interval = 0
        two_interval = len(nums)

        def swap(pos1,pos2):
            nums[pos1],nums[pos2] = nums[pos2],nums[pos1]

        i = 0
        while i < two_interval:
            if nums[i] == 0:
                swap(i,one_interval)
                i+=1 
                one_interval += 1
            elif nums[i] == 1:
                i += 1
            else:
                two_interval -= 1
                swap(i,two_interval)
        return nums

s = Solution()
data =[2,0,2,1,1,0]
s.sortColors(data)


