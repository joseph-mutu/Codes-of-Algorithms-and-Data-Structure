#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-04 09:30:12
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def wallsAndGates(self, rooms):
        if not rooms:
            return rooms



        node_list = []

        row_len = len(rooms)
        col_len = len(rooms[0])

        for i in range(row_len):
            for j in range(col_len):
                if rooms[i][j] == 0:
                    node_list.append([i,j,1])

        def neighbour(x,y):

            for new_x,new_y in ((x-1,y),(x,y+1),(x+1,y),(x,y-1)):
                if 0 <= new_x and new_x < row_len and 0 <= new_y and new_y < col_len:
                    yield new_x,new_y

        while node_list:

            x,y,dis = node_list.pop(0)

            for new_x,new_y in neighbour(x,y):
                if rooms[new_x][new_y] != -1 and dis < rooms[new_x][new_y]:
                    rooms[new_x][new_y] = dis
                    node_list.append([new_x,new_y,dis + 1])

        print(rooms)

s = Solution()
INF = 2147483647

data = [[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]

print(s.wallsAndGates(data))



