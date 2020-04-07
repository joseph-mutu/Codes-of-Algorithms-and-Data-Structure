#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-07 19:42:51
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

class Solution(object):
    def movingCount(self, m, n, k):
        if m <= 0 or n <= 0 or k  == 0:
            return 1
        node_stack = []
        node_stack.append((0,0))

        count = 0
        visited = set()
        visited.add((0,0))
        while node_stack:
            x,y = node_stack.pop(0)
            count += 1
            print(x,y)
            for nx,ny in ((x,y-1),(x-1,y),(x,y+1),(x+1,y)):
                if (nx,ny) not in visited and 0 <= nx < m and 0 <= ny < n and self.check(nx,ny,k):
                    node_stack.append((nx,ny))
                    visited.add((nx,ny))
        return count

    def check(self,x,y,target):
        tem = 0
        while x:
            tem += x%10
            x//=10
        while y:
            tem += y%10
            y//= 10
        return tem <= target
s = Solution()
print(s.movingCount(2,3,1))