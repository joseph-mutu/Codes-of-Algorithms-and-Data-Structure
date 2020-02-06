#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-20 13:44:44
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

class node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.flag = False

def insert(tree,data):
	if tree is None:
		tree = node(data)
	else:
		if tree.data < data:
			tree.right = insert(tree.right,data)
		else:
			tree.left = insert(tree.left,data)
	return tree

def build_tree(number_node):
	tem_number = number_node
	ori_data = list(map(int,input().split()))
	ori_tree = node(ori_data[0])
	for i in range(1,number_node):
		ori_tree = insert(ori_tree,ori_data[i])

	return ori_tree

def print_tree(tree):
	if tree is not None:
		print (tree.flag)
		if tree.left is not None:
			print_tree(tree.left)
		if tree.right is not None:
			print_tree(tree.right)

def judge(ori_tree,test_data,tem_flag):

	if ori_tree.flag is True:
		if ori_tree.data < test_data:
			ori_tree = ori_tree.right
			tem_flag = judge(ori_tree,test_data,tem_flag)
			return tem_flag
		elif ori_tree.data > test_data:
			ori_tree = ori_tree.left
			tem_flag = judge(ori_tree,test_data,tem_flag)
			return tem_flag
	else: 
		if ori_tree.flag is False and (ori_tree.data == test_data):
			ori_tree.flag = True
			return tem_flag
		else:
			tem_flag = 0
			return tem_flag

def reset_tree_flag(ori_tree):
	if ori_tree is not None:
		ori_tree.flag = False
		if ori_tree.left is not None:
			reset_tree_flag(ori_tree.left)
		if ori_tree.right is not None:
			reset_tree_flag(ori_tree.right)


while 1:
	number = list(map(int,input().split()))
	if number[0]:
		number_node = int(number[0])
		number_seq = int(number[1])
		ori_tree = build_tree(number_node)
		while number_seq :
			reset_tree_flag(ori_tree)
			# print_tree(ori_tree)
			number_seq -=1
			tem_flag = 1
			test_data = list(map(int,input().split()))
			if test_data[0] != ori_tree.data :
				print("No")
			else:
				ori_tree.flag = True
				for i in range(1,number_node):
					tem_flag = judge(ori_tree,test_data[i],tem_flag)
					if tem_flag != 1:
						break
				if tem_flag != 1:
					print("No")
				else:
					print("Yes")
	else:
		break