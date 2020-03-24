#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-21 14:51:26
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
class Solution(object):
    def validTree(self, n, edges):
        if n < 0:
            return False
        # BFS 
        visited = set()
        #使用邻接表存储图，且图为无向图
        graph = [[0 for _ in range(n)]for _ in range(n)]
        for node1,node2 in edges:
            graph[node1][node2] = 1
            graph[node2][node1] = 1

        node_stack = [0]
        visited.add(0)
        print(graph)
        while node_stack:
            node = node_stack.pop(0)
            for neigh in range(n):
                if graph[node][neigh] == 1:
                    if neigh in visited:
                        return False
                    else:
                        visited.add(neigh)
                        node_stack.append(neigh)
                        graph[neigh][node] = 0
                        graph[node][neigh] = 0
        return len(visited) == n
s = Solution()
print(s.validTree(5,[[0,1],[0,2],[0,3],[1,4]]))
