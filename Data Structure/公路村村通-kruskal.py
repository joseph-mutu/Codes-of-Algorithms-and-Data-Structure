#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-04 09:14:16
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

class node:
	def __init__(self,data,start,end):
		self.data = data
		self.father = -1
		self.start = start
		self.end = end


def insert_heap(cur_node):
	cur_index = len(cost)
	cost.append(cur_node)
	father_index = int(cur_index/2)
	while cost[father_index].data > cost[cur_index].data:
		tem = cost[father_index]
		cost[father_index] = cost[cur_index]
		cost[cur_index] = tem
		cur_index = father_index
		father_index = int(cur_index/2)
	return 

def take():
	if len(cost) != 2:
		need = cost[1]
		cost[1] = cost[-1]
		cost.pop()
		cur_length = len(cost) - 1
		cur_index = 1
		cur_child = cur_index * 2
		while cur_child <= cur_length : 
			#找到两个孩子之间小的那个
			if cur_child != cur_length and cost[cur_child + 1].data < cost[cur_child].data:
				cur_child += 1
			if cost[cur_index].data < cost[cur_child].data:
				break
			else:
				tem = cost[cur_index]
				cost[cur_index] = cost[cur_child]
				cost[cur_child] = tem
				cur_index = cur_child
				cur_child = cur_index * 2
		return need
	else:
		need = cost[1]
		cost.pop()
		return need

def find(x):
	while city_union[x] > 0:
		x = city_union[x]
	return x

def union(cur_edge):
	city1 = cur_edge.start
	city2 = cur_edge.end
	city1_father = find(city1)
	city2_father = find(city2)
	if city_union[city1_father] < city_union[city2_father]:
		for i in range(nodes):
			if city_union[i] == city2_father:
				city_union[i] = city1_father
				city_union[city1_father] -= 1
		city_union[city2_father] = city1_father
		city_union[city1_father] -= 1
	else:
		for i in range(nodes):
			if city_union[i] == city1_father:
				city_union[i] = city2_father
				city_union[city2_father] -= 1
		city_union[city1_father] = city2_father
		city_union[city2_father] -= 1
	return 

def kruskal(edge_get,cost_count):
	while 1:
		if len(cost) == 1 or edge_get == nodes-1:
			return cost_count
			break
		cur_edge = take()
		if find(cur_edge.start) != find(cur_edge.end) or (find(cur_edge.start) == -1 and find(cur_edge.end) == -1):
			# print(cur_edge.start,cur_edge.end,cur_edge.data)
			union(cur_edge)
			cost_count += cur_edge.data
			edge_get += 1
		else:
			continue






# 先进行最小堆的建立以及删除操作
in_data = list(map(int,input().split()))
nodes = in_data[0]
edges = edge_count = in_data[1]
city_union = [-1 for i in range(nodes+1)]

cost = []
cost.append(node(-99,-1,-1)) #哨兵，堆从 1 开始计数
cost_count = 0
edge_get = 0

while edge_count:
	edge_count -= 1
	tem_data = list(map(int,input().split()))
	start = tem_data[0] 
	end = tem_data[1]
	insert_heap(node(tem_data[2],start,end))
cost_count = kruskal(edge_get,cost_count)

source = 0
disconnect = False
for i in range(1,nodes+1):
	if city_union[i] < 0:
		source += 1
	if source > 1:
		disconnect = True
		break
if disconnect:
	print(-1)
else:
	print(cost_count)
