#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 20:15:36
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        count  = 0
        max_left,max_right = height[0],height[len(height) - 1]
        start,end = 1,len(height) - 2

        count = 0
        while start <= end:
            if max_left < max_right:
                #更新左边
                tem_max = max(max_left,height[start])
                count += tem_max - height[start]
                max_left = tem_max
                start += 1
            else:
                tem_max = max(max_right,height[end])
                count += tem_max - height[end]
                max_right = tem_max
                end -= 1
        return count

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))