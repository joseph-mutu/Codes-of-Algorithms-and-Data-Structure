#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-15 06:41:38
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        max_len = 0
        # 使用二分法找到第一个大于等于当前 house 数目的 heater
        for house in houses:
            l,r = 0,len(heaters) - 1
            while l < r:
                mid = (l+r)//2
                if heaters[mid] < house:
                    l = mid + 1
                else:
                    r = mid
            if heaters[r] <= house:
                tem_length = abs(heaters[r] - house)
            elif heaters[r] > house:
                if r > 0:
                    tem_length = min(abs(heaters[r] - house), abs(heaters[r-1]-house))
                else:
                    tem_length = abs(heaters[0] - house)
            if tem_length > max_len:
                max_len = tem_length   
        return max_len         

                
s  = Solution()
print(s.findRadius([1,2,3,4],[1,4]))
