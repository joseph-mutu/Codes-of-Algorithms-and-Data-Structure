#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 19:50:10
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def trap(self, height):
        # 向左扫描找到第一个比自己高的
        # 向右扫描找到第一个比自己高的
        # 两者取 min - 自身
        if not height:
            return 0
        #不包含当前位置的左边第一个高于自身的位置
        dp_left = [0 for i in range(len(height))] 
        # 不包含当前位置的右边第一个高于自身的位置
        dp_right = [0 for i in range(len(height))] 

        for i in range(1,len(height)):
            dp_left[i] = max(dp_left[i-1],height[i-1])
        for i in range(len(height)-2,-1,-1):
            dp_right[i] = max(dp_right[i+1],height[i+1])
        count = 0
        for center in range(1,len(height)-1):
            count += min(max(dp_left[center],height[center]),max(height[center],dp_right[center])) - height[center]
        return count 

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))