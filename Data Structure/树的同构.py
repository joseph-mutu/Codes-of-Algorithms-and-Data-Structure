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

def build_tree(data,number):
	real_tree = []
	for i in range(number):
		if data[i].left !='-':
			data[i].left = data[int(data[i].left)].node
		else:
			data[i].left = None
		if data[i].right !='-':
			data[i].right = data[int(data[i].right)].node
		else:
			data[i].right = None
		real_tree.append(data[i])
	return real_tree


def check_isomorphic(tree1,tree2,root1,root2,data_node2):
	if tree1[root1].node != tree2[root2].node:
		return 0
	elif tree1[root1].left != tree2[root2].right and tree1[root1].left != tree2[root2].left:
		return 0
	elif tree1[root1].right != tree2[root2].right and tree1[root1].right != tree2[root2].left:

		return 0
	else:
		for i in range(len(tree1)):
			tem_index = data_node2.index(tree1[i].node)
			tem_left = tree1[i]
			tem_right = tree2[tem_index]
			if tem_left.left != tem_right.left and tem_left.left != tem_right.right:
				# print(3.1)
				# print(tem_left.left,tem_left.right,tem_right.left,tem_right.right)
				return 0
			elif tem_left.right != tem_right.left and tem_left.right != tem_right.right:
				# print(3.2)
				return 0
		return 1


number_data1 = int(input())
if number_data1 !=0:
	check = list(np.zeros((number_data1),dtype = int))
	data1 = []
	data_node1 = []
	for i in range(number_data1):
		tem = input().split()
		tem_tree = tree(tem[0],tem[1],tem[2])
		data_node1.append(tem[0])
		data1.append(tem_tree)
		if tem[1] != '-':
			check[int(tem[1])] = 1
		if tem[2] != '-':
			check[int(tem[2])] = 1
	root1 = int(find_root(check))
	tree1 = build_tree(data1,number_data1)

 
number_data2 = int(input())
if number_data2 != 0:
	check = list(np.zeros((number_data2),dtype = int))
	data2 = []
	data_node2 = []
	for i in range(number_data2):
		tem = input().split()
		tem_tree = tree(tem[0],tem[1],tem[2])
		data2.append(tem_tree)
		data_node2.append(tem[0])
		if tem[1] != '-':
			check[int(tem[1])] = 1
		if tem[2] != '-':
			check[int(tem[2])] = 1
	root2 = int(find_root(check))
	tree2 = build_tree(data2,number_data2)
if number_data1 != number_data2 :
	print("No")
elif number_data1 == 0 and number_data2 == 0:
	print("Yes")
else:
	flag = check_isomorphic(tree1,tree2,root1,root2,data_node2)
	if flag:
		print("Yes")
	else:
		print("No")

