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

def rotateRR(root):
	tem_tree = root.right
	root.right = tem_tree.left
	tem_tree.left = root
	root = tem_tree
	return root

def rotateLL(root):
	tem_tree = root.left
	root.left = tem_tree.right
	tem_tree.right = root
	root = tem_tree
	return root

def rotateLR(root):
	root.left = rotateRR(root.left)
	return rotateLL(root)

def rotateRL(root):
	root.right = rotateLL(root.right)
	return rotateRR(root)

def insert(tree,data):
	if tree is None:
		tree = node(data)
		return tree
	else:
		if tree.data < data:
			tree.right = insert(tree.right,data)
			if np.abs(get_height(tree.left) - get_height(tree.right)) == 2 :
				if data > tree.right.data:
					tree = rotateRR(tree)
				else:
					tree = rotateRL(tree)
		else:
			tree.left = insert(tree.left,data)
			if np.abs(get_height(tree.left) - get_height(tree.right)) == 2:		
				if data > tree.left.data:
					tree = rotateLR(tree)
				else:
					tree = rotateLL(tree)
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


def get_height(root):
	if root is not None:
		return max(get_height(root.left),get_height(root.right))+1
	else:
		return 0

number_node = int(input())
root = build_tree(number_node)
print(root.data)
