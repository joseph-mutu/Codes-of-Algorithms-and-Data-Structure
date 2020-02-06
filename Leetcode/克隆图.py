#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-07 07:25:43
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Node:
	def __init__(self, val, neighbors):
		self.val = val
		self.neighbors = neighbors

class Solution:
	def cloneGraph(self, node):
		if not node:
			return None
		node_que = []
		node_que.append(node)

		clone_node = Node(node.val,[])
		clone_nodes_vis = {node:clone_node}

		self.bfs(node_que,clone_nodes_vis)

		return clone_node


	def bfs(self,node_que,clone_nodes_vis):
		while node_que:
			cur_node = node_que.pop()
			for neigh in cur_node.neighbors:
				if clone_nodes_vis.get(neigh):
					clone_nodes_vis[cur_node].neighbors.append(clone_nodes_vis[neigh])
				else:
					tem_clone = Node(neigh.val,[])
					clone_nodes_vis[neigh] = tem_clone
					clone_nodes_vis[cur_node].neighbors.append(clone_nodes_vis[neigh])
					node_que.append(neigh)
		return 

	def dfs(self,node,clone_nodes_vis):
		for neigh in node.neighbors:
			if clone_nodes_vis.get(neigh):
				clone_nodes_vis[node].neighbors.append(clone_nodes_vis[neigh])
			else:
				tem_clone = Node(neigh.val,[])
				clone_nodes_vis[neigh] = tem_clone
				clone_nodes_vis[node].neighbors.append(tem_clone)
				self.dfs(neigh,clone_nodes_vis)
		return 


