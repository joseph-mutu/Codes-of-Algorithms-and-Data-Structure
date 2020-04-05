#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-02 12:57:46
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


import collections 
class Solution(object):
    def findWhetherExistsPath(self, n, graph, start, target):
        # 同时将 start 和 target 入栈

        nodes = [(0,start),(1,target)]

        start_path = set()
        target_path = set()
        start_path.add(start)
        target_path.add(target)

        # construct graph
        connections = collections.defaultdict(set)

        for node1,node2 in graph:
            connections[node1].add(node2)

        while nodes:
            if not start_path.isdisjoint(target_path):
                print(start_path)
                print(target_path)
                return True
            num,node = nodes.pop(0)
            if num == 0:
                start_path.add(node)
            else:
                target_path.add(node)

            for tem_node in connections[node]:
                if num == 0:
                    if tem_node not in start_path:
                        nodes.append((num,tem_node))
                else:
                    if tem_node not in target_path:
                        nodes.append((num,tem_node))
        return False


s = Solution()
graph = [[0, 1], [1, 2], [1, 3], [1, 10], [1, 11], [1, 4], [2, 4], [2, 6], [2, 9], [2, 10], [2, 4], [2, 5], [2, 10], [3, 7], [3, 7], [4, 5], [4, 11], [4, 11], [4, 10], [5, 7], [5, 10], [6, 8], [7, 11], [8, 10]]

print(s.findWhetherExistsPath(12, graph, 2,3))
