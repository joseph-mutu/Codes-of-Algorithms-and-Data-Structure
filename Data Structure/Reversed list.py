#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-22 17:26:08
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class node:
	def __init__(self,address,data,next):
		self.address = address
		self.data = data
		self.next = next

def creat_link(number_node,data,start_add):
	root = -99
	while number_node:
		tem_data = list(map(int,input().split()))
		tem_node = node(tem_data[0],tem_data[1],tem_data[2])
		if tem_data[0] == start_add:
			root = tem_node
