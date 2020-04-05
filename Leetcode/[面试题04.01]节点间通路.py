#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-02 11:49:50
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections 
class Solution(object):
    def findWhetherExistsPath(self, n, graph, start, target):
        if not graph:
            return False

        # mark which node are collected 
        collected = set()
        nodes = []
        nodes.append(start)

        # construct the graph
        connections = collections.defaultdict(set)
        for node1,node2 in graph:
            connections[node1].add(node2)

        while nodes:
            node = nodes.pop(0)
            collected.add(node)

            if target in collected:
                return True

            for city in connections[node]:
                if city not in collected:
                    nodes.append(city)
        return False

s = Solution()
graph = [[0, 1], [0, 4], [0, 12], [1, 2], [1, 3], [1, 5], [2, 10], [3, 13], [5, 6], [5, 8], [5, 9], [5, 19], [6, 7], [8, 11], [8, 14], [10, 16], [11, 15], [12, 14], [14, 17], [14, 18]]
print(s.findWhetherExistsPath(20, graph, 8,11))