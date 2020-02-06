#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-28 10:20:12
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

data_input = list(map(int,input().split()))
nodes = data_input[0]
count = edges = data_input[1]
dis = np.full((nodes,nodes),999,dtype = int)
for i in range(nodes):
	dis[i,i] = 0

min_data =[]
min_index = []



while count:
	count -= 1
	data = list(map(int,input().split()))
	tem_node1 = data[0] - 1
	tem_node2 = data[1] - 1
	weight = data[2]
	dis[tem_node1,tem_node2] = weight
	dis[tem_node2,tem_node1] = weight
for k in range(nodes):
	for i in range(nodes):
		for j in range(nodes):
			if dis[i,k] + dis[k,j] < dis[i,j]:
				dis[i,j] = dis[i,k] + dis[k,j]
				dis[j,i] = dis[i,k] + dis[k,j]
for i in range(nodes):
	tem_min = max(dis[i,])
	tem_index = list(dis[i,]).index(tem_min)
	min_data.append(tem_min)
ans = []
ans.append(min_data.index(min(min_data)) + 1)
ans.append(min(min_data))
if ans[1] == 999:
	print(0)
else:
	print(" ".join(str(i) for i in ans))