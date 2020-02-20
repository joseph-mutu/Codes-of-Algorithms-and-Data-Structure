#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-19 20:31:49
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        start = []
        end = []

        room_max = float('-inf')

        for i,j in intervals:
            start.append(i)
            end.append(j)
        start.sort()
        end.sort()

        cur_num = 0

        start_point = 0
        end_point = 0
        while start_point < len(intervals) and end_point < len(intervals):
            if start[start_point] < end[end_point]:
                # 表示当前为 开始时间
                cur_num += 1
                start_point += 1
            else:
                # 表示当前为结束时间
                cur_num -= 1
                end_point += 1
            if cur_num > room_max:
                room_max = cur_num
        return room_max


        
