#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-12 07:32:49
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import collections
import itertools
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        if not prerequisites or numCourses <= 0:
            return True

        # construct the grad
        #using set to avoid redundant connections
        graph = collections.defaultdict(set)

        for node1,node2 in prerequisites:
            graph[node1].add(node2)

        no_parent = graph.keys() - set(itertools.chain.from_iterable(graph.values()))
        while no_parent:
            for node in no_parent:
                graph.pop(node)
            no_parent = graph.keys() - set(itertools.chain.from_iterable(graph.values()))

        if graph:
            return False
        return True


s = Solution()
print(s.canFinish(2,[[1,0],[0,1]]))