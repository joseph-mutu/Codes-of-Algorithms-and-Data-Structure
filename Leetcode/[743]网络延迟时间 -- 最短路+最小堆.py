#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-27 19:56:54
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

from heapq import heapify,heappop,heappush,heapreplace

class Solution(object):
    def __init__(self):
        self.collected = set()
        self.dis = []

    def networkDelayTime(self, times, N, K):
        K = K - 1
        self.dis = [float('inf')]*N
        # build the graph using the adjencent matrix
        graph = [[-1 for _ in range(N)]for _ in range(N)]
        for node1,node2,w in times:
            graph[node1-1][node2-1] = w

        # initialization
        # self.collected.add(K)
        self.dis[K] = 0
        heap = []
        heappush(heap,(0,K))    
        while heap:
            # find the shortest list
            tem_min,node = heappop(heap)
            if node not in self.collected:
                self.dis[node] = tem_min
                self.collected.add(node)
                for i in range(N):
                    if i not in self.collected and graph[node][i] > 0:
                        heappush(heap,(tem_min + graph[node][i],i))
            print(self.dis)
        max_dis = max(self.dis)
        if max_dis == float('inf'):
            return -1
        return max_dis
s = Solution()
# times = [[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2))
