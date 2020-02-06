#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-22 21:08:55
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

def bfs(graph,node_list_bfs,result_list,visit_bfs):
	if len(node_list_bfs) == 0:
		print("{"," ".join(str(i) for i in result_list),"}")
		return result_list
	else:
		cur_node = node_list_bfs.pop(0)
		visit_bfs[cur_nosde] = 1
		result_list.append(cur_node)
		for i in range(len(graph)):
			if graph[cur_node,i] > 0 and visit_bfs[i] == -1:
				node_list_bfs.append(i)
				visit_bfs[i] = 1
		bfs(graph,node_list_bfs,result_list,visit_bfs)

def dfs(graph,node_list_dfs,result_list,visit_dfs):
	cur_node = node_list_dfs.pop(0)
	visit_dfs[cur_node] = 1
	result_list.append(cur_node)
	for i in range(len(graph)):
		if graph[cur_node,i] > 0 and visit_dfs[i] == -1:
			node_list_dfs.append(i)
			dfs(graph,node_list_dfs,result_list,visit_dfs)
	if len(node_list_dfs) == 0:
		return 

data = list(map(int,input().split()))
number_nodes = data[0]
number_edge = data[1]
tem_cou = number_edge
graph = np.full((number_nodes,number_nodes),-1,dtype = int)
visit_bfs = [-1 for i in range(number_nodes)]
visit_dfs = [-1 for i in range(number_nodes)]

while tem_cou:
	inp_node = list(map(int,input().split()))
	graph[inp_node[0],inp_node[1]] = 1
	graph[inp_node[1],inp_node[0]] = 1
	tem_cou -= 1

node_list_dfs = []
for i in range(number_nodes):
	if visit_dfs[i] != 1:
		result_list = []
		node_list_dfs.append(i)
		dfs(graph, node_list_dfs, result_list,visit_dfs)
		print("{"," ".join(str(i) for i in result_list),"}")


node_list_bfs = []
for i in range(number_nodes):
	if visit_bfs[i] != 1:
		result_list = []
		node_list_bfs.append(i)
		bfs(graph, node_list_bfs, result_list,visit_bfs)



