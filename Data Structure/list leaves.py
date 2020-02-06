#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-13 17:46:31
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
import queue

class tree:
	def __init__(self,left,right):
		self.left = left
		self.right = right

def find_root(check):
	root = check.index(0)
	return root

number_data1 = int(input())
check = list(np.zeros((number_data1),dtype = int))
data1 = []
for i in range(number_data1):
	tem = input().split()
	if tem[0] != '-':
		tem[0] = int(tem[0])
		check[int(tem[0])] = 1
	if tem[1] != '-':
		tem[1] = int(tem[1])
		check[int(tem[1])] = 1
	if tem[0] == '-':
		tem[0] = None
	if tem[1] == '-':
		tem[1] = None
	data1.append(tree(tem[0],tem[1]))
root1 = int(find_root(check))

if number_data1 == 0:
	print(0)
else:
	leaves = []
	q_leaves = queue.Queue()
	q_leaves.put(root1)
	while not q_leaves.empty():
		tem_root = q_leaves.get()
		if data1[tem_root].left != None:
			q_leaves.put(data1[tem_root].left)
		if data1[tem_root].right != None:
			q_leaves.put(data1[tem_root].right)
		if data1[tem_root].left == None and data1[tem_root].right == None:
			leaves.append(tem_root)
	print(" ".join(str(i) for i in leaves))