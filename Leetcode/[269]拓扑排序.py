#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-02 16:12:44
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


import collections 
import itertools
class Solution(object):
    def alienOrder(self, words):
        if not words:
            return ""

        max_len = max(len(word) for word in words)
        #将单词两两比对，只记录第一个不同的字母，将其作为拓扑序,建立单向图
        connections, not_compared = collections.defaultdict(set), [True] * (len(words)-1)

        #单词只比对当前的单词以及当前单词的下一个单词
        for column in itertools.zip_longest(*words):
            for i in range(len(words)-1):
                if column[i] is None or column[i+1] is None:
                    not_compared[i] = False
                if column[i] is not None and (not not_compared[i] or column[i+1] is None):
                    connections[column[i]]
                if not_compared[i] and column[i] != column[i+1]:
                    connections[column[i]].add(column[i+1])
                    not_compared[i] = False
            if column[-1] is not None:
                connections[column[-1]]

        print(connections)
        if len(connections) != 1 and not any(connections.values()):
            return ""

        no_parent,res = connections.keys() - set(itertools.chain.from_iterable(connections.values())),""

        while no_parent:
            for node in no_parent:
                res += node
                connections.pop(node)
            no_parent = connections.keys() - set(itertools.chain.from_iterable(connections.values()))
        print(connections)
        if connections:
            return ""
        return res



s = Solution()
words = ["wrt","wrtkj"]

print(s.alienOrder(words))


                                        