#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-14 20:42:39
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
        if not heaters:
            return 0
        max_len = 0
        for house in houses:
            cur_heater = 0
            while cur_heater <= len(heaters)-2 and abs(heaters[cur_heater] - house) >= abs(heaters[cur_heater+1] - house):
                cur_heater += 1
            # 如果下一个加热器的距离比当前加热器距离当前house 的距离大
            # 当前加热器为最近的加热器
            if max_len < abs(heaters[cur_heater] - house):
                max_len = abs(heaters[cur_heater] - house)
        return max_len
                
s = Solution()
print(s.findRadius([1,2,3,4],[1,4]))
