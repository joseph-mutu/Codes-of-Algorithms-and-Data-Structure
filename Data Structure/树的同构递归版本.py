#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-13 17:46:31
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

class tree:
	def __init__(self,node,left,right):
		self.node = node
		self.left = left
		self.right = right

def find_root(check):
	root = check.index(0)
	return root

def check_isomorphic(data1,root1,data2,root2,):
	if root1 == None and root2 == None:
		return 1
	if (root1 == None and root2 != None) or (root1 != None and root2 == None) :
		return 0
	if data1[root1].node != data2[root2].node :
		return 0
	if data1[root1].left == None and data2[root2].left == None :
		return check_isomorphic(data1,data1[root1].right,data2,data2[root2].right)
	if data1[root1].left != None and data2[root2].left != None and (data1[data1[root1].left].node == data2[data2[root2].left].node) :
		return check_isomorphic(data1,data1[root1].left,data2,data2[root2].left) and check_isomorphic(data1,data1[root1].right,data2,data2[root2].right)
	else:
		return check_isomorphic(data1,data1[root1].left,data2,data2[root2].right) and check_isomorphic(data1,data1[root1].right,data2,data2[root2].left)

	return 0


number_data1 = int(input())
check = list(np.zeros((8),dtype = int))
data1 = []
for i in range(number_data1):
	tem = input().split()
	if tem[1] != '-':
		tem[1] = int(tem[1])
		check[int(tem[1])] = 1
	if tem[2] != '-':
		tem[2] = int(tem[2])
		check[int(tem[2])] = 1
	if tem[1] == '-':
		tem[1] = None
	if tem[2] == '-':
		tem[2] = None
	data1.append(tree(tem[0],tem[1],tem[2]))
root1 = int(find_root(check))

number_data2 = int(input())
check = list(np.zeros((8),dtype = int))
data2 = []
for i in range(number_data2):
	tem = input().split()
	if tem[1] != '-':
		tem[1] = int(tem[1])
		check[int(tem[1])] = 1
	if tem[2] != '-':
		tem[2] = int(tem[2])
		check[int(tem[2])] = 1
	if tem[1] == '-':
		tem[1] = None
	if tem[2] == '-':
		tem[2] = None
	data2.append(tree(tem[0],tem[1],tem[2]))
root2 = int(find_root(check))
# for i in range(number_data1):
# 	print(data1[i].node,data1[i].left,data1[i].right)
# for i in range(number_data1):
# 	print(data2[i].node,data2[i].left,data2[i].right)
if check_isomorphic(data1,root1,data2,root2):
	print("Yes")
else:
	print('No')
