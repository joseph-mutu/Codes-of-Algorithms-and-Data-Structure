#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-27 06:59:29
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import math 

def get_len(n):
	if n == 1:
		return [0,0]
	n = n-1
	left_right = []
	layer = int(math.log(n+1,2)) - 1
	tem_total = 2*pow(2,layer) - 2
	remin = n - tem_total# 在完整的层数中，一共有多少个节点
	left = tem_total/2
	right = tem_total/2

	#分属于左子树以及右子树余数的个数
	tem_layer_nodes = pow(2,layer + 1)/2
	if remin <= tem_layer_nodes: 
		left = left + remin
	elif remin > tem_layer_nodes:
		left = left + tem_layer_nodes
		right = right + remin - tem_layer_nodes
	left_right.append(int(left))
	left_right.append(int(right))
	return left_right


def complete_tree(start,end,len,num):
	if len == 0:
		return
	left_right = get_len(len)
	left = left_right[0]
	right = left_right[1]
	root = data[start+left]

	ans_tree[num] = root

	complete_tree(start,left,left,2*num+1)
	complete_tree(start+left+1,start+left+right,right,2*num+2)



number_nodes = int(input())
data = list(map(int,input().split()))
data.sort()
ans_tree = [-1 for i in range(number_nodes)]
complete_tree(0,number_nodes-1,number_nodes,0)
print(" ".join(str(i) for i in ans_tree))
