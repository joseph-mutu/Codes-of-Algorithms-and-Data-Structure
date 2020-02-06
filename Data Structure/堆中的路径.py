#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-22 09:38:59
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

def insert(heap,data):
	i = int(len(heap))
	heap.append(data)
	while heap[int(i/2)] > heap[i] :
		tem = heap[i]
		heap[i] = heap[int(i/2)]
		heap[int(i/2)] = tem
		i = int(i/2)
	return heap

def print_node(pos,heap):
	ans = []
	while pos:
		ans.append(heap[pos])
		pos = int(pos/2)
	return ans

input_number = list(map(int,input().split()))
number_node = input_number[0]
number_seq = input_number[1]
heap = [-99999]
data = list(map(int,input().split()))
pos = list(map(int,input().split()))
for i in range(len(data)):
	heap = insert(heap,data[i])

for i in range(len(pos)):
	ans = print_node(pos[i],heap)
	print(" ".join(str(i) for i in ans))