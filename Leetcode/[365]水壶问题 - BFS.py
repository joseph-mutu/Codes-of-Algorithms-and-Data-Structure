#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-21 09:34:14
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def canMeasureWater(self, x, y, z):
        if z < 0:
            return False
        if x == z or y == z or x + y == z:
            return True
        state = set()
        # starts from 0,0
        bfs_stack = [(0,0)]
        state.add((0,0))
        while bfs_stack:

            nx,ny = bfs_stack.pop(0)
            if nx == z or ny == z or nx + ny == z:
                return True

            # generate neighbours 

            # empty actions
            if (0,ny) not in state:
                bfs_stack.append((0,ny))
                state.add((0,ny))
            if (nx,0) not in state:
                bfs_stack.append((nx,0))
                state.add((nx,0))

            # fill actions
            if (x,ny) not in state:
                bfs_stack.append((x,ny))
                state.add((x,ny))
            if (nx,y) not in state:
                bfs_stack.append((nx,y))
                state.add((nx,y))

            # pour water from one to another
            # pour from y to x
            if x - nx >= nx + ny and (nx+ny,0) not in state:
                bfs_stack.append((nx+ny,0))
                state.add((nx+ny,0))
            elif x - nx < nx + ny and (x,ny-(x-nx)) not in state:
                bfs_stack.append((x,ny - (x-nx)))
                state.add((x,ny-(x-nx)))
            
            # pour from x to y
            #  if the water in x is not enough to fill y
            if y - ny >= nx + ny and (0,nx+ny) not in state:
                bfs_stack.append((0,nx+ny))
                state.add((0,nx+ny))
            # if the water in x is too much to fill y
            elif y - ny < nx + ny and (x - (y-ny),y) not in state:
                bfs_stack.append((x - (y-ny),y))
                state.add((x - (y-ny),y))
        return False

s = Solution()
print(s.canMeasureWater(2,6,5))

