#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-03 06:46:34
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

def find_min():
	index = -1
	tem_cost = 999
	for i in range(nodes):
		if cost[i] > 0 and tem_cost > cost[i]:
			index = i
			tem_cost = cost[i]
	return index

def prim(cost_count):
	while 1:
		cur_node = find_min()
		if cur_node == -1:
			break
		cost_count = cost[cur_node] + cost_count
		cost[cur_node] = 0
		for i in range(nodes):
			if graph[cur_node][i] > 0 and cost[i] !=0 and cost[i] > graph[cur_node][i]:
				cost[i] = graph[cur_node][i]

	return cost_count



in_data = list(map(int,input().split()))
nodes = in_data[0]
edges = edge_count = in_data[1]
graph = list(np.full((nodes,nodes),-1,dtype = int))
cost = [999 for i in range(nodes)]
cost_count = 0


while edge_count:
	edge_count -= 1
	tem_data = list(map(int,input().split()))
	start = tem_data[0] - 1
	end = tem_data[1] - 1
	graph[start][end] = tem_data[2]
	graph[end][start] = tem_data[2]

cost[0] = 0
for i in range(1,nodes):
	if graph[0][i] > 0:
		cost[i] = graph[0][i]

ans = prim(cost_count)
disconnect = False
for i in range(nodes):
	if cost[i] !=0:
		disconnect = True
		break
if disconnect:
	print(-1)
else:
	print(ans)