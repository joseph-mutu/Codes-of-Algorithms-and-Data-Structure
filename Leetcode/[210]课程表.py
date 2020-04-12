#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-12 08:01:10
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
import itertools
class Solution:
    def findOrder(self, numCourses: int, prerequisites) :
        if numCourses<=0:
            return []

        # construct the graph

        graph = collections.defaultdict(set)

        for i in range(numCourses):
            graph[i]
        res = []
        for node1, node2 in prerequisites:
            graph[node2].add(node1)
        no_parent = graph.keys() - set(itertools.chain.from_iterable(graph.values()))

        while no_parent:
            for node in no_parent:
                res.append(node)
                graph.pop(node)
            no_parent = graph.keys() - set(itertools.chain.from_iterable(graph.values()))

        if graph:
            return []

        return res
s = Solution()
print(s.findOrder( 4, [[1,0],[2,0],[3,1],[3,2]]))