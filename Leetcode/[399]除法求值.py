#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-13 20:38:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
from typing import List
import collections
from heapq import heappush,heappop
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        #construct the graph
        graph = {}
        for (node1,node2),val in zip(equations,values):
            if node1 in graph:
                graph[node1][node2] = val
            else:
                graph[node1] = {node2:val}

            if node2 in graph:
                graph[node2][node1] = 1.0/val
            else:
                graph[node2] = {node1:1.0 / val}
        res = []
        print(graph)
        for node1,node2 in queries:
            if node1 not in graph or node2 not in graph:
                res.append(-1.0)
                continue
            if node1 == node2 and node1 in graph:
                res.append(1.0)
            else:
                ans = self.dijkstra(graph,node1,node2)
                res.append(ans)
        return res

    def dijkstra(self,graph,start,end):
        heap = []
        path = {start : -1}
        for node,val in zip(graph[start].keys(),graph[start].values()):
            heappush(heap,(val,node))
            path[node] = start
        print(start,end,heap)
        collected = set()
        collected.add(start)

        while heap:
            val,node = heappop(heap)
            if node in collected:
                continue
            collected.add(node)

            if node == end:
                break

            for neigh,val in zip(graph[node].keys(),graph[node].values()):
                if neigh not in collected:
                    heappush(heap,(val,neigh))
                    path[neigh] = node
        if end not in path:
            return -1.0
        wei = 1.0
        node = end
        while path[node] != -1:
            wei *= graph[path[node]][node]
            node = path[node]
        return wei

s = Solution()
equa = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]

val = [3.0,4.0,5.0,6.0]
que = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]


print(s.calcEquation(equa,val,que))