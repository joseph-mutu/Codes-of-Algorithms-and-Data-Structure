#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-18 19:56:40
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import math
import numpy as np
import operator


max_size = 99999999
mad = 0

class hash_node:
	def __init__(self,data):
		self.data = data
		self.count = 0
		self.next = None

def max_prime(N):
	if N%2:
		tem_num = N + 2
	else:
		tem_num = N + 1
	while tem_num < max_size:
		for i in range(int(math.sqrt(tem_num)),1,-1):
			if i == 2:
				return tem_num
			elif tem_num%i == 0:
				break
		tem_num += 2

def calculate_pos(string):
	return(int(string[-5:]))

def find(pos,string):
	tem = hash_table[pos].next
	global mad
	#查找在当前 hash 位置挂着的数据中是否存在自己想找的那个
	while tem is not None:
		if operator.eq(tem.data,string):
			tem.count += 1
			if tem.count > mad_num.count:
				mad_num.data = tem.data
				mad_num.count = tem.count
				mad = 1
			elif tem.count == mad_num.count:
				mad += 1
				if int(tem.data) < int(mad_num.data):
					mad_num.data = tem.data
			return 1
		tem = tem.next
	return 0


def insert(string):
	global mad
	pos = calculate_pos(string)
	if hash_table[pos].data == -1:
		hash_table[pos].next = hash_node(string)
		hash_table[pos].next.count += 1
		hash_table[pos].data = 0
		if hash_table[pos].next.count > mad_num.count:
			mad_num.data = hash_table[pos].next.data
			mad_num.count = hash_table[pos].next.count
			mad = 1
		elif hash_table[pos].next.count == mad_num.count:
			mad += 1
			if int(hash_table[pos].next.data) < int(mad_num.data):
				mad_num.data = hash_table[pos].next.data
	else:
		if not find(pos,string):
			# 当前位置挂着的数据中，没有与当前string相同的元素
			# 需要将当前 string 挂在pos .next 上
			tem = hash_table[pos].next
			hash_table[pos].next = hash_node(string)
			hash_table[pos].next.count += 1
			hash_table[pos].next.next = tem
			if hash_table[pos].next.count > mad_num.count:
				mad_num.data = hash_table[pos].next.data
				mad_num.count = hash_table[pos].next.count
				mad = 1
			elif hash_table[pos].next.count == mad_num.count:
				mad += 1
				if int(hash_table[pos].next.data) < int(mad_num.data):
					mad_num.data = hash_table[pos].next.data
	return 0


N = int(input())
mad_num = hash_node(-1)
mad_num.count = -1

hash_table = [hash_node(-1) for i in range(max_prime(100000))]


for i in range(N):
	tem_string = input().split()
	insert(tem_string[0])
	insert(tem_string[1])
if mad == 1:
	print(mad_num.data,mad_num.count)
else:
	print(mad_num.data,mad_num.count,mad)