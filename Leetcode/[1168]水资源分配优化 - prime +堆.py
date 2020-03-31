#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-31 15:36:06
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
from heapq import heappop,heappush
class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):

        #prime + heap

        # denote nodes that are collected in the tree
        collected = set()

        total_cost = 0

        #construct the graph
        graph = collections.defaultdict(list)
        for idx,cost in enumerate(wells):
            graph[0].append((cost,idx+1))
            graph[idx+1].append((cost,0))
        for node1,node2,cost in pipes:
            graph[node1].append((cost,node2))
            graph[node2].append((cost,node1))

        heap = []

        #push the distance from the node to the spanning tree
        heappush(heap,(0,1))

        while heap:
            cost, target = heappop(heap)
            if target in collected:
                continue

            collected.add(target)
            total_cost += cost
            print(collected,total_cost)
            #update the distance from nodes to the tree and push
            for cost,node in graph[target]:
                if node not in collected:
                    heappush(heap,(cost,node))

        return total_cost
s = Solution()
print(s.minCostToSupplyWater(5, [46012,72474,64965,751,33304],[[2,1,6719],[3,2,75312],[5,3,44918]]))

