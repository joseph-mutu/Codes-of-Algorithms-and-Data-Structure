#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-31 14:01:32
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
from heapq import heappush,heappop
class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        if not pipes:
            return sum(wells)
        
        # construct the graph
        total_cost = 0

        edges = []

        for idx,well in enumerate(wells):

            heappush(edges,(well,0,idx+1))
        for node1,node2,cost in pipes:

            heappush(edges,(cost,node1,node2))

        # union_find set to check the tree
        parent = [-1] * (n+1)
        edge_count = 0
        while edges and edge_count != n:
            cost,node1,node2 = heappop(edges)
            print(node1)
            root1 = self.find_root(parent,node1)
            root2 = self.find_root(parent,node2)

            #造成回路，drop
            if root1 == root2:
                continue

            edge_count += 1
            total_cost += cost
            # collect the edge
            if parent[root1] < parent[root2]:
                parent[root1] += parent[root2]
                parent[root2] = root1
                parent[node2] = root1
            else:
                parent[root2] += parent[root1]
                parent[root1] = root2
                parent[node1] = root2

        return total_cost

    def find_root(self,parent,node):
        # union_find using path compression
        if parent[node] < 0:
            return node
        parent[node] = self.find_root(parent,parent[node])
        return parent[node]

s = Solution()
print(s.minCostToSupplyWater(5, [46012,72474,64965,751,33304],[[2,1,6719],[3,2,75312],[5,3,44918]]))

