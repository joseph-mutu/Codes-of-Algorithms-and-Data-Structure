#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-23 19:22:40
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np



class node:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def check_dis(cur_node,want_node):
	tem_dis = np.sqrt(np.power((cur_node.x - want_node.x),2) + np.power((cur_node.y - want_node.y),2))
	if tem_dis > maxi_dis:
		return False
	else:
		return True

def check_edge(cur_node):
	if (cur_node.x + maxi_dis >= 50) or (cur_node.y + maxi_dis >= 50):
		return True
	elif (cur_node.x - maxi_dis <= -50) or (cur_node.y - maxi_dis <= -50):
		return True
	else:
		return False

def check_start(cur_node,want_node):
	tem_dis = np.sqrt(np.power((cur_node.x - want_node.x),2) + np.power((cur_node.y - want_node.y),2))
	if (tem_dis-7.5) > maxi_dis :
		return False
	else:
		return True
def check_start_edge(cur_node):
	if (cur_node.x + maxi_dis >= 42.5) or (cur_node.y + maxi_dis >= 42.5):
		return True
	elif (cur_node.x - maxi_dis <= -42.5) or (cur_node.y - maxi_dis <= -42.5):
		return True
	else:
		return False

def dfs(cur,visit):
	if check_edge(cro_list[cur]):
		global flag
		flag = 1
		return flag
	for i in range(number_cro):
		if visit[i] != 1 and check_dis(cro_list[cur],cro_list[i]):
			visit[i] = 1
			dfs(i,visit)


mess = list(map(int,input().split()))
tem_count = number_cro = mess[0]
maxi_dis = mess[1]
if number_cro == 0 and check_start_edge(cur_node):
	print("Yes")
elif number_cro == 0 and (check_start_edge(cur_node) == False) :
	print(1)
	print("No")
else:
	visit = [-1 for i in range(number_cro)]
	cro_list = []
	start_node = node(0,0)

	while tem_count :
		tem_count -= 1
		coords = list(map(int,input().split()))
		cor_x = coords[0]
		cor_y = coords[1]
		cro_list.append(node(cor_x,cor_y))
	flag = -1
	for i in range(number_cro):
		if check_start(start_node,cro_list[i]):
			visit[i] = 1
			dfs(i,visit)
	if flag < 0:
		print("No")
	else:
		print("Yes")
