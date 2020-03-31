#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-31 14:27:28
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        if not pipes:
            return sum(wells)
        # prime algo

        # denote which nodes are collected
        # dis array denote the distance between the node and the tree
        dis = [float('inf')] * (n+1)
        start = 1
        total_cost = 0

        dis[start] = -1

        # constrct the graph
        graph = [[-1 for _ in range(n+1)]for _ in range(n+1)]

        for idx,cost in enumerate(wells):
            graph[0][idx+1] = cost
            graph[idx+1][0] = cost
        for node1,node2,cost in pipes:
            graph[node1][node2] = cost
            graph[node2][node1] = cost

        # initialize the distance array
        for i in range(n+1):
            if graph[start][i] != -1:

                dis[i] = graph[start][i]
        while 1:
            # find the node with the minimal distance to the spanning tree
            tem_cost = float('inf')
            node = -1
            for i in range(n+1):
                if dis[i] != -1 and dis[i] < tem_cost:
                    tem_cost = dis[i]
                    node = i
            
            if node == -1:
                break
            total_cost += tem_cost
            dis[node] = -1
            # update the distance 
            for i in range(n+1):
                if dis[i] != -1 and graph[node][i] >= 0:
                    if dis[i] > graph[node][i]:
                        dis[i] = graph[node][i]
        return total_cost

s = Solution()
print(s.minCostToSupplyWater(5, [46012,72474,64965,751,33304],[[2,1,6719],[3,2,75312],[5,3,44918]]))

