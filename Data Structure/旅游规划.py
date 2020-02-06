#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-30 06:50:18
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

def find_min():
	tem_dis = 9999
	tem_index = -1
	for i in range(nodes):
		if collected[i] != 1 and tem_dis > dis[i]:
			tem_dis = dis[i]
			tem_index = i
	return tem_index


def dijkstra():
	while 1:
		cur_node = find_min()
		if cur_node == -1:
			break
		collected[cur_node] = 1
		for i in range(nodes):
			if graph[cur_node][i] > 0 and collected[i] != 1:
				if dis[i] > dis[cur_node] + graph[cur_node][i]:

					dis[i] = dis[cur_node] + graph[cur_node][i]
					cost[i] = cost[cur_node] + cost_graph[cur_node][i]

				elif dis[i] == dis[cur_node] + graph[cur_node][i] and \
				cost[i] > cost[cur_node] + cost_graph[cur_node][i]:

					cost[i] = cost[cur_node] + cost_graph[cur_node][i]


in_data = list(map(int,input().split()))
nodes = in_data[0]
edges = in_data[1]
start = in_data[2]
end = in_data[3]

dis = [999 for i in range(nodes)]
graph = list(np.full((nodes,nodes),-1,dtype = int))
cost_graph = list(np.full((nodes,nodes),999,dtype = int))

cost = [999 for i in range(nodes)]
collected = [-1 for i in range(nodes)]

count = edges

while count:
	count -= 1
	data = list(map(int,input().split()))
	graph[data[0]][data[1]] = data[2]
	graph[data[1]][data[0]] = data[2]
	cost_graph[data[0]][data[1]] = data[3]
	cost_graph[data[1]][data[0]] = data[3]

collected[start] = 1
for i in range(nodes):
	if graph[start][i] > 0:
		dis[i] = graph[start][i]
		cost[i] = cost_graph[start][i]

dijkstra()
print(dis[end],cost[end])
