#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-19 18:26:40
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution(object):
    def networkDelayTime(self, times, N, K):
        if K > N or K <= 0:
            return -1
        # 首先使用邻接矩阵存储图
        graph = [[-1]*N for _ in range(N)]
        for x,y,w in times:
            graph[x-1][y-1] = w
        dis = [float('inf') for _ in range(N)] 
        dis[K-1] = 0
        print(graph,dis)
        # 对源点周围的点进行初始化
        for i in range(N):
            if graph[K-1][i] >= 0:
                dis[i] = graph[K-1][i]
        collected = [False]*N
        collected[K-1] = True

        while 1:
            # find the minimal distance that is not collected
            min_dis = float('inf')
            node = -1
            for i in range(N):
                if collected[i] is False and dis[i] < min_dis:
                    min_dis = dis[i]
                    node = i
            if node == -1 :
                break
            collected[node] = True
            print(node,collected,dis)
            for i in range(N):
                # 两点之间存在边,且当前邻节点没有被收录
                if graph[node][i] >= 0 and collected[i] is False:
                    # 如果临节点的最短距离可以被当前节点更新
                    if dis[i] > dis[node] + graph[node][i]:
                        dis[i] = dis[node] + graph[node][i]
        if max(dis) == float('inf'):
            return -1
        return max(dis)

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
s = Solution()
print(s.networkDelayTime(times,N,K))





