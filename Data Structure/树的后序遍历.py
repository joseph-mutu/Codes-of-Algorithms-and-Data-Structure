#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-24 20:32:00
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

def find_postorder(pre_pos,mid_pos,pos_pos,cur_len):
	if cur_len == 0:
		return
	if cur_len == 1:
		pos_order[pos_pos] = pre_order[pre_pos]
		return
	root = pre_order[pre_pos]
	pos_order[pos_pos + cur_len - 1] = root

	node = mid_order.index(root) - mid_pos
	left = node
	right = cur_len - node - 1


	find_postorder(pre_pos + 1,mid_pos,pos_pos,left)
	find_postorder(pre_pos + left+ 1, mid_pos + left + 1,pos_pos + left,right)


number_node = int(input())
count = 2*number_node
nodes = []
pre_order = []
mid_order = []
pos_order = np.full((1,number_node),-1,dtype = int).flatten()

while count:
	count -= 1
	in_node = list(input().split())
	if in_node[0] == "Push":
		nodes.append(int(in_node[1]))
		pre_order.append(int(in_node[1]))
	elif in_node[0] == "Pop" :
		mid_order.append(nodes.pop())
find_postorder(0,0,0,len(pre_order))
print(" ".join(str(i) for i in pos_order))
