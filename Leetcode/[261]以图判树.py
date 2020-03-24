#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-21 14:25:41
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution(object):
    def validTree(self, n, edges):
        # union d
        uf = {i:-1 for i in range(n)}
        n_com = 0 # number of components
        is_circle = False

        def union(node1,node2,is_circle):
            father1 = find(node1)
            father2 = find(node2)
            if father1 == father2:
                is_circle = True
                return is_circle
            # path compression 
            if uf[father1] <= uf[father2]:
                uf[father1] += uf[father2]
                uf[father2] = father1 
                uf[node2] = father1
            else:
                uf[father2] += uf[father1]
                uf[father1] = father2
                uf[node1] = father2
            return is_circle
        def find(node):
            while uf[node] >= 0:
                node = uf[node]
            return node

        for node1,node2 in edges:
            is_circle = union(node1,node2,is_circle)
            if is_circle:
                return False
        if not is_circle:
            for node in uf:
                if uf[node] < 0:
                    n_com +=1
            if n_com > 1:
                return False
        return True
s = Solution()
print(s.validTree(5,[[0,1],[0,2],[0,3],[1,4]]))
